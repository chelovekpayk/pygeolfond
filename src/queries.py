# Переменные для создания запроса


# Список фильтров
lfilt = {
    "oil": "Н - Углеводородное сырье",
    "water": "В - Подземные воды (за исключением подземных минеральных вод)",
    "drag_met": "Б - Драгоценные металлы (золото, серебро, платина и металлы платиновой группы)",
    "radioact": "З - Подземное пространство, используемое для строительства и эксплуатации подземных сооружений для захоронения радиоактивных отходов (пунктов захоронения), отходов производства и потребления I - V классов опасности (объектов захоронения отходов)",
    "drag_stones": "К - Драгоценные камни (природные алмазы, изумруды, рубины, сапфиры, александриты)",
    "min_waters": "М - Подземные минеральные воды, лечебные грязи, специфические минеральные ресурсы (рапа лиманов и озер, сапропель и другие)",
    "sci_obj": "О - Подземное пространство, используемое для образования особо охраняемых геологических объектов, имеющих научное, культурное, эстетическое, санитарно-оздоровительное и иное значение (научные и учебные полигоны, геологические заповедники, заказники, памятники природы, пещеры и другие подземные полости), сбора минералогических, палеонтологических и других геологических коллекционных материалов",
    "non_radioactive": "П - Подземное пространство, используемое для строительства и эксплуатации подземных сооружений (за исключением подземных сооружений для захоронения радиоактивных отходов (пунктов захоронения), отходов производства и потребления I - V классов опасности (объектов захоронения отходов), для строительства и эксплуатации хранилищ углеводородного сырья, размещения в пластах горных пород попутных вод и вод, использованных пользователями недр для собственных производственных и технологических нужд при разведке и добыче углеводородного сырья, размещения в пластах горных пород вод, образующихся у пользователей недр, осуществляющих разведку и добычу, а также первичную переработку калийных и магниевых солей",
    "hard": "Т - Твердые полезные ископаемые",
}


# Сконвертированные переменные для запроса
url = "https://bi.rfgf.ru/corelogic/api/query"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    "Authorization": "Bearer NoAuth",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://bi.rfgf.ru",
    "Connection": "keep-alive",
    "Referer": "https://bi.rfgf.ru/viewer/public?dashboardGuid=ae176f70a6df4e81ba10247f44fb1191&showNav=false&fit=false",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    "QueryType": "GetRawOlapData+Query",
    "RawOlapSettings": {
        "databaseId": "Main",
        "measureGroup": {
            "columns": [
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "c64a19c50c394605981e3ebe87918ae1",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "rcart_link",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "7c57c1b9e5b74322b5976eff809e3c20",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "lc_number_full",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "b146527321b840668975b16507194d33",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "has_doc",
                },
                {
                    "type": "RawOlapDimensionRoleAttributeColumnDto",
                    "kind": "RawOlapDimensionRoleAttributeColumnDto",
                    "guid": "3766824573874611bc87322d41091f2f",
                    "dimensionRoleId": {
                        "type": "DimensionRoleIdDto",
                        "kind": "DimensionRoleIdDto",
                        "value": "date_reg_start",
                    },
                    "attributeId": "DATE",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "dd98c164c5234359b58909f9b96f10da",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "purpose",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "0c54fe57b031469686122724a10fca61",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "lc_cat_type_abr_with_pi",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "7514ae69824d42fb999a6630fc6b902d",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "area_nedr_name",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "f5cd97e6be364c82a48e8bad88682e32",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "region_name_sf",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "15dfc1c77ad34713acd832b0b28cba33",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "koord",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "89880068c9514a94b74dd1ac6326c4ee",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "stat_uch",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "55928c0365254e989776b22c2ad91133",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "company_name",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "30e8b6fcda754620b37a8808eaad9822",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "organ",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "1565bb98bd09479dbb14db2a63d04ad6",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "doc_lic",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "8b0d834417a14859940ba47a37420323",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "doc_dopoln",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "86006ff857ee48c0b94c27a5c82743e4",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "lc_number_full_new",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "24644a616cba4dcba8369c584ba1cfea",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "annul_doc",
                },
                {
                    "type": "RawOlapDimensionRoleAttributeColumnDto",
                    "kind": "RawOlapDimensionRoleAttributeColumnDto",
                    "guid": "17bd7207b3b14433803e97480f5dc2a4",
                    "dimensionRoleId": {
                        "type": "DimensionRoleIdDto",
                        "kind": "DimensionRoleIdDto",
                        "value": "annul_date",
                    },
                    "attributeId": "DATE",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "930bb47ba3b242b2b91e81d457692a54",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "pause_dates",
                },
                {
                    "type": "RawOlapDimensionRoleAttributeColumnDto",
                    "kind": "RawOlapDimensionRoleAttributeColumnDto",
                    "guid": "a46c3241eeae4c5e9d81d71f84c03eab",
                    "dimensionRoleId": {
                        "type": "DimensionRoleIdDto",
                        "kind": "DimensionRoleIdDto",
                        "value": "date_reg_end",
                    },
                    "attributeId": "DATE",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "d02af800021e4f559a1120bae16e692f",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "num_rann_lic",
                },
                {
                    "type": "RawOlapDimensionAttributeColumnDto",
                    "kind": "RawOlapDimensionAttributeColumnDto",
                    "guid": "1fb7dfc7907545899a8bf78dc7c655b2",
                    "dimensionId": {
                        "type": "DimensionIdDto",
                        "kind": "DimensionIdDto",
                        "value": "R_litsenziya",
                    },
                    "attributeId": "asln_link",
                },
            ],
            "filters": [
                [
                    {
                        "selectedFilterValues": [
                            "Н - Углеводородное сырье",
                        ],
                        "attributeId": "S_rasshifrovkoi",
                        "dimensionOrDimensionRoleId": {
                            "type": "DimensionIdDto",
                            "kind": "DimensionIdDto",
                            "value": "R_litsenziya",
                        },
                        "useExcluding": False,
                    },
                ],
            ],
            "times": [],
            "id": "R_Reestr_litsenzii",
        },
        "lazyLoadOptions": {
            "columnSorts": [
                {
                    "columnindex": 3,
                    "order": 1,
                },
            ],
            "offset": 0,
            "limit": 20,
        },
    },
    "CalculationQueries": [],
    "AdditionalLogs": {
        "widgetGuid": "245d52ef1fdc474a8795fc37a8d03d02",
        "dashboardGuid": "ae176f70a6df4e81ba10247f44fb1191",
        "sheetGuid": "23760aa1c3844e9686946dfac2d0e8a0",
    },
    "WidgetGuid": "245d52ef1fdc474a8795fc37a8d03d02",
}
