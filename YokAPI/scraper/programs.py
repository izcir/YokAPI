from YokAPI.scraper.fetcher import Fetcher
from YokAPI.scraper.parser import Parser
import aiohttp
import asyncio

class BaseProgram:
    def __init__(self, session: aiohttp.ClientSession = None):
        self.fetcher = Fetcher(session)

    async def __aenter__(self):
        await self.fetcher.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.fetcher.__aexit__(exc_type, exc, tb)

    async def close(self):
        await self.fetcher.close()

    async def get_url(self, key: str) -> str:
        raise NotImplementedError("get_url tanımlanmamış.")
    
    async def genel_blg(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("genel_blg")
        )
        return await Parser(html).genel_blg_parser(self.program_id, self.year)

    async def kontenjan(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("kontenjan")
        )
        return await Parser(html).kontenjan_parser(self.program_id, self.year)

    async def cinsiyet(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("cinsiyet")
        )
        return await Parser(html).cinsiyet_parser(self.program_id, self.year)

    async def cograf_bolg(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("cograf_bolg")
        )
        return await Parser(html).cograf_bolg_parser(self.program_id, self.year)

    async def iller(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("iller")
        )
        return await Parser(html).iller_parser(self.program_id, self.year)

    async def ogr_durum(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("ogr_durum")
        )
        return await Parser(html).ogr_durum_parser(self.program_id, self.year)

    async def mezun_yil(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("mezun_yil")
        )
        return await Parser(html).mezun_yil_parser(self.program_id, self.year)

    async def lise_alan(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("lise_alan")
        )
        return await Parser(html).lise_alan_parser(self.program_id, self.year)

    async def lise_grup_tip(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("lise_grup_tip")
        )
        return await Parser(html).lise_grup_tip_parser(self.program_id, self.year)

    async def liseler(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("liseler")
        )
        return await Parser(html).liseler_parser(self.program_id, self.year)

    async def okul_birinci(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("okul_birinci")
        )
        return await Parser(html).okul_birinci_parser(self.program_id, self.year)

    async def taban_puan(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("taban_puan")
        )
        return await Parser(html).taban_puan_parser(self.program_id, self.year)

    async def son_profil(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("son_profil")
        )
        return await Parser(html).son_profil_parser(self.program_id, self.year)

    async def tercih_istatistik(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("tercih_istatistik")
        )
        return await Parser(html).tercih_istatistik_parser(self.program_id, self.year)

    async def ort_tercih(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("ort_tercih")
        )
        return await Parser(html).ort_tercih_parser(self.program_id, self.year)

    async def tercih_genel(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("tercih_genel")
        )
        return await Parser(html).tercih_genel_parser(self.program_id, self.year)

    async def tercih_uni_tur(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("tercih_uni_tur")
        )
        return await Parser(html).tercih_uni_tur_parser(self.program_id, self.year)

    async def tercih_uni(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("tercih_uni")
        )
        return await Parser(html).tercih_uni_parser(self.program_id, self.year)

    async def tercih_il(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("tercih_il")
        )
        return await Parser(html).tercih_il_parser(self.program_id, self.year)

    async def tercih_fark(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("tercih_fark")
        )
        return await Parser(html).tercih_fark_parser(self.program_id, self.year)

    async def tercih_program(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("tercih_program")
        )
        return await Parser(html).tercih_program_parser(self.program_id, self.year)

    async def yerlesme_kosul(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("yerlesme_kosul")
        )
        return await Parser(html).yerlesme_kosul_parser(self.program_id, self.year)

    async def ogretim_uyesi(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("ogretim_uyesi")
        )
        return await Parser(html).ogretim_uyesi_parser(self.program_id, self.year)

    async def kayitli_ogr(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("kayitli_ogr")
        )
        return await Parser(html).kayitli_ogr_parser(self.program_id, self.year)

    async def mezun_ogr(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("mezun_ogr")
        )
        return await Parser(html).mezun_ogr_parser(self.program_id, self.year)

    async def degisim_ogr(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("degisim_ogr")
        )
        return await Parser(html).degisim_ogr_parser(self.program_id, self.year)

    async def yatay_gecis(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("yatay_gecis")
        )
        return await Parser(html).yatay_gecis_parser(self.program_id, self.year)


    


class Lisans(BaseProgram):
    URLS = {
        "genel_blg":        "content/lisans-dynamic/1000_1.php?y={}",
        "kontenjan":        "content/lisans-dynamic/1000_2.php?y={}",
        "cinsiyet":         "content/lisans-dynamic/1010.php?y={}",
        "cograf_bolg":      "content/lisans-dynamic/1020ab.php?y={}",
        "iller":            "content/lisans-dynamic/1020c.php?y={}",
        "ogr_durum":        "content/lisans-dynamic/1030a.php?y={}",
        "mezun_yil":        "content/lisans-dynamic/1030b.php?y={}",
        "lise_alan":        "content/lisans-dynamic/1050b.php?y={}",
        "lise_grup_tip":    "content/lisans-dynamic/1050a.php?y={}",
        "liseler":          "content/lisans-dynamic/1060.php?y={}",
        "okul_birinci":     "content/lisans-dynamic/1030c.php?y={}",
        "taban_puan":       "content/lisans-dynamic/1000_3.php?y={}",
        "son_profil":       "content/lisans-dynamic/1070.php?y={}",
        "yks_net":          "content/lisans-dynamic/1210a.php?y={}",
        "yks_puan":         "content/lisans-dynamic/1220.php?y={}",
        "yks_sira":         "content/lisans-dynamic/1230.php?y={}",
        "tercih_istatistik":"content/lisans-dynamic/1080.php?y={}",
        "ort_tercih":       "content/lisans-dynamic/1040.php?y={}",
        "tercih_genel":     "content/lisans-dynamic/1300.php?y={}",
        "tercih_uni_tur":   "content/lisans-dynamic/1310.php?y={}",
        "tercih_uni":       "content/lisans-dynamic/1320.php?y={}",
        "tercih_il":        "content/lisans-dynamic/1330.php?y={}",
        "tercih_fark":      "content/lisans-dynamic/1340a.php?y={}",
        "tercih_program":   "content/lisans-dynamic/1340b.php?y={}",
        "yerlesme_kosul":   "content/lisans-dynamic/1110.php?y={}",
        "ogretim_uyesi":    "content/lisans-dynamic/2050.php?y={}",
        "kayitli_ogr":      "content/lisans-dynamic/2010.php?y={}",
        "mezun_ogr":        "content/lisans-dynamic/2030.php?y={}",
        "degisim_ogr":      "content/lisans-dynamic/2040.php?y={}",
        "yatay_gecis":      "content/lisans-dynamic/2060.php?y={}"
    }

    def __init__(self, program_id: int, year: int, session: aiohttp.ClientSession = None):
        super().__init__(session=session)
        self.year = year
        self.program_id = program_id
    
    def get_url(self, key):
        return self.URLS[key].format(self.program_id)
    
    async def yks_puan(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("yks_puan")
        )
        return await Parser(html).yks_puan_parser(self.program_id, self.year)

    async def yks_sira(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("yks_sira")
        )
        return await Parser(html).yks_sira_parser(self.program_id, self.year)

    async def yks_net(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("yks_net")
        )
        return await Parser(html).yks_net_parser(self.program_id, self.year)



class Onlisans(BaseProgram):
    URLS = {
        "genel_blg":        "content/onlisans-dynamic/3000_1.php?y={}", #düzenlencek
        "kontenjan":        "content/onlisans-dynamic/3000_2.php?y={}", #düzen
        "cinsiyet":         "content/onlisans-dynamic/3010.php?y={}",
        "cograf_bolg":      "content/onlisans-dynamic/3020ab.php?y={}",
        "iller":            "content/onlisans-dynamic/3020c.php?y={}",
        "ogr_durum":        "content/onlisans-dynamic/3030a.php?y={}",
        "mezun_yil":        "content/onlisans-dynamic/3030b.php?y={}",
        "lise_alan":        "content/onlisans-dynamic/3050b.php?y={}",
        "lise_grup_tip":    "content/onlisans-dynamic/3050a.php?y={}",
        "liseler":          "content/onlisans-dynamic/3060.php?y={}",
        "okul_birinci":     "content/onlisans-dynamic/3030c.php?y={}",
        "taban_puan":       "content/onlisans-dynamic/3000_3.php?y={}", #düzenlenecek + ##yorum satırı var htmlde
        "son_profil":       "content/onlisans-dynamic/3070.php?y={}",
        "yks_net":          "content/onlisans-dynamic/3210a.php?y={}",
        "tercih_istatistik":"content/onlisans-dynamic/3080.php?y={}",
        "ort_tercih":       "content/onlisans-dynamic/3040.php?y={}",
        "tercih_genel":     "content/onlisans-dynamic/3300_2.php?y={}",
        "tercih_uni_tur":   "content/onlisans-dynamic/3310b.php?y={}",
        "tercih_uni":       "content/onlisans-dynamic/3320b.php?y={}",
        "tercih_il":        "content/onlisans-dynamic/3330b.php?y={}",
        "tercih_fark":      "content/onlisans-dynamic/3340ab.php?y={}", # düzenlencek +
        "tercih_program":   "content/onlisans-dynamic/3340bb.php?y={}",
        "yerlesme_kosul":   "content/onlisans-dynamic/3110.php?y={}",
        "ogretim_uyesi":    "content/onlisans-dynamic/2050.php?y={}", 
        "kayitli_ogr":      "content/onlisans-dynamic/2010.php?y={}",
        "mezun_ogr":        "content/onlisans-dynamic/2030.php?y={}",
        "degisim_ogr":      "content/onlisans-dynamic/2040.php?y={}",
        "yatay_gecis":      "content/onlisans-dynamic/2060.php?y={}"
    }

    def __init__(self, program_id: int, year: int, session: aiohttp.ClientSession = None):
        super().__init__(session=session)
        self.year = year
        self.program_id = program_id
        
    def get_url(self, key):
        return self.URLS[key].format(self.program_id)
    
    async def genel_blg(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("genel_blg")
        )
        return await Parser(html).genel_blg_onlisans_parser(self.program_id, self.year)
    
    async def kontenjan(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("kontenjan")
        )
        return await Parser(html).kontenjan_onlisans_parser(self.program_id, self.year)

    async def tercih_fark(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("tercih_fark")
        )
        return await Parser(html).tercih_fark_onlisans_parser(self.program_id, self.year)

    async def taban_puan(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("taban_puan")
        )
        return await Parser(html).taban_puan_onlisans_parser(self.program_id, self.year)
    
    async def yks_net(self):
        html = await self.fetcher.send_request(
            self.year, 
            self.get_url("yks_net")
        )
        return await Parser(html).yks_net_parser(self.program_id, self.year, onlisans=True)


    async def all_functions(self):
        tasks = [
            self.genel_blg(),
            self.kontenjan(),
            self.cinsiyet(),
            self.cograf_bolg(),
            self.iller(),
            self.ogr_durum(),
            self.mezun_yil(),
            self.lise_alan(),
            self.lise_grup_tip(),
            self.liseler(),
            self.okul_birinci(),
            self.taban_puan(),
            self.son_profil(),
            self.yks_net(),
            self.tercih_istatistik(),
            self.ort_tercih(),
            self.tercih_genel(),
            self.tercih_uni_tur(),
            self.tercih_uni(),
            self.tercih_il(),
            self.tercih_fark(),
            self.tercih_program(),
            self.yerlesme_kosul(),
            self.ogretim_uyesi(),
            self.kayitli_ogr(),
            self.mezun_ogr(),
            self.degisim_ogr(),
            self.yatay_gecis()
        ]

        results = await asyncio.gather(*tasks)
        return results

