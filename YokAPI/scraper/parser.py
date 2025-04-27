from YokAPI.scraper.selectors import selectors
from YokAPI.models import *
from bs4 import BeautifulSoup
import asyncio


class Parser():
    def __init__(self, html: str):
        self.html = html
        self.bs = BeautifulSoup(html, "html.parser")

    async def async_select_one(
            self,
            bs       : BeautifulSoup | str,
            selector : str,
            int_     : bool = False,
            float_   : bool = False,
            yuzde    : bool = False,
            ek_yer   : bool = False
    ) -> int | float | str | None:

        r_ = bs.select_one(selector).text.strip()

        if int_:
            if r_ in ["---", "", "--"]:
                r_ = None
            elif r_ == " ":
                r_ = None
            elif r_ == "Dolmadı":
                r_ = None
            elif "." in r_:
                r_ = int(r_.replace(".", ""))
            else:
                r_ = int(r_)

        elif float_:
            if r_ in ["---", ""]:
                r_ = None
            elif r_ == "Dolmadı":
                r_ = None
            else:
                r_ = float(r_.replace(",", "."))

        elif yuzde:
            if r_ in ["---", ""]:
                r_ = None
            elif r_ == "Dolmadı":
                r_ = None
            elif r_ == "%":
                r_ = None
            else:
                r_ = float((r_.replace("%", "")).replace(",", "."))

        elif ek_yer:
            if "olmamıştır" in r_:
                r_ = 0
            elif "---" in r_:
                r_ = None
            elif r_ == " ":
                r_ = None
            else:
                r_ = r_.split(" ile ")[-1][0:1]
                if r_ == " ": r_ = None
                else: r_ = int(r_)

        return r_

    def format_text(
            self,
            text: str,
            int_     : bool = False,
            float_   : bool = False,
            yuzde    : bool = False,
    ) -> str:
        
        r_ = text.strip()

        if int_:
            if r_ in ["---", "", "--"]:
                r_ = None
            elif r_ == " ":
                r_ = None
            elif r_ == "Dolmadı":
                pass
            elif "." in r_:
                r_ = int(r_.replace(".", ""))
            else:
                r_ = int(r_)

        elif float_:
            if r_ in ["---", ""]:
                r_ = None
            elif r_ == "Dolmadı":
                pass
            else:
                r_ = float(r_.replace(",", "."))

        elif yuzde:
            if r_ in ["---", ""]:
                r_ = None
            elif r_ == "Dolmadı":
                pass
            elif r_ == "%":
                r_ = None
            else:
                r_ = float((r_.replace("%", "")).replace(",", "."))

        return r_

    async def genel_blg_parser(self, osym_kod: int, year: int) -> GenelBilgiler:
        selectors_genel_blg = selectors["genel_blg"]
        
        async def parse_table(table: dict) -> dict:
            base_selector = f"table:nth-child({table['index']})"
            rows = self.bs.select(f"{base_selector} > {table['rows']}")

            row_data = {}
            for i in range(len(rows)):
                table_data = table["datas"]
                row_data[table_data[i]["name"]] = await self.async_select_one(
                    rows[i],
                    selector="tr > td.text-center.vert-align",
                    int_=table_data[i]["type"] == "int",
                    float_=table_data[i]["type"] == "float",
                    yuzde=table_data[i]["type"] == "yuzde",
                    ek_yer=False
                )

            return row_data

    
        tasks = [
            self.async_select_one(self.bs, selectors_genel_blg["table1"]["bolum"]),
            parse_table(selectors_genel_blg["table1"]),
            parse_table(selectors_genel_blg["table2"]),
            parse_table(selectors_genel_blg["table3"])
        ]

        results = {"osym_kod": osym_kod, "year": year}
        for table_result in await asyncio.gather(*tasks):
            results.update({"bolum_ismi": table_result} if isinstance(table_result, str) else table_result)

        return GenelBilgiler(**results)
    
    async def genel_blg_onlisans_parser(self, osym_kod: int, year: int) -> GenelBilgilerOnlisans:
        selectors_genel_blg = selectors["genel_blg_onlisans"]
        
        async def parse_table(table: dict) -> dict:
            base_selector = f"table:nth-child({table['index']})"
            rows = self.bs.select(f"{base_selector} > {table['rows']}")


            row_data = {}
            for i in range(len(rows)):
                table_data = table["datas"]
                row_data[table_data[i]["name"]] = await self.async_select_one(
                    rows[i],
                    selector="tr > td.text-center.vert-align",
                    int_=table_data[i]["type"] == "int",
                    float_=table_data[i]["type"] == "float",
                    yuzde=table_data[i]["type"] == "yuzde",
                    ek_yer=False
                )

            return row_data

    
        tasks = [
            self.async_select_one(self.bs, selectors_genel_blg["table1"]["bolum"]),
            parse_table(selectors_genel_blg["table1"]),
            parse_table(selectors_genel_blg["table2"]),
            parse_table(selectors_genel_blg["table3"]),
            parse_table(selectors_genel_blg["table4"]) if year != 2024 else parse_table(selectors_genel_blg["table4_2024"]),
        ]

        results = {"osym_kod": osym_kod, "year": year}
        for table_result in await asyncio.gather(*tasks):
            results.update({"bolum_ismi": table_result} if isinstance(table_result, str) else table_result)

        return GenelBilgilerOnlisans(**results)
    

    async def kontenjan_parser(self, osym_kod: int, year: int) -> Kontenjan:
        selectors_kont = selectors["kontenjan"]
        base_selector = f"table > {selectors_kont['rows']}"
        rows = self.bs.select(base_selector)

        tasks = [
            self.async_select_one(
                rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=data["type"] == "yuzde",
                ek_yer=False
            ) for data in selectors_kont["datas"]
        ]
        tasks.append(
            self.async_select_one(
                self.bs,
                selector=selectors_kont["ek_yer"]["selector"],
                int_=False,
                float_=False,
                yuzde=False,
                ek_yer=True
            )
        )
        model_keys = [
            "kont_gte", "genel_kont", "yer_oran", "kesn_kayt",
            "kayt_yptrmyn", "tubitak", "engelli", "okl_bir_kont",
            "okl_bir_yer", "t_kont", "t_yer", "ek_yer", "osym_kod", "year"
        ]

        results = await asyncio.gather(*tasks)
        results.append(osym_kod)
        results.append(year)
        results = dict(zip(model_keys, results))
        return Kontenjan(**results)
    

    async def kontenjan_onlisans_parser(self, osym_kod: int, year: int) -> Kontenjan:
        selectors_kont = selectors["kontenjan_onlisans"]
        base_selector = f"table > {selectors_kont['rows']}"
        rows = self.bs.select(base_selector)
        
        def edit_tr(tr: BeautifulSoup) -> BeautifulSoup:
            tr = tr.replace("<tr>", "").replace("</tr>", "")
            return BeautifulSoup(tr, "html.parser")

        tasks = [
            self.async_select_one(
                rows[data["index"] - 1] if data["index"] != 4 else edit_tr(str(rows[3])),
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=data["type"] == "yuzde",
                ek_yer=False
            ) for data in selectors_kont["datas"]
        ]
        tasks.append(
            self.async_select_one(
                self.bs,
                selector=selectors_kont["ek_yer"]["selector"],
                int_=False,
                float_=False,
                yuzde=False,
                ek_yer=True
            )
        )
        model_keys = [
            "kont_gte", "genel_kont", "yer_oran", "kesn_kayt",
            "kayt_yptrmyn", "tubitak", "engelli", "okl_bir_kont",
            "okl_bir_yer", "t_kont", "t_yer", "ek_yer", "osym_kod", "year"
        ]

        results = await asyncio.gather(*tasks)
        results.append(osym_kod)
        results.append(year)
        results = dict(zip(model_keys, results))
        return Kontenjan(**results)

    async def cinsiyet_parser(self, osym_kod: int, year: int) -> Cinsiyet:
        selectors_cins = selectors["cinsiyet"]
        base_selector = f"table > {selectors_cins['rows']}"
        rows = self.bs.select(base_selector)

        tasks = [
            self.async_select_one(
                rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=False,
                yuzde=data["type"] == "yuzde",
                ek_yer=False
            ) for data in selectors_cins["datas"]
        ]
        results = await asyncio.gather(*tasks)

        return Cinsiyet(
            osym_kod=osym_kod,
            year=year,
            erkek={"sayi": results[2], "orn": results[3]},
            kadin={"sayi": results[0], "orn": results[1]}
        )

    async def cograf_bolg_parser(self, osym_kod: int, year: int) -> CografiBolgeler:
        selectors_cograf = selectors["cograf_bolg"]
        sehir_rows = self.bs.select(selectors_cograf['sehir_rows'])
        bolge_rows = self.bs.select(selectors_cograf['bolge_rows'])

        sehir_json = selectors_cograf["sehr_json"]
        bolge_json = selectors_cograf["bolge_json"]

        for sehir_row in sehir_rows:
            tasks = [
                self.async_select_one(
                    sehir_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=data["type"] == "yuzde",
                    ek_yer=False
                ) for data in selectors_cograf["sehir_datas"]
            ]

            sehir_results = await asyncio.gather(*tasks)
            cins_rep = sehir_results[-1].split("/")

            erkek = cins_rep[0].strip().replace("Erkek", " ").strip()
            kadin = cins_rep[1].strip().replace("Kız", " ").strip()

            sehir_json[sehir_results[0]] = {
                "sayi": sehir_results[1],
                "orn": sehir_results[2],
                "erkek": self.format_text(erkek, int_=True),
                "kadin": self.format_text(kadin, int_=True)
            }

        for bolge_row in bolge_rows:
            tasks = [
                self.async_select_one(
                    bolge_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=data["type"] == "yuzde",
                    ek_yer=False
                ) for data in selectors_cograf["bolge_datas"]
            ]

            bolge_results = await asyncio.gather(*tasks)
            bolge_json[bolge_results[0]] = {
                "sayi": bolge_results[1],
                "orn": bolge_results[2]
            }

        return CografiBolgeler(
            osym_kod=osym_kod,
            year=year,
            bolge=Bolgeler(
                toplam=bolge_json["Toplam"],
                akdeniz=bolge_json["Akdeniz"],
                dogu_anadolu=bolge_json["Doğu Anadolu"],
                ege=bolge_json["Ege"],
                guneydogu_anadolu=bolge_json["Güneydoğu Anadolu"],
                ic_anadolu=bolge_json["İç Anadolu"],
                karadeniz=bolge_json["Karadeniz"],
                marmara=bolge_json["Marmara"],
                belli_degil=bolge_json["Belli Değil"]
            ),
            sehir=SehirDurum(
                toplam=sehir_json["Toplam"],
                ayni=sehir_json["Aynı Şehir"],
                farkli=sehir_json["Farklı Şehir"],
                belli_degil=sehir_json["Belli Değil"]
            )
        )

    async def iller_parser(self, osym_kod: int, year: int) -> Iller:
        selectors_iller = selectors["iller"]
        rows = self.bs.select(selectors_iller["rows"])

        sehirler = []

        async def get_sehir(sehir_row):
            tasks = [
                self.async_select_one(
                    sehir_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=data["type"] == "yuzde",
                    ek_yer=False
                ) for data in selectors_iller["datas"]
            ]

            sehir_results = await asyncio.gather(*tasks)
            return sehir_results

        tasks = [get_sehir(sehir_row) for sehir_row in rows]
        sehirler = await asyncio.gather(*tasks)
        model_keys = ["isim", "sayi", "orn"]
        sehirler = [dict(zip(model_keys, sehir)) for sehir in sehirler]

        return Iller(
            osym_kod=osym_kod,
            year=year,
            sehirler=sehirler
        )
    
    async def ogr_durum_parser(self, osym_kod: int, year: int) -> OgrenimDurumu:
        selectors_ogr_durum = selectors["ogr_durum"]
        rows = self.bs.select(selectors_ogr_durum["rows"])
        if rows == []:
            return OgrenimDurumu(
                osym_kod=osym_kod,
                year=year,
                toplam={"sayi":None, "orn":None},
                lise_yeni={"sayi":None, "orn":None},
                lise_mezun={"sayi":None, "orn":None},
                uni_ogr={"sayi":None, "orn":None},
                uni_mezun={"sayi":None, "orn":None},
                diger={"sayi":None, "orn":None}
            )

        try: 
            tasks = [
                self.async_select_one(
                    rows[data["index"] - 1],
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=data["type"] == "yuzde",
                    ek_yer=False
                ) for data in selectors_ogr_durum["datas"]
            ]

        except IndexError: 
            return OgrenimDurumu(
                osym_kod=osym_kod,
                year=year,
                toplam={"sayi":None, "orn":None},
                lise_yeni={"sayi":None, "orn":None},
                lise_mezun={"sayi":None, "orn":None},
                uni_ogr={"sayi":None, "orn":None},
                uni_mezun={"sayi":None, "orn":None},
                diger={"sayi":None, "orn":None}
            ) 


        results = await asyncio.gather(*tasks)
        
        return OgrenimDurumu(
            osym_kod=osym_kod,
            year=year,
            toplam={"sayi":results[0], "orn":results[1]},
            lise_yeni={"sayi":results[2], "orn":results[3]},
            lise_mezun={"sayi":results[4], "orn":results[5]},
            uni_ogr={"sayi":results[6], "orn":results[7]},
            uni_mezun={"sayi":results[8], "orn":results[9]},
            diger={"sayi":results[10], "orn":results[11]}
        )
    
    async def mezun_yil_parser(self, osym_kod: int, year: int) -> MezunYil:
        selectors_mezun_yil = selectors["mezun_yil"]
        rows = self.bs.select(selectors_mezun_yil["rows"])
        
        yillar = []
        
        async def get_yil(yil_row):
            tasks = [
                self.async_select_one(
                    yil_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=data["type"] == "yuzde",
                    ek_yer=False
                ) for data in selectors_mezun_yil["datas"]
            ]
            
            yil_results = await asyncio.gather(*tasks)
            return yil_results
        
        tasks = [get_yil(yil_row) for yil_row in rows]
        yillar = await asyncio.gather(*tasks)
        model_keys = ["yil", "sayi", "orn"]
        yillar = [dict(zip(model_keys, yil)) for yil in yillar]

        return MezunYil(
            osym_kod=osym_kod,
            year=year,
            yillar=yillar
        )
    
    async def lise_alan_parser(self, osym_kod: int, year: int) -> LiseAlan:
        selectors_lise_alan = selectors["lise_alan"]
        rows = self.bs.select(selectors_lise_alan["rows"])
        
        alanlar = []
        
        async def get_alan(alan_row):

            tasks = [
                self.async_select_one(
                    alan_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=data["type"] == "yuzde",
                    ek_yer=False
                ) for data in selectors_lise_alan["datas"]
            ]
            
            alan_results = await asyncio.gather(*tasks)
            return alan_results
        
        tasks = [get_alan(alan_row) for alan_row in rows]
        alanlar = await asyncio.gather(*tasks)
        model_keys = ["alan", "sayi", "orn"]
        alanlar = [dict(zip(model_keys, alan)) for alan in alanlar]

        return LiseAlan(
            osym_kod=osym_kod,
            year=year,
            alanlar=alanlar
        )
    

    async def lise_grup_tip_parser(self, osym_kod: int, year: int) -> LiseTip:

        selectors_lise_grup_tip = selectors["lise_grup_tip"]
        genel_lise_rows = self.bs.select(
            selectors_lise_grup_tip["genel_lise_2019_rows"] if year == 2019 else selectors_lise_grup_tip["genel_lise_rows"]
        )
        meslek_lise_rows = self.bs.select(
            selectors_lise_grup_tip["meslek_lise_2019_rows"] if year == 2019 else selectors_lise_grup_tip["meslek_lise_rows"]
        )
        
        genel_lise = []
        meslek_lise = []

        async def get_lise(lise_row):
            tasks = [
                self.async_select_one(
                    lise_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=data["type"] == "yuzde",
                    ek_yer=False
                ) for data in selectors_lise_grup_tip["datas"]
            ]

            lise_results = await asyncio.gather(*tasks)
            return lise_results

        tasks = [get_lise(genel_lise_row) for genel_lise_row in genel_lise_rows]
        genel_lise = await asyncio.gather(*tasks)
        model_keys = ["alan", "sayi", "orn"]
        genel_lise = [dict(zip(model_keys, lise)) for lise in genel_lise]

        tasks = [get_lise(meslek_lise_row) for meslek_lise_row in meslek_lise_rows]
        meslek_lise = await asyncio.gather(*tasks)
        meslek_lise = [dict(zip(model_keys, lise)) for lise in meslek_lise]

        return LiseTip(
            osym_kod=osym_kod,
            year=year,
            genel_lise=genel_lise,
            meslek_lise=meslek_lise
        )
    
    async def liseler_parser(self, osym_kod: int, year: int) -> Liseler:
        selectors_liseler = selectors["liseler"]
        rows = self.bs.select(selectors_liseler["rows"])
        
        liseler = []
        
        async def get_lise(lise_row):
            tasks = [
                self.async_select_one(
                    lise_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=False,
                    ek_yer=False
                ) for data in selectors_liseler["datas"]
            ]
            
            lise_results = await asyncio.gather(*tasks)
            return lise_results
        
        tasks = [get_lise(lise_row) for lise_row in rows]
        liseler = await asyncio.gather(*tasks)
        model_keys = ["isim", "toplam", "eski_mezun", "yeni_mezun"]
        liseler = [dict(zip(model_keys, lise)) for lise in liseler]

        return Liseler(
            osym_kod=osym_kod,
            year=year,
            liseler=liseler
        )
        
    async def okul_birinci_parser(self, osym_kod: int, year: int) -> OkulBirinciKontenjan:
        selectors_okul_birinci = selectors["okul_birinci"]
        tbody1_rows = self.bs.select(selectors_okul_birinci["tbody1_rows"])
        tbody2_rows = self.bs.select(selectors_okul_birinci["tbody2_rows"])

        kont_json = {
            "toplam":None,
            "genel":None,
            "okul_bir":None,
            "sehit_gazi":None,
            "depremzede":None,
            "kadin_34yas":None
        }

        liseler = []

        async def get_kont(kont_row):
            tasks = [
                self.async_select_one(
                    kont_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=False,
                    ek_yer=False
                )  for data in selectors_okul_birinci["tbody1_datas"]
            ]

            kont_results = await asyncio.gather(*tasks)
            return kont_results
        
        for kont_row in tbody1_rows:
            kont_turu = await self.async_select_one(
                kont_row,
                selector="td:nth-child(1)",
                    int_=False,
                    float_=False,
                    yuzde=False,
                    ek_yer=False
                )
            kont_sayi = await self.async_select_one(
                kont_row,
                selector="td:nth-child(2)",
                    int_=True,
                    float_=False,
                    yuzde=False,
                    ek_yer=False
                )

            if "Toplam" == kont_turu: kont_json["toplam"] = kont_sayi
            elif "Genel" == kont_turu: kont_json["genel"] = kont_sayi
            elif "Okul Birincisi" == kont_turu: kont_json["okul_bir"] = kont_sayi
            elif "Şehit-Gazi" == kont_turu: kont_json["sehit_gazi"] == kont_turu
            elif "Depremzede" == kont_turu: kont_json["depremzede"] = kont_sayi
            elif "Otuz Dört Yaş Üstü Kadın" == kont_turu: kont_json["kadin_34yas"] = kont_sayi

        async def get_lise(lise_row):
            tasks = [
                self.async_select_one(
                    lise_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=False,
                    ek_yer=False
                ) for data in selectors_okul_birinci["tbody2_datas"]
            ]

            lise_results = await asyncio.gather(*tasks)
            return lise_results
        


        tasks = [get_lise(lise_row) for lise_row in tbody2_rows]
        liseler = await asyncio.gather(*tasks)
        model_keys = ["kont_turu", "isim"]
        liseler = [dict(zip(model_keys, lise)) for lise in liseler]

        return OkulBirinciKontenjan(
            osym_kod=osym_kod,
            year=year,
            toplam=kont_json["toplam"],
            genel=kont_json["genel"],
            okul_bir=kont_json["okul_bir"],
            sehit_gazi=kont_json["sehit_gazi"],
            depremzede=kont_json["depremzede"],
            kadin_34yas=kont_json["kadin_34yas"],
            liseler=liseler
        )

    async def taban_puan_parser(self, osym_kod: int, year: int) -> TabanPuan:
        selectors_taban_puan = selectors["taban_puan"]
        puan_rows = self.bs.select(selectors_taban_puan["puan_rows"])
        sira_rows = self.bs.select(selectors_taban_puan["sira_rows"])

        tasks = [
            self.async_select_one(
                puan_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=False,
                ek_yer=False
            ) for data in selectors_taban_puan["puan_datas"]
        ]

        puan_results = await asyncio.gather(*tasks)
        model_keys_puan = ["kont_turu", "kont", "yerlesen", "puan"]
        puan_results_dict = [dict(zip(model_keys_puan, puan_results[0:4]))]
        puan_results_dict.append(dict(zip(model_keys_puan, puan_results[4:8])))

        tasks = [
            self.async_select_one(
                sira_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for data in selectors_taban_puan["sira_datas"]
        ]

        sira_results = await asyncio.gather(*tasks)
        model_keys_sira = ["kont_turu", "kont", "yerlesen", "sira_012", "sira_012_006"]
        sira_results_dict = [dict(zip(model_keys_sira, sira_results[0:5]))]
        sira_results_dict.append(dict(zip(model_keys_sira, sira_results[5:10])))

        return TabanPuan(
            osym_kod=osym_kod,
            year=year,
            puanlar=puan_results_dict,
            siralar=sira_results_dict
        )
    
    async def taban_puan_onlisans_parser(self, osym_kod: int, year: int) -> TabanPuan:
        tbody1 = self.bs.select_one("table:nth-child(1) > tbody")
        tds_fail = tbody1.find_all(lambda tag: tag.name == 'td' and tag.find_parent('tr') is None)
        # <td> taglarının etrafında tr yok
        
        new_tr = self.bs.new_tag("tr")
        for td in tds_fail:
            new_tr.append(td)
        tbody1.insert(0, new_tr)

        selectors_taban_puan = selectors["taban_puan_onlisans"]
        
        puan_rows = tbody1.select(selectors_taban_puan["puan_rows"])
        sira_rows = self.bs.select(selectors_taban_puan["sira_rows"])

        tasks = [
            self.async_select_one(
                puan_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=False,
                ek_yer=False
            ) for data in selectors_taban_puan["puan_datas"]
        ]

        puan_results = await asyncio.gather(*tasks)
        model_keys_puan = ["kont_turu", "kont", "yerlesen", "puan_012", "puan_012_006"]
        puan_results_dict = [dict(zip(model_keys_puan, puan_results[0:5]))]
        puan_results_dict.append(dict(zip(model_keys_puan, puan_results[5:10])))

        if year == 2019:
            sira_datas = selectors_taban_puan["sira_datas_2019"]
        else:
            sira_datas = selectors_taban_puan["sira_datas"]
        
        tasks = [
            self.async_select_one(
                sira_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for data in sira_datas
        ]

        sira_results = await asyncio.gather(*tasks)
        if year == 2019: sira_results.append(None)
        model_keys_sira = ["kont_turu", "kont", "yerlesen", "sira_012", "sira_012_006"]
        sira_results_dict = [dict(zip(model_keys_sira, sira_results[0:5]))]
        if year != 2019: sira_results_dict.append(dict(zip(model_keys_sira, sira_results[5:10])))

        return TabanPuanOnlisans(
            osym_kod=osym_kod,
            year=year,
            puanlar=puan_results_dict,
            siralar=sira_results_dict
        )
    
    async def son_profil_parser(self, osym_kod: int, year: int) -> SonProfil:
        selectors_son_profil = selectors["son_profil"]
        rows = self.bs.select(selectors_son_profil["rows"])
        
        tasks = [
            self.async_select_one(
                rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=False,
                ek_yer=False
            ) for data in selectors_son_profil["datas"]
        ]

        results = await asyncio.gather(*tasks)

        return SonProfil(
            osym_kod=osym_kod,
            year=year,
            ogrnm_durumu=results[0],
            mezun_yil=results[1],
            lise_alan=results[2],
            puan=results[3],
            sira=results[4],
            katsayi=float(results[5].split(" ")[0].replace(",", ".")) if results[5] else None,
            obp=results[6],
            dn=results[7],
            cinsiyet=results[8],
            il=results[9]
        )
    
    async def yks_net_parser(self, osym_kod: int, year: int) -> YksNet:
        selectors_yks_net = selectors["yks_net"]
        rows = self.bs.select(selectors_yks_net["rows"])
        if rows == []:
            return YksNet(
                osym_kod=osym_kod,
                year=year,
                ort_obp_012=None,
                ort_obp_012_006=None,
                yerlesen_012=None,
                yerlesen_012_006=None,
                dersler=None
            )
        
        async def get_net(net_row):
            tasks = [
                self.async_select_one(
                    net_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=data["type"] == "float",
                    yuzde=False,
                    ek_yer=False
                ) for data in selectors_yks_net["datas"]
            ]
            
            net_results = await asyncio.gather(*tasks)
            return net_results
        
        tasks = [get_net(net_row) for net_row in rows]
        yks_net = await asyncio.gather(*tasks)
        model_keys = ["ders", "net_012", "net_012_006"]
        yks_net_dict = [dict(zip(model_keys, net)) for net in yks_net[2:]]

        if year == 2024 or 2023:
            ort_obp_012 = yks_net[0][1]
            ort_obp_012_006 = yks_net[0][2]
            yerlesen_012 = yks_net[1][1]
            yerlesen_012_006 = yks_net[1][2]
        else:
            ort_obp_012 = yks_net[1][1]
            ort_obp_012_006 = yks_net[1][2]
            yerlesen_012 = yks_net[0][1]
            yerlesen_012_006 = yks_net[0][2]
            

        return YksNet(
            osym_kod=osym_kod,
            year=year,
            ort_obp_012=ort_obp_012,
            ort_obp_012_006=ort_obp_012_006,
            yerlesen_012=yerlesen_012,
            yerlesen_012_006=yerlesen_012_006,
            dersler=yks_net_dict
        )        
    
    async def yks_puan_parser(self, osym_kod: int, year: int) -> YksPuan:
        selectors_yks_puan = selectors["yks_puan"]
        ort_rows = self.bs.select(selectors_yks_puan["ort_rows"])
        dusuk_rows = self.bs.select(selectors_yks_puan["dusuk_rows"])

        if ort_rows == [] and dusuk_rows == []:
            return YksPuan(
                osym_kod=osym_kod,
                year=year,
                ort_puan=None,
                dusuk_puan=None
            )

        ort_tasks = [
            self.async_select_one(
                ort_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=False,
                ek_yer=False
            ) for data in selectors_yks_puan["ort_datas"]
        ]

        dusuk_tasks = [
            self.async_select_one(
                dusuk_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=False,
                ek_yer=False
            ) for data in selectors_yks_puan["dusuk_datas"]
        ]
        try: ort_puan = await asyncio.gather(*ort_tasks)
        except AttributeError as e: ort_puan = [None, None, None, None, None, None] 
        
        try: dusuk_puan = await asyncio.gather(*dusuk_tasks)
        except AttributeError as e: dusuk_puan = [None, None, None, None, None, None]

        model_keys = ["yer_012", "yer_012_006", "obp_012", "obp_012_006", "tyt_012", "tyt_012_006"]
        ort_puan_dict = [dict(zip(model_keys, ort_puan))]
        dusuk_puan_dict = [dict(zip(model_keys, dusuk_puan))]

        return YksPuan(
            osym_kod=osym_kod,
            year=year,
            ort_puan=ort_puan_dict,
            dusuk_puan=dusuk_puan_dict
        )
    
    async def yks_sira_parser(self, osym_kod: int, year: int) -> YksSira:
        selectors_yks_sira = selectors["yks_sira"]
        ort_rows = self.bs.select(selectors_yks_sira["ort_rows"])
        dusuk_rows = self.bs.select(selectors_yks_sira["dusuk_rows"])

        if dusuk_rows == [] and ort_rows == []:
            return YksSira(
                osym_kod=osym_kod,
                year=year,
                ort_sira=None,
                dusuk_sira=None
            )

        ort_tasks = [
            self.async_select_one(
                ort_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for data in selectors_yks_sira["ort_datas"]
        ]

        dusuk_tasks = [
            self.async_select_one(
                dusuk_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=False,
                ek_yer=False
            ) for data in selectors_yks_sira["dusuk_datas"]
        ]

        try: ort_sira = await asyncio.gather(*ort_tasks)
        except AttributeError as e: ort_sira = [None, None, None, None, None, None]
        try: dusuk_sira = await asyncio.gather(*dusuk_tasks)
        except AttributeError as e: dusuk_sira = [None, None, None, None, None, None]

        model_keys = ["yer_012", "yer_012_006", "tyt_012", "tyt_012_006"]
        ort_sira_dict = [dict(zip(model_keys, ort_sira))]
        dusuk_sira_dict = [dict(zip(model_keys, dusuk_sira))]

        return YksSira(
            osym_kod=osym_kod,
            year=year,
            ort_sira=ort_sira_dict,
            dusuk_sira=dusuk_sira_dict
        )
    
    async def tercih_istatistik_parser(self, osym_kod: int, year: int) -> TercihIstatistik:
        selectors_tercih_istatistik = selectors["tercih_istatistik"]
        table1_rows = self.bs.select(selectors_tercih_istatistik["table1_rows"])
        table3_rows = self.bs.select(selectors_tercih_istatistik["table3_rows"])
        table1_datas = selectors_tercih_istatistik["table1_datas"]
        if year == 2022: table1_datas = selectors_tercih_istatistik["table1_datas_2022"]

        tercih_list = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ]

        if len(table3_rows) != 10:
            for table3_row in table3_rows:
                sira_ = await self.async_select_one(table3_row, "td:nth-child(1)")
                tercih_ = await self.async_select_one(table3_row, "td:nth-child(2)")
                if sira_ == "10 ve Sonrası":
                    sira_ = 10
                tercih_list[int(sira_) - 1] = tercih_

    
        else:
            table3_tasks = [
                self.async_select_one(
                    table3_rows[data["index"] - 1],
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=False,
                    ek_yer=False
                ) for data in selectors_tercih_istatistik["table3_datas"]
            ]

            tercih_list = await asyncio.gather(*table3_tasks)

        table1_tasks = [
            self.async_select_one(
                table1_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=data["type"] == "yuzde",
                ek_yer=False
            ) for data in table1_datas
        ]   

        table1_results = await asyncio.gather(*table1_tasks)
        model_keys = [
            "osym_kod", "year", "toplam", "aday", "ort_tercih",
            "ilk_bir", "ilk_bir_orn", "ilk_uc", "ilk_uc_orn", "ilk_dokuz", "ilk_dokuz_orn", "tercihler"
        ]
        model_tercih = ["tercih_1", "tercih_2", "tercih_3", "tercih_4", "tercih_5", "tercih_6", "tercih_7", "tercih_8", "tercih_9", "tercih_10_sonra"]
        tercih_dict = dict(zip(model_tercih, tercih_list))


        results_list = [osym_kod, year]
        results_list.extend(table1_results)
        results_list.append(tercih_dict)
        results = dict(zip(model_keys, results_list))

        return TercihIstatistik(**results)


    async def ort_tercih_parser(self, osym_kod: int, year: int) -> OrtTercih:
        selectors_ort_tercih = selectors["ort_tercih"]
        main_rows = self.bs.select(selectors_ort_tercih["main_rows"])
        tbody1_rows = self.bs.select(selectors_ort_tercih["tbody1_rows"])
        tbody2_rows = self.bs.select(selectors_ort_tercih["tbody2_rows"])

        main_tasks = [
            self.async_select_one(
                main_rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=data["type"] == "float",
                yuzde=data["type"] == "yuzde",
                ek_yer=False
            ) for data in selectors_ort_tercih["main_datas"]
        ]
        
        tbody1_tasks = [
            self.async_select_one(
                row,
                "td:nth-child(2)",
                int_=True,
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for row in tbody1_rows
        ]

        tbody2_tasks = [
            self.async_select_one(
                row,
                "td:nth-child(2)",
                int_=True,
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for row in tbody2_rows
        ]

        main_results = await asyncio.gather(*main_tasks)
        tbody1_results = await asyncio.gather(*tbody1_tasks)
        tbody2_results = await asyncio.gather(*tbody2_tasks)

        tbody1_results.extend(tbody2_results)
        model_key = [
            "osym_kod", "year", "toplam", "ilk_bir", "ilk_bir_orn", "ilk_uc", "ilk_uc_orn", "ilk_on", "ilk_on_orn", "ort_tercih", "tercihler"
        ]
        tercih_key = [
            "tercih_1", "tercih_2", "tercih_3", "tercih_4", "tercih_5", "tercih_6", "tercih_7", "tercih_8", "tercih_9", "tercih_10",
            "tercih_11", "tercih_12", "tercih_13", "tercih_14", "tercih_15", "tercih_16", "tercih_17", "tercih_18", "tercih_19", "tercih_20",
            "tercih_21", "tercih_22", "tercih_23", "tercih_24"
        ]

        main_list = [osym_kod, year]
        main_list.extend(main_results)
        tercih_list = dict(zip(tercih_key, tbody1_results))
        main_list.append(tercih_list)
        results = dict(zip(model_key, main_list))

        return OrtTercih(**results)

    async def tercih_genel_parser(self, osym_kod: int, year: int) -> TercihGenel:
        selectors_tercih_genel = selectors["tercih_genel"]
        rows = self.bs.select(selectors_tercih_genel["rows"])
        
        tercihler = []
        
        tasks = [
            self.async_select_one(
                rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for data in selectors_tercih_genel["datas"]
        ]
        
        tercihler = await asyncio.gather(*tasks)
        
        model_keys = ["osym_kod", "year", "genel", "t_tercih", "k_tercih", "bos_tercih", "ort_tercih"]
        main_list = [osym_kod, year]
        main_list.extend(tercihler)
        tercihler = dict(zip(model_keys, main_list))

        return TercihGenel(**tercihler)

    async def tercih_uni_tur_parser(self, osym_kod: int, year: int) -> TercihUniTur:
        selectors_tercih_uni_tur = selectors["tercih_uni_tur"]
        rows = self.bs.select(selectors_tercih_uni_tur["rows"])

        if rows == []:
            return TercihUniTur(
                osym_kod=osym_kod,
                year=year,
                devlet=None,
                vakif=None,
                kibris=None,
                yabanci=None
            )
        
        uni_turleri = []
        
        tasks = [
            self.async_select_one(
                rows[data["index"] - 1],
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for data in selectors_tercih_uni_tur["datas"]
        ]
        
        uni_turleri = await asyncio.gather(*tasks)
        
        model_keys = ["osym_kod", "year", "devlet", "vakif", "kibris", "yabanci"]
        main_list = [osym_kod, year]
        main_list.extend(uni_turleri)
        uni_turleri = dict(zip(model_keys, main_list))

        return TercihUniTur(**uni_turleri)
    
    async def tercih_uni_parser(self, osym_kod: int, year: int) -> TercihUni:
        selectors_tercih_uni = selectors["tercih_uni"]
        tablolar = self.bs.select(selectors_tercih_uni["tablo_rows"])

        async def get_uni(tr_row) -> dict:

            tasks = [
                self.async_select_one(
                    tr_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=False,
                    ek_yer=False
                ) for data in selectors_tercih_uni["datas"]
            ]

            results = await asyncio.gather(*tasks)

            return {
                "isim": results[0],
                "sayi": results[1]
            } 

        devlet = None
        vakif = None
        kibris = None
        yabanci = None

        for tablo in tablolar:
            uni_tur = tablo.select_one(selectors_tercih_uni["baslik"]).text.strip()

            trs = tablo.select(selectors_tercih_uni["tr_rows"])

            uni_tasks = [get_uni(tr) for tr in trs]
            uni_results = await asyncio.gather(*uni_tasks)

            if uni_tur == "Devlet": devlet = uni_results
            elif uni_tur == "Vakıf": vakif = uni_results
            elif uni_tur == "Kıbrıs" or "KKTC": kibris = uni_results
            elif uni_tur == "Yabancı": yabanci = uni_results

        
        return TercihUni(
            osym_kod=osym_kod,
            year=year,
            devlet=devlet,
            vakif=vakif,
            kibris=kibris,
            yabanci=yabanci
        )
    
    async def tercih_il_parser(self, osym_kod: int, year: int) -> TercihIl:
        selectors_tercih_il = selectors["tercih_il"]
        rows = self.bs.select(selectors_tercih_il["rows"])

        async def get_il(il_row):
            tasks = [
                self.async_select_one(
                    il_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=False,
                    ek_yer=False
                ) for data in selectors_tercih_il["datas"]
            ]

            il_results = await asyncio.gather(*tasks)
            return {
                "isim":il_results[0],
                "sayi":il_results[1]
            }
        tasks = [get_il(il_row) for il_row in rows]
        results = await asyncio.gather(*tasks)
        

        return TercihIl(
            osym_kod=osym_kod,
            year=year,
            iller=results
        )
    
    async def tercih_fark_parser(self, osym_kod: int, year: int) -> TercihFark:
        if year == 2024: selectors_tercih_fark = selectors["tercih_fark"]["datas_2024"]
        else: selectors_tercih_fark = selectors["tercih_fark"]["datas"]


        tasks = [
            self.async_select_one(
                self.bs,
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for data in selectors_tercih_fark
        ]

        try: results = await asyncio.gather(*tasks)
        except AttributeError as e: results = [None, None, None, None, None]

        return TercihFark(
            osym_kod=osym_kod,
            year=year,
            ayni=results[0],
            farkli=results[1],
            kibris=results[2],
            onlisans=results[3],
            yabanci=results[4],
        )
    

    async def tercih_fark_onlisans_parser(self, osym_kod: int, year: int) -> TercihFark:

        if year == 2024: selectors_tercih_fark = selectors["tercih_fark"]["datas_2024"]
        else: selectors_tercih_fark = selectors["tercih_fark"]["datas"]


        tasks = [
            self.async_select_one(
                self.bs,
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for data in selectors_tercih_fark
        ]

        try: results = await asyncio.gather(*tasks)
        except AttributeError as e: results = [None, None, None, None, None]

        return TercihFarkOnlisans(
            osym_kod=osym_kod,
            year=year,
            ayni=results[0],
            farkli=results[1],
            kibris=results[2],
            lisans=results[3],
            yabanci=results[4],
        )
    
    
    async def tercih_program_parser(self, osym_kod: int, year: int) -> TercihProgram:
        selectors_tercih_program = selectors["tercih_program"]
        rows = self.bs.select(selectors_tercih_program["rows"])

        async def get_program(program_row):
            tasks = [
                self.async_select_one(
                    program_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=False,
                    ek_yer=False
                ) for data in selectors_tercih_program["datas"]
            ]

            program_results = await asyncio.gather(*tasks)
            return {
                "isim":program_results[0],
                "sayi":program_results[1]
            }
        tasks = [get_program(program_row) for program_row in rows]
        results = await asyncio.gather(*tasks)
        
        return TercihProgram(
            osym_kod=osym_kod,
            year=year,
            programlar=results
        )
    
    async def yerlesme_kosul_parser(self, osym_kod: int, year: int) -> YerlesmeKosul:
        selectors_yerlesme_kosul = selectors["yerlesme_kosul"]
        rows = self.bs.select(selectors_yerlesme_kosul["rows"])

        async def get_kosul(kosul_row):
            tasks = [
                self.async_select_one(
                    kosul_row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=data["type"] == "float",
                    yuzde=False,
                    ek_yer=False
                ) for data in selectors_yerlesme_kosul["datas"]
            ]

            kosul_results = await asyncio.gather(*tasks)
            return {
                "no":kosul_results[0],
                "aciklama":kosul_results[1]
            }
        
        tasks = [get_kosul(kosul_row) for kosul_row in rows]
        results = await asyncio.gather(*tasks)

        return YerlesmeKosul(
            osym_kod=osym_kod,
            year=year,
            kosullar=results
        )
    
    async def ogretim_uyesi_parser(self, osym_kod: int, year: int) -> OgretimUyesi:
        selectors_ogretim_uyesi = selectors["ogretim_uyesi"]["datas"]


        tasks = [
            self.async_select_one(
                self.bs,
                selector=f"{data['selector']}",
                int_=data["type"] == "int",
                float_=False,
                yuzde=False,
                ek_yer=False
            ) for data in selectors_ogretim_uyesi
        ]

        #results = await asyncio.gather(*tasks)
        try: results = await asyncio.gather(*tasks)
        except AttributeError as e: results = [None, None, None, None]
        
        return OgretimUyesi(
            osym_kod=osym_kod,
            year=year,
            prof=results[0],
            docent=results[1],
            dou=results[2],
            toplam=results[3]
        )
    
    async def kayitli_ogr_parser(self, osym_kod: int, year: int) -> KayitliOgrenci:
        selectors_kayitli_ogr = selectors["kayitli_ogr"]
        rows = self.bs.select(selectors_kayitli_ogr["rows"])
        toplam = None
        toplam_orn = None
        kiz = None
        kiz_orn = None
        erkek = None
        erkek_orn = None

        for row in rows:
            tasks = [
                self.async_select_one(
                    row,
                    selector=f"{data['selector']}",
                    int_=data["type"] == "int",
                    float_=False,
                    yuzde=data["type"] == "yuzde",
                    ek_yer=False
                ) for data in selectors_kayitli_ogr["datas"]
            ]

            results = await asyncio.gather(*tasks)

            if results[0] == "Toplam":
                toplam = results[1]
                toplam_orn = results[2]
            elif results[0] == "Kız":
                kiz = results[1]
                kiz_orn = results[2]
            elif results[0] == "Erkek":
                erkek = results[1]
                erkek_orn = results[2]

        return KayitliOgrenci(
            osym_kod=osym_kod,
            year=year,
            toplam=toplam,
            toplam_orn=toplam_orn,
            kiz=kiz,
            kiz_orn=kiz_orn,
            erkek=erkek,
            erkek_orn=erkek_orn
        )
    
    async def mezun_ogr_parser(self, osym_kod: int, year: int) -> MezunOgrenci:
        selectors_mezun_ogr = selectors["mezun_ogr"]
        
        mezun_control = self.bs.select_one(selectors_mezun_ogr["mezun_control"])

        if mezun_control is not None:
            return MezunOgrenci(
                osym_kod=osym_kod,
                year=year,
                yillar=None
            )
        
        else:
            rows = self.bs.select(selectors_mezun_ogr["rows"])
            yillar_list = []
            for row in rows:
                tasks = [
                    self.async_select_one(
                        row,
                        selector=f"{data['selector']}",
                        int_=data["type"] == "int",
                        float_=False,
                        yuzde=False,
                        ek_yer=False
                    ) for data in selectors_mezun_ogr["datas"]
                ]

                results = await asyncio.gather(*tasks)
                yillar_list.append({
                    "yil": results[0],
                    "toplam": results[1],
                    "erkek": results[2],
                    "kiz": results[3]
                })

            return MezunOgrenci(
                osym_kod=osym_kod,
                year=year,
                yillar=yillar_list
            )
        
    async def degisim_ogr_parser(self, osym_kod: int, year: int) -> DegisimOgrenci:
        selectors_degisim_ogr = selectors["degisim_ogr"]

        degisim_control = self.bs.select_one(selectors_degisim_ogr["control"])

        if degisim_control is not None:
            return DegisimOgrenci(
                osym_kod=osym_kod,
                year=year,
                degisimler=None
            )
        
        else:
            rows = self.bs.select(selectors_degisim_ogr["rows"])
            degisim_list = []
            for row in rows:
                tasks = [
                    self.async_select_one(
                        row,
                        selector=f"{data['selector']}",
                        int_=data["type"] == "int",
                        float_=False,
                        yuzde=False,
                        ek_yer=False
                    ) for data in selectors_degisim_ogr["datas"]
                ]

                results = await asyncio.gather(*tasks)
                degisim_list.append({
                    "program": results[0],
                    "giden": results[1],
                    "gelen": results[2]
                })

            return DegisimOgrenci(
                osym_kod=osym_kod,
                year=year,
                degisimler=degisim_list
            )

    async def yatay_gecis_parser(self, osym_kod: int, year: int) -> YatayGecis:
        selectors_yatay_gecis = selectors["yatay_gecis"]

        
        if year in [2023, 2024]:

            gelen_control = self.bs.select_one(selectors_yatay_gecis["gelen_kontrol"])
            giden_control = self.bs.select_one(selectors_yatay_gecis["giden_kontrol"])
            if gelen_control and giden_control is not None:
                return YatayGecis(
                    osym_kod=osym_kod,
                    year=year,
                    gelen=None,
                    giden=None
                )
            elif gelen_control is not None:

                return YatayGecis(
                    osym_kod=osym_kod,
                    year=year,
                    gelen=None,
                    giden=[{
                        "madde": "Giden",
                        "once":await self.async_select_one(
                            self.bs,
                            selector=selectors_yatay_gecis["2324_giden_onceki"],
                            int_=True,
                            float_=False,
                            yuzde=False,
                            ek_yer=False
                        ),
                        "simdi":await self.async_select_one(
                            self.bs,
                            selector=selectors_yatay_gecis["2324_giden_simdiki"],
                            int_=True,
                            float_=False,
                            yuzde=False,
                            ek_yer=False
                        )
                    }]
                )
            
            elif giden_control is not None:
                return YatayGecis(
                    osym_kod=osym_kod,
                    year=year,
                    gelen=[{
                        "madde": "Gelen",
                        "once":await self.async_select_one(
                            self.bs,
                            selector=selectors_yatay_gecis["2324_gelen_onceki"],
                            int_=True,
                            float_=False,
                            yuzde=False,
                            ek_yer=False
                        ),
                        "simdi":await self.async_select_one(
                            self.bs,
                            selector=selectors_yatay_gecis["2324_gelen_simdiki"],
                            int_=True,
                            float_=False,
                            yuzde=False,
                            ek_yer=False
                        )
                    }],
                    giden=None
                )
            else:
                return YatayGecis(
                    osym_kod=osym_kod,
                    year=year,
                    gelen=[{
                        "madde": "Gelen",
                        "once":await self.async_select_one(
                            self.bs,
                            selector=selectors_yatay_gecis["2324_gelen_onceki"],
                            int_=True,
                            float_=False,
                            yuzde=False,
                            ek_yer=False
                        ),
                        "simdi":await self.async_select_one(
                            self.bs,
                            selector=selectors_yatay_gecis["2324_gelen_simdiki"],
                            int_=True,
                            float_=False,
                            yuzde=False,
                            ek_yer=False
                        )
                    }],
                    giden=[{
                        "madde": "Giden",
                        "once":await self.async_select_one(
                            self.bs,
                            selector=selectors_yatay_gecis["2324_giden_onceki"],
                            int_=True,
                            float_=False,
                            yuzde=False,
                            ek_yer=False
                        ),
                        "simdi":await self.async_select_one(
                            self.bs,
                            selector=selectors_yatay_gecis["2324_giden_simdiki"],
                            int_=True,
                            float_=False,
                            yuzde=False,
                            ek_yer=False
                        )
                    }]
                )

            
        else:
            gelen_rows = self.bs.select(selectors_yatay_gecis["gelen_rows"])
            giden_rows = self.bs.select(selectors_yatay_gecis["giden_rows"])    

            async def get_row(row, datas):
                tasks = [
                    self.async_select_one(
                        row,
                        selector=f"{data['selector']}",
                        int_=data["type"] == "int",
                        float_=False,
                        yuzde=False,
                        ek_yer=False
                    ) for data in datas
                ]

                results = await asyncio.gather(*tasks)
                return {
                    "madde": results[0],
                    "once": results[1],
                    "simdi": results[2]
                }
            
            gelen_tasks = [get_row(row, selectors_yatay_gecis["datas"]) for row in gelen_rows]
            giden_tasks = [get_row(row, selectors_yatay_gecis["datas"]) for row in giden_rows]

            gelen_results = await asyncio.gather(*gelen_tasks)
            giden_results = await asyncio.gather(*giden_tasks)

            return YatayGecis(
                osym_kod=osym_kod,
                year=year,
                gelen=gelen_results,
                giden=giden_results
            )


