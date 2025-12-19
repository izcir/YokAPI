selectors = {
    "genel_blg": {
        "table1": {
            "index": 1,
            "bolum": "thead > tr > th > big",
            "rows": "tbody > tr",
            "datas": [
                {"name": "program_kod", "index": 1, "type": "int"},
                {"name": "uni_tur", "index": 2, "type": "str"},
                {"name": "uni", "index": 3, "type": "str"},
                {"name": "fakulte", "index": 4, "type": "str"},
                {"name": "puan_tur", "index": 5, "type": "str"},
                {"name": "burs_tur", "index": 6, "type": "str"}
            ]
        },
        "table2": {
            "index": 2,
            "rows": "tbody > tr",
            "datas": [
                {"name": "genel_kontenjan", "index": 1, "type": "int"},
                {"name": "ob_kontenjan", "index": 2, "type": "int"},
                {"name": "toplam_kontenjan", "index": 3, "type": "int"},
                {"name": "genel_yerlesen", "index": 4, "type": "int"},
                {"name": "ob_yerlesen", "index": 5, "type": "int"},
                {"name": "toplam_yerlesen", "index": 6, "type": "int"},
                {"name": "bos_kontenjan", "index": 7, "type": "int"},
                {"name": "ilk_yer_oran", "index": 8, "type": "yuzde"},
                {"name": "kayit_yaptirmayan", "index": 9, "type": "int"},
                {"name": "ek_yerlesen", "index": 10, "type": "int"}
            ]
        },
        "table3": {
            "index": 3,
            "rows": "tbody > tr",
            "datas": [
                {"name": "yer_012_son_puan", "index": 1, "type": "float"},
                {"name": "yer_018_son_puan", "index": 2, "type": "float"},
                {"name": "yer_012_son_sira", "index": 3, "type": "int"},
                {"name": "yer_018_son_sira", "index": 4, "type": "int"},
                {"name": "tavan_puan", "index": 5, "type": "float"},
                {"name": "tavan_basari_sira", "index": 6, "type": "int"},
                {"name": "obp_kirilan", "index": 7, "type": "int"},
                {"name": "ort_obp", "index": 8, "type": "float"},
                {"name": "ort_diploma", "index": 9, "type": "float"}
            ]
        }
    },
    "genel_blg_onlisans" : {
        "table1": {
            "index": 1,
            "bolum": "thead > tr > th > big",
            "rows": "tbody > tr",
            "datas": [
                {"name": "program_kod", "index": 1, "type": "int"},
                {"name": "uni_tur", "index": 2, "type": "str"},
                {"name": "uni", "index": 3, "type": "str"},
                {"name": "fakulte", "index": 4, "type": "str"},
                {"name": "puan_tur", "index": 5, "type": "str"},
                {"name": "burs_tur", "index": 6, "type": "str"}
            ]
        },
        "table2": {
            "index": 2,
            "rows": "tbody > tr",
            "datas": [
                {"name": "genel_kontenjan", "index": 1, "type": "int"},
                {"name": "ob_kontenjan", "index": 2, "type": "int"},
                {"name": "toplam_kontenjan", "index": 3, "type": "int"},
                {"name": "genel_yerlesen", "index": 4, "type": "int"},
                {"name": "ob_yerlesen", "index": 5, "type": "int"},
                {"name": "toplam_yerlesen", "index": 6, "type": "int"}
            ]
        },
        "table3": {
            "index": 3,
            "rows": "tr",
            "datas": [
                {"name": "bos_kontenjan", "index": 7, "type": "int"},
                {"name": "ilk_yer_oran", "index": 8, "type": "yuzde"},
                {"name": "kayit_yaptirmayan", "index": 9, "type": "int"},
                {"name": "ek_yerlesen", "index": 10, "type": "int"}
            ]
        },
        "table4_2024": {
            "index": 4,
            "rows": "tbody > tr",
            "datas": [
                {"name": "yer_012_son_puan", "index": 1, "type": "float"},
                {"name": "yer_018_son_puan", "index": 2, "type": "float"},
                {"name": "yer_012_son_sira", "index": 3, "type": "int"},
                {"name": "yer_018_son_sira", "index": 4, "type": "int"},
                {"name": "tavan_2024_puan", "index": 7, "type": "float"},
                {"name": "tavan_2024_sira", "index": 8, "type": "int"},
                {"name": "ort_obp_2024", "index": 9, "type": "float"},
                {"name": "ort_dn_2024", "index": 10, "type": "float"}
            ]
        },

        
        "table4": {
            "index": 4,
            "rows": "tbody > tr",
            "datas": [
                {"name": "yer_012_son_puan", "index": 1, "type": "float"},
                {"name": "yer_018_son_puan", "index": 2, "type": "float"},
                {"name": "yer_012_son_sira", "index": 3, "type": "int"},
                {"name": "yer_018_son_sira", "index": 4, "type": "int"},
                
            ]
        },
    },
    
    "kontenjan": {
        "rows": "tbody > tr",
        "ek_yer": {"name": "ek_yer", "selector":"div[align='left']:last-of-type", "type": "int"},
        "datas":[
            {"name": "kont_gte",   "index": 1, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "genel_kont", "index": 1, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "yer_oran",   "index": 1, "selector":"td:nth-child(4)", "type": "yuzde"},
            {"name": "kesn_kayt",  "index": 1, "selector":"td:nth-child(5)", "type": "int"},
            {"name": "kayt_yptrmyn", "index": 1, "selector":"td:nth-child(6)", "type": "int"},
            {"name": "tubitak",    "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "engelli",    "index": 3, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "okl_bir_kont", "index": 4, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "okl_bir_yer", "index": 4, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "t_kont", "index": 5, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "t_yer", "index": 5, "selector":"td:nth-child(3)", "type": "int"},
        ]
    },
    "kontenjan_onlisans": {
        "rows": "tbody > tr",
        "ek_yer": {"name": "ek_yer", "selector":"div[align='left']:last-of-type", "type": "int"},
        "datas":[
            {"name": "kont_gte",   "index": 1, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "genel_kont", "index": 1, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "yer_oran",   "index": 1, "selector":"td:nth-child(4)", "type": "yuzde"},
            {"name": "kesn_kayt",  "index": 1, "selector":"td:nth-child(5)", "type": "int"},
            {"name": "kayt_yptrmyn", "index": 1, "selector":"td:nth-child(6)", "type": "int"},
            {"name": "tubitak",    "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "engelli",    "index": 3, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "okl_bir_kont", "index": 4, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "okl_bir_yer", "index": 4, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "t_kont", "index": 4, "selector":"td:nth-child(5)", "type": "int"},
            {"name": "t_yer", "index": 4, "selector":"td:nth-child(6)", "type": "int"},
        ]
    },

    "cinsiyet": {
        "rows": "tbody > tr",
        "datas":[
            {"name": "erkek", "index": 1, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "erkek_orn", "index": 1, "selector":"td:nth-child(3)", "type": "yuzde"},
            {"name": "kadin", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "kadin_orn", "index": 2, "selector":"td:nth-child(3)", "type": "yuzde"}
        ]
    },
    "cograf_bolg": {
        "sehir_rows":"table:nth-child(1) > tbody > tr",
        "bolge_rows":"table:nth-child(6) > tbody > tr",
        "sehr_json": {
                    'Toplam'        : {'sayi': None, 'orn': None, 'erkek': None, 'kadin': None},
                    'Aynı Şehir'    : {'sayi': None, 'orn': None, 'erkek': None, 'kadin': None},
                    'Farklı Şehir'  : {'sayi': None, 'orn': None, 'erkek': None, 'kadin': None},
                    'Belli Değil'   : {'sayi': None, 'orn': None, 'erkek': None, 'kadin': None}
                },
        "bolge_json":{
                    "Toplam"            : {"sayi": None, "orn": None},
                    "Akdeniz"           : {"sayi": None, "orn": None},
                    "Doğu Anadolu"      : {"sayi": None, "orn": None},
                    "Ege"               : {"sayi": None, "orn": None},
                    "Güneydoğu Anadolu" : {"sayi": None, "orn": None},
                    "İç Anadolu"        : {"sayi": None, "orn": None},
                    "Karadeniz"         : {"sayi": None, "orn": None},
                    "Marmara"           : {"sayi": None, "orn": None},
                    "Belli Değil"       : {"sayi": None, "orn": None}
                },
        "sehir_datas":[
           {"name":"sehir_text", "index": 1, "selector":"td.text-left", "type":"str"},
           {"name":"sehir_sayi", "index": 2,"selector":"td:nth-child(2)", "type":"int"},
           {"name":"sehir_orn", "index": 3,"selector":"td:nth-child(3)", "type":"yuzde"},
           {"name":"sehir_cins", "index": 4,"selector":"td:nth-child(4)", "type":"str"},
        ],
        "bolge_datas":[
           {"name":"bolge_text", "index": 1,"selector":"td:nth-child(1)", "type":"str"},
           {"name":"bolge_sayi", "index": 2,"selector":"td:nth-child(2)", "type":"int"},
           {"name":"bolge_orn", "index": 3,"selector":"td:nth-child(3)", "type":"yuzde"}
        ]
    },
    "iller": {
        "rows": "table > tbody > tr",
        "datas":[
            {"name": "il", "index": 1, "selector":"td:nth-child(1) > div", "type": "str"},
            {"name": "sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn", "index": 3, "selector":"td:nth-child(3)", "type": "yuzde"}
        ]
    },
    "ogr_durum": {
        "rows": "tbody > tr",
        "datas":[
            {"name": "sayi", "index": 1, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn",  "index": 1, "selector":"td:nth-child(3)", "type": "yuzde"},
            {"name": "sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn",  "index": 2, "selector":"td:nth-child(3)", "type": "yuzde"},
            {"name": "sayi", "index": 3, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn",  "index": 3, "selector":"td:nth-child(3)", "type": "yuzde"},
            {"name": "sayi", "index": 4, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn",  "index": 4, "selector":"td:nth-child(3)", "type": "yuzde"},
            {"name": "sayi", "index": 5, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn",  "index": 5, "selector":"td:nth-child(3)", "type": "yuzde"},
            {"name": "sayi", "index": 6, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn",  "index": 6, "selector":"td:nth-child(3)", "type": "yuzde"},
        ]
    },
    "mezun_yil": {
        "rows": "table > tbody > tr",
        "datas":[
            {"name": "yil", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn", "index": 3, "selector":"td:nth-child(3)", "type": "yuzde"}
        ]
    },
    "lise_alan": {
        "rows": "table > tbody > tr",
        "datas":[
            {"name": "alan", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn", "index": 3, "selector":"td:nth-child(3)", "type": "yuzde"}
        ]
    },
    "lise_grup_tip": {
        "genel_lise_rows": "table:nth-child(4) > tbody > tr",
        "meslek_lise_rows": "table:nth-child(5) > tbody > tr",
        "datas":[
            {"name": "alan", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn", "index": 3, "selector":"td:nth-child(3)", "type": "yuzde"}
        ]
    },
    "liseler": {
        "rows": "table > tbody > tr",
        "datas":[
            {"name": "lise_ismi", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "lise_toplam", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "yeni_mezun", "index": 3, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "eski_mezun", "index": 4, "selector":"td:nth-child(4)", "type": "int"}
        ]
    },
    "okul_birinci": {
        "tbody1_rows": "table:nth-child(1) > tbody > tr",
        "tbody2_rows": "table:nth-child(3) > tbody > tr",
        "tbody1_datas":[
            {"name": "kont_turu", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "kont_sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"},

        ],
        "tbody2_datas":[
            {"name": "kont_turu", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "okul_ismi", "index": 2, "selector":"td:nth-child(2)", "type": "str"},
        ]
    },
    "taban_puan": {
        "puan_rows": "table:nth-child(1) > tbody > tr",
        "sira_rows": "table:nth-child(3) > tbody > tr",
        "puan_datas":[
            {"name": "kont_turu", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "kontenjan", "index": 1, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "yerlesen", "index": 1, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "puan", "index": 1, "selector":"td:nth-child(4)", "type": "float"},
            {"name": "kont_turu", "index": 2, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "kontenjan", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "yerlesen", "index": 2, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "puan", "index": 2, "selector":"td:nth-child(4)", "type": "float"},
            
        ],
        "sira_datas":[
            {"name": "kont_turu", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "kontenjan", "index": 1, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "yerlesen", "index": 1, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "sira_012", "index": 1, "selector":"td:nth-child(4)", "type": "int"},
            {"name": "sira_012_006", "index": 1, "selector":"td:nth-child(5)", "type": "int"},
            {"name": "kont_turu", "index": 2, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "kontenjan", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "yerlesen", "index": 2, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "sira_012", "index": 2, "selector":"td:nth-child(4)", "type": "int"},
            {"name": "sira_012_006", "index": 2, "selector":"td:nth-child(5)", "type": "int"},    
        ]
    },
    "taban_puan_onlisans":{
        "puan_rows": "table:nth-child(1) > tbody > tr",
        "sira_rows": "table:nth-child(3) > tbody > tr",
        "puan_datas":[
            {"name": "kont_turu", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "kontenjan", "index": 1, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "yerlesen", "index": 1, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "puan_012", "index": 1, "selector":"td:nth-child(4)", "type": "float"},
            {"name": "puan_012_006", "index": 1, "selector":"td:nth-child(5)", "type": "float"},
            {"name": "kont_turu", "index": 2, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "kontenjan", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "yerlesen", "index": 2, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "puan_012", "index": 2, "selector":"td:nth-child(4)", "type": "float"},
            {"name": "puan_012_006", "index": 2, "selector":"td:nth-child(5)", "type": "float"},    
        ],
        "sira_datas":[
            {"name": "kont_turu", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "kontenjan", "index": 1, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "yerlesen", "index": 1, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "sira_012", "index": 1, "selector":"td:nth-child(4)", "type": "int"},
            {"name": "sira_012_006", "index": 1, "selector":"td:nth-child(5)", "type": "int"},
            {"name": "kont_turu", "index": 2, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "kontenjan", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "yerlesen", "index": 2, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "sira_012", "index": 2, "selector":"td:nth-child(4)", "type": "int"},
            {"name": "sira_012_006", "index": 2, "selector":"td:nth-child(5)", "type": "int"},    
        ]
    },
    "son_profil": {
        "rows": "table > tbody > tr",
        "datas":[
            {"name": "ogrnm_durumu", "index": 1, "selector":"td:nth-child(2)", "type": "str"},
            {"name": "mezun_yil", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "lise_alan", "index": 3, "selector":"td:nth-child(2)", "type": "str"},
            {"name": "puan", "index": 4, "selector":"td:nth-child(2)", "type": "float"},
            {"name": "sira", "index": 5, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "katsayi", "index": 6, "selector":"td:nth-child(2)", "type": "str"},
            {"name": "obp", "index": 7, "selector":"td:nth-child(2)", "type": "float"},
            {"name": "dn", "index": 8, "selector":"td:nth-child(2)", "type": "float"},
            {"name": "cinsiyet", "index": 9, "selector":"td:nth-child(2)", "type": "str"},
            {"name": "il", "index": 10, "selector":"td:nth-child(2)", "type": "str"},
        ]
    },
    "yks_net": {
        "rows": "table > tbody > tr",
        "datas":[
            {"name": "ders", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "012", "index": 2, "selector":"td:nth-child(2)", "type": "float"},
            {"name": "012_006", "index": 3, "selector":"td:nth-child(3)", "type": "float"}
        ]
    },
    "yks_puan":{
        "ort_rows":"table > tbody > tr",
        "dusuk_rows":"div.panel-body > table > tbody > tr",
        "ort_datas":[
            {"name":"ort_yer_012", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ort_yer_012_006", "index":1, "selector":"td:nth-child(3)", "type":"int"},
            {"name":"ort_obp_012", "index":2, "selector":"td:nth-child(2)", "type":"float"},
            {"name":"ort_obp_012_006", "index":2, "selector":"td:nth-child(3)", "type":"float"},
            {"name":"ort_tyt_012", "index":3, "selector":"td:nth-child(2)", "type":"float"},
            {"name":"ort_tyt_012_006", "index":3, "selector":"td:nth-child(3)", "type":"float"},
        ],
        "dusuk_datas":[
            {"name":"dusuk_yer_012", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"dusuk_yer_012_006", "index":1, "selector":"td:nth-child(3)", "type":"int"},
            {"name":"dusuk_obp_012", "index":2, "selector":"td:nth-child(2)", "type":"float"},
            {"name":"dusuk_obp_012_006", "index":2, "selector":"td:nth-child(3)", "type":"float"},
            {"name":"dusuk_tyt_012", "index":3, "selector":"td:nth-child(2)", "type":"float"},
            {"name":"dusuk_tyt_012_006", "index":3, "selector":"td:nth-child(3)", "type":"float"},
        ]
    },
    "yks_sira": {
        "ort_rows":"table > tbody > tr",
        "dusuk_rows":"div.panel-body > table > tbody > tr",
        "ort_datas":[
            {"name":"ort_yer_012", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ort_yer_012_006", "index":1, "selector":"td:nth-child(3)", "type":"int"},
            {"name":"ort_tyt_012", "index":2, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ort_tyt_012_006", "index":2, "selector":"td:nth-child(3)", "type":"int"},
        ],
        "dusuk_datas":[
            {"name":"dusuk_yer_012", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"dusuk_yer_012_006", "index":1, "selector":"td:nth-child(3)", "type":"int"},
            {"name":"dusuk_tyt_012", "index":2, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"dusuk_tyt_012_006", "index":2, "selector":"td:nth-child(3)", "type":"int"},
        ]
    },
    "tercih_istatistik":{
        "table1_rows":"table:nth-child(1) > tbody > tr",
        "table3_rows":"table:nth-child(3) > tbody > tr",
        "table1_datas":[
            {"name":"toplam", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"aday", "index":2, "selector":"td:nth-child(2)", "type":"float"},
            {"name":"ort_tercih", "index":3, "selector":"td:nth-child(2)", "type":"float"},
            {"name":"ilk_bir", "index":4, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ilk_bir_orn", "index":4, "selector":"td:nth-child(3)", "type":"yuzde"},
            {"name":"ilk_uc", "index":5, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ilk_uc_orn", "index":5, "selector":"td:nth-child(3)", "type":"yuzde"},
            {"name":"ilk_dokuz", "index":6, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ilk_dokuz_orn", "index":6, "selector":"td:nth-child(3)", "type":"yuzde"}            
        ],
        "table1_datas_2022":[
            {"name":"toplam", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"aday", "index":2, "selector":"td:nth-child(2)", "type":"float"},
            {"name":"ort_tercih", "index":3, "selector":"td:nth-child(2)", "type":"float"},
            {"name":"ilk_bir", "index":4, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ilk_bir_orn", "index":4, "selector":"td:nth-child(3)", "type":"yuzde"},
            {"name":"ilk_uc", "index":5, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ilk_uc_orn", "index":5, "selector":"td:nth-child(3)", "type":"yuzde"},
            {"name":"ilk_dokuz", "index":6, "selector":"td:nth-child(3)", "type":"int"},         
            {"name":"ilk_dokuz_orn", "index":6, "selector":"td:nth-child(2)", "type":"yuzde"}
        ],
        "table3_datas":[
            {"name":"tercih_1", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"tercih_2", "index":2, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"tercih_3", "index":3, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"tercih_4", "index":4, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"tercih_5", "index":5, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"tercih_6", "index":6, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"tercih_7", "index":7, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"tercih_8", "index":8, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"tercih_9", "index":9, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"tercih_10_sonra", "index":10, "selector":"td:nth-child(2)", "type":"int"},
        ]
    },
    "ort_tercih":{
        "main_rows":"table.table.table-bordered > tbody > tr",
        "tbody1_rows":"table:nth-child(3) > tbody > tr > td:nth-child(1) > table > tbody > tr",
        "tbody2_rows":"table:nth-child(3) > tbody > tr > td:nth-child(2) > table > tbody > tr",
        "main_datas":[
            {"name":"toplam", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ilk_bir", "index":2, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ilk_bir_orn", "index":2, "selector":"td:nth-child(3)", "type":"yuzde"},
            {"name":"ilk_uc", "index":3, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ilk_uc_orn", "index":3, "selector":"td:nth-child(3)", "type":"yuzde"},
            {"name":"ilk_on", "index":4, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ilk_on_orn", "index":4, "selector":"td:nth-child(3)", "type":"yuzde"},          
            {"name":"ort_tercih", "index":5, "selector":"td:nth-child(2)", "type":"float"}            
        ],
        "tbody1_datas":[
            {"name":"tercih", "index":1, "selector":"td:nth-child(2)", "type":"int"},
        ],
        "tbody2_datas":[
            {"name":"tercih", "index":1, "selector":"td:nth-child(2)", "type":"int"},
        ]
    },
    "tercih_genel":{
        "rows":"table > tbody > tr",
        "datas":[
            {"name":"genel", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"t_tercih", "index":2, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"k_tercih", "index":3, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"bos_tercih", "index":4, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"ort_tercih", "index":5, "selector":"td:nth-child(2)", "type":"int"},
        ]
    },
    "tercih_uni_tur":{
        "rows":"table > tbody > tr",
        "datas":[
            {"name":"devlet", "index":1, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"vakif", "index":2, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"kibris", "index":3, "selector":"td:nth-child(2)", "type":"int"},
            {"name":"yabanci", "index":4, "selector":"td:nth-child(2)", "type":"int"},
        ]
    },
    "tercih_uni":{
        "tablo_rows": "table.table-bordered",
        "baslik": "thead > tr:nth-child(1) > th",
        "tr_rows": "tbody > tr",
        "datas":[
            {"name": "isim", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"}
        ]
    },
    "tercih_il":{
        "rows": "tbody > tr",
        "datas":[
            {"name": "isim", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"}
        ]
    },
    "tercih_fark":{
        "datas":[
            {"name": "ayni", "index": 1, "selector":"tbody > tr:nth-child(1) > td:nth-child(2)", "type": "int"},
            {"name": "farkli", "index": 1, "selector":"tbody > tr:nth-child(2) > td:nth-child(2)", "type": "int"},
            {"name": "kibris", "index": 1, "selector":"tbody > tr:nth-child(3) > td:nth-child(2)", "type": "int"},
            {"name": "onlisans", "index": 1, "selector":"tbody > tr:nth-child(4) > td:nth-child(2)", "type": "int"},
            {"name": "yabanci", "index": 1, "selector":"tbody > tr:nth-child(5) > td:nth-child(2)", "type": "int"}
        ],
        "datas_2024":[
            {"name": "ayni", "index": 1, "selector":"tbody > tr:nth-child(1) > td:nth-child(2)", "type": "int"},
            {"name": "farkli", "index": 1, "selector":"tbody > tr:nth-child(2) > td:nth-child(2)", "type": "int"},
            {"name": "kibris", "index": 1, "selector":"tbody > tr:nth-child(4) > td:nth-child(2)", "type": "int"},
            {"name": "onlisans", "index": 1, "selector":"tbody > tr:nth-child(3) > td:nth-child(2)", "type": "int"},
            {"name": "yabanci", "index": 1, "selector":"tbody > tr:nth-child(5) > td:nth-child(2)", "type": "int"}
        ]
    },
    "tercih_program":{
        "rows": "tbody > tr",
        "datas": [
            {"name": "isim", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"}
        
        ]
    },
    "yerlesme_kosul":{
        "rows": "table > tbody > tr",
        "datas": [
            {"name": "no", "index": 1, "selector":"td:nth-child(1)", "type": "int"},
            {"name": "aciklama", "index": 2, "selector":"td:nth-child(2)", "type": "str"}
        ]
    },
    "ogretim_uyesi":{
        "datas": [
            {"name": "prof", "index": 1, "selector":"table > tbody > tr:nth-child(1) > td:nth-child(2)", "type": "int"},
            {"name": "docent", "index": 2, "selector":"table > tbody > tr:nth-child(2) > td:nth-child(2)", "type": "int"},
            {"name": "dou", "index": 3, "selector":"table > tbody > tr:nth-child(3) > td:nth-child(2)", "type": "int"},
            {"name": "toplam", "index": 4, "selector":"table > tbody > tr:nth-child(4) > td:nth-child(2)", "type": "int"}
        ]
    },
    "kayitli_ogr":{
        "rows":"table > tbody > tr",
        "datas":[
            {"name": "text", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "sayi", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "orn", "index": 3, "selector":"td:nth-child(3)", "type": "yuzde"},
        ],
    },
    "mezun_ogr":{
        "rows":"table > tbody > tr",
        "mezun_control": "div:nth-child(1) > h4",
        "datas":[
            {"name": "yil", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "toplam", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "kiz", "index": 3, "selector":"td:nth-child(3)", "type": "int"},
            {"name": "erkek", "index": 4, "selector":"td:nth-child(4)", "type": "int"},
        ],
    },
    "degisim_ogr":{
        "rows":"table > tbody > tr",
        "control":"div:nth-child(1) > h4",
        "datas":[
            {"name": "program", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "giden", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "gelen", "index": 3, "selector":"td:nth-child(3)", "type": "int"},
        ],
    },
    "yatay_gecis":{
        "gelen_rows":"table:nth-child(1) > tbody > tr",
        "giden_rows":"table:nth-child(3) > tbody > tr",
        "datas":[
            {"name": "madde", "index": 1, "selector":"td:nth-child(1)", "type": "str"},
            {"name": "onceki", "index": 2, "selector":"td:nth-child(2)", "type": "int"},
            {"name": "simdiki", "index": 3, "selector":"td:nth-child(3)", "type": "int"},
        ],
        "2324_gelen_onceki":"table:nth-child(1) > tbody > tr > td:nth-child(1)",
        "2324_gelen_simdiki":"table:nth-child(1) > tbody > tr > td:nth-child(2)",
        "2324_giden_onceki":"table:nth-child(3) > tbody > tr > td:nth-child(1)",
        "2324_giden_simdiki":"table:nth-child(3) > tbody > tr > td:nth-child(2)",
        "gelen_kontrol":"div:nth-child(1) > h4",
        "giden_kontrol":"div:nth-child(3) > h4"
    },
    "net_sihirbazi":{
        "rows":"table#mydata > tbody > tr",
        "headers":"table#mydata > thead > tr > th",
        "datas":[
            {"name": "uni", "selector":"td:nth-child(2) > small > a", "type": "str"},
            {"name": "osym_kod", "selector":"td:nth-child(2) > small > a", "type": "href"},
            {"name": "year", "selector":"td:nth-child(3)", "type": "int"},
            {"name": "katsayi", "selector":"td:nth-child(5)", "type": "float"},
            {"name": "obp", "selector":"td:nth-child(6)", "type": "float"},
            {"name": "puan", "selector":"td:nth-child(7)", "type": "float"},
            {"name": "bolum_yerlesen", "selector":"td:nth-child(8)", "type": "int"},
        ],
        "ders_baslangic_index": 9
    }

}
