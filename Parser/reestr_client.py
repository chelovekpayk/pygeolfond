#!venv/bin/python3
# -*- coding=utf-8 -*-

"""
Модуль для запроса к серверу и получения сырых данных
"""

import os
import requests
import socks
import socket

from .headers import url as _url
from .headers import headers as _headers 
from .headers import json_data as _json_data
from .headers import cols as _cols
from .headers import filter as _filter

class ReestrRequest:
    """Создание объекта данных из реестра Роснедр https://rfgf.ru/ReestrLic/"""

    def __init__(self):

        # Переменные для запроса
        self.url: str = _url
        self.headers: dict = _headers

        # Подстановка нужного фильтра в POST запрос
        self.json_data: dict = _json_data

        # Количество записей в запросе. Для получения всех записей надо делать тестовый запрос
        # Полученное количество записей подставить в сдлвать для следующего запроса
        self.json_data["RawOlapSettings"]["lazyLoadOptions"]["limit"] = 1
        
        # Создание объекта сессии 
        self.session = requests.Session()

    def config(self):
        """Запуск конфигурации из файла конфигурации config.ini"""
        
        # Блок проверки наличия config.ini
        if os.path.exists("Parser/config.ini"):
            from configparser import ConfigParser

            config = ConfigParser()
            config.read("Parser/config.ini")

            os.environ['DATA_FOLDER_PATH'] = os.path.abspath(config["DEFAULT"]["data_folder"])
            self.logfile = os.path.abspath(config["DEFAULT"]["logfile"])
            

            # Настройки для прокси через российский VDS
            if "PROXY" in config:
                proxy_host = config["PROXY"]["proxy_host"]
                proxy_port = config["PROXY"]["proxy_port"]

                socks.set_default_proxy(socks.SOCKS5, proxy_host, proxy_port)
                socket.socket = socks.socksocket
                self.session.proxies = {"https": f"socks5://{proxy_host}:{proxy_port}"}

            # Настройка SSL
            if "SSL" in config:
                cert = os.path.relpath(config["SSL"]["key"], os.getcwd())
                self.session.verify = cert
        else:
            #requests.packages.urllib3.disable_warnings()  # отключить ошибку SSL-сертификата
            self.session.verify = False
            self.path = os.getcwd()

    def get_record_count(self):
        """
        Метод для получения количества записей.
        """

        #Создание запроса
        response = self.session.post(
            self.url, headers=self.headers, json=self.json_data
        ).json()
        self.json_data["RawOlapSettings"]["lazyLoadOptions"]["limit"] = int(
            response["result"]["recordCount"]
        )

    def get_data_from_reestr(self, filter: str = "oil") -> tuple[list, str]:
        """
        Метод делает запросы к базе данных Роснедр.
        Возращает плоский Python-словарь с данными.
        """
        # Переменная фильтра для запроса
        self.filter = _filter(filter) 
        
        self.json_data["RawOlapSettings"]["measureGroup"]["filters"][0][0][
            "selectedFilterValues"
        ] = [self.filter[1]]

        # Запрос для получения всех записей выгрузки
        self.get_record_count()
        response = self.session.post(
            self.url, headers=self.headers, json=self.json_data
        ).json()

        # Подготовка данных
        response["result"]["data"]["cols"][16] = ["Дата.1"]
        response["result"]["data"]["cols"][18] = ["Дата.2"]

        cols = [x.replace(k, v) for x in [v[0] for v in response["result"]["data"]["cols"]] for k, v in _cols.items() if x == k]
        vals = response["result"]["data"]["values"]

        # Плоский список словарей-строк в которых столбец:значение
        data: list = [{key:vals[n][i] for n, key in enumerate(cols)} for i in range(len(vals[0]))]

        #Возващает список словарей-строк и фильтр
        return data, self.filter[0]
