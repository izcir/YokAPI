from pydantic import BaseModel
from typing import Optional

class GenelBilgiler(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    bolum_ismi: Optional[str]
    program_kod: Optional[int]
    uni_tur: Optional[str]
    uni: Optional[str]
    fakulte: Optional[str]
    puan_tur: Optional[str]
    burs_tur: Optional[str]
    genel_kontenjan: Optional[int]
    ob_kontenjan: Optional[int]
    toplam_kontenjan: Optional[int]
    genel_yerlesen: Optional[int]
    ob_yerlesen: Optional[int]
    toplam_yerlesen: Optional[int]
    bos_kontenjan: Optional[int]
    ilk_yer_oran: Optional[float]
    kayit_yaptirmayan: Optional[int]
    ek_yerlesen: Optional[int]
    yer_012_son_puan: Optional[float]
    yer_018_son_puan: Optional[float]
    yer_012_son_sira: Optional[int]
    yer_018_son_sira: Optional[int]
    tavan_puan: Optional[float]
    tavan_basari_sira: Optional[int]
    obp_kirilan: Optional[int]
    ort_obp: Optional[float]
    ort_diploma: Optional[float]


class GenelBilgilerOnlisans(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    bolum_ismi: Optional[str]
    program_kod: Optional[int]
    uni_tur: Optional[str]
    uni: Optional[str]
    fakulte: Optional[str]
    puan_tur: Optional[str]
    burs_tur: Optional[str]
    genel_kontenjan: Optional[int]
    ob_kontenjan: Optional[int]
    toplam_kontenjan: Optional[int]
    genel_yerlesen: Optional[int]
    ob_yerlesen: Optional[int]
    toplam_yerlesen: Optional[int]
    bos_kontenjan: Optional[int]
    ilk_yer_oran: Optional[float]
    kayit_yaptirmayan: Optional[int]
    ek_yerlesen: Optional[int]
    yer_012_son_puan: Optional[float]
    yer_018_son_puan: Optional[float]
    yer_012_son_sira: Optional[int]
    yer_018_son_sira: Optional[int]
    tavan_2024_puan: Optional[float] = None
    tavan_2024_sira: Optional[int] = None
    ort_obp_2024: Optional[float] = None
    ort_dn_2024: Optional[float] = None


class Kontenjan(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    kont_gte: Optional[int]
    genel_kont: Optional[int]
    yer_oran: Optional[float]
    kesn_kayt: Optional[int]
    kayt_yptrmyn: Optional[int]
    tubitak: Optional[int]
    engelli: Optional[int]
    okl_bir_kont: Optional[int]
    okl_bir_yer: Optional[int]
    t_kont: Optional[int]
    t_yer: Optional[int]
    ek_yer: Optional[int]

class ModelDetay(BaseModel):
    sayi: Optional[int]
    orn: Optional[float]
    
class Cinsiyet(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    erkek: ModelDetay
    kadin: ModelDetay

class ModelDetayCinsiyet(BaseModel):
    sayi: Optional[int]
    orn: Optional[float]
    erkek: Optional[int]
    kadin: Optional[int]


class Bolgeler(BaseModel):
    toplam: ModelDetay
    akdeniz: ModelDetay
    dogu_anadolu: ModelDetay
    ege: ModelDetay
    guneydogu_anadolu: ModelDetay
    ic_anadolu: ModelDetay
    karadeniz: ModelDetay
    marmara: ModelDetay
    belli_degil: ModelDetay

class SehirDurum(BaseModel):
    toplam: ModelDetayCinsiyet
    ayni: ModelDetayCinsiyet
    farkli: ModelDetayCinsiyet
    belli_degil: ModelDetayCinsiyet

class CografiBolgeler(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    bolge: Bolgeler
    sehir: SehirDurum
    
class Il(BaseModel):
    isim: Optional[str]
    sayi: Optional[int]
    orn: Optional[float]

class Iller(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    sehirler: list[Il]

class OgrenimDurumu(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    toplam: ModelDetay
    lise_yeni: ModelDetay
    lise_mezun: ModelDetay
    uni_ogr: ModelDetay
    uni_mezun: ModelDetay
    diger: ModelDetay

class YilModelDetay(BaseModel):
    yil: Optional[str]
    sayi: Optional[int]
    orn: Optional[float]

class MezunYil(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    yillar: list[YilModelDetay]

class LiseAlanModelDetay(BaseModel):
    alan: Optional[str]
    sayi: Optional[int]
    orn: Optional[float]

class LiseAlan(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    alanlar: list[LiseAlanModelDetay]

class LiseTip(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    genel_lise: list[LiseAlanModelDetay]
    meslek_lise: list[LiseAlanModelDetay]

class LiseModelDetay(BaseModel):
    isim: Optional[str]
    toplam: Optional[int]
    yeni_mezun: Optional[int]
    eski_mezun: Optional[float]

class Liseler(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    liseler: list[LiseModelDetay]

class LiseYerlesme(BaseModel):
    kont_turu: Optional[str]
    isim: Optional[str]

class OkulBirinciKontenjan(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    toplam: Optional[int]
    genel: Optional[int]
    okul_bir: Optional[int]
    sehit_gazi: Optional[int]
    depremzede: Optional[float]
    kadin_34yas: Optional[int]
    liseler: list[LiseYerlesme]

class PuanModelDetay(BaseModel):
    kont_turu: Optional[str]
    kont: Optional[int]
    yerlesen: Optional[int]
    puan: Optional[float]

class SiraModelDetay(BaseModel):
    kont_turu: Optional[str]
    kont: Optional[int]
    yerlesen: Optional[int]
    sira_012: Optional[int]
    sira_012_006: Optional[int]

class TabanPuan(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    puanlar: list[PuanModelDetay]
    siralar: list[SiraModelDetay]

class PuanOnlisansModelDetay(BaseModel):
    kont_turu: Optional[str]
    kont: Optional[int]
    yerlesen: Optional[int]
    puan_012: Optional[float]
    puan_012_006: Optional[float]

class TabanPuanOnlisans(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    puanlar: list[PuanOnlisansModelDetay]
    siralar: list[SiraModelDetay]


class SonProfil(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    ogrnm_durumu: Optional[str]
    mezun_yil: Optional[int]
    lise_alan: Optional[str]
    puan: Optional[float]
    sira: Optional[int]
    katsayi: Optional[float]
    obp: Optional[float]
    dn: Optional[float]
    cinsiyet: Optional[str]
    il: Optional[str]

class DersModelDetay(BaseModel):
    ders: Optional[str]
    net_012: Optional[float]
    net_012_006: Optional[float]

class YksNet(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    yerlesen_012: Optional[float]
    yerlesen_012_006: Optional[float]
    ort_obp_012: Optional[float]
    ort_obp_012_006: Optional[float]
    dersler: Optional[list[DersModelDetay]]

class YksPuanModelDetay(BaseModel):
    yer_012: Optional[int]
    yer_012_006: Optional[int]
    obp_012: Optional[float]
    obp_012_006: Optional[float]
    tyt_012: Optional[float]
    tyt_012_006: Optional[float]

class YksPuan(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    ort_puan: Optional[list[YksPuanModelDetay]]
    dusuk_puan: Optional[list[YksPuanModelDetay]]

class YksSiraModelDetay(BaseModel):
    yer_012: Optional[int]
    yer_012_006: Optional[int]
    tyt_012: Optional[int]
    tyt_012_006: Optional[int]

class YksSira(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    ort_sira: Optional[list[YksSiraModelDetay]]
    dusuk_sira: Optional[list[YksSiraModelDetay]]

class TercihSiraDetay(BaseModel):
    tercih_1: Optional[int]
    tercih_2: Optional[int]
    tercih_3: Optional[int]
    tercih_4: Optional[int]
    tercih_5: Optional[int]
    tercih_6: Optional[int]
    tercih_7: Optional[int]
    tercih_8: Optional[int]
    tercih_9: Optional[int]
    tercih_10_sonra: Optional[int]

class TercihIstatistik(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    toplam: Optional[int] 
    aday: Optional[float]
    ort_tercih: Optional[float]
    ilk_bir: Optional[int]
    ilk_bir_orn: Optional[float]
    ilk_uc: Optional[int]
    ilk_uc_orn: Optional[float]
    ilk_dokuz: Optional[int]
    ilk_dokuz_orn: Optional[float]
    tercihler: Optional[TercihSiraDetay]

class OrtTercihDetay(BaseModel):
    tercih_1: Optional[int]
    tercih_2: Optional[int]
    tercih_3: Optional[int]
    tercih_4: Optional[int]
    tercih_5: Optional[int]
    tercih_6: Optional[int]
    tercih_7: Optional[int]
    tercih_8: Optional[int]
    tercih_9: Optional[int]
    tercih_10: Optional[int]
    tercih_11: Optional[int]
    tercih_12: Optional[int]
    tercih_13: Optional[int]
    tercih_14: Optional[int]
    tercih_15: Optional[int]
    tercih_16: Optional[int]
    tercih_17: Optional[int]
    tercih_18: Optional[int]
    tercih_19: Optional[int]
    tercih_20: Optional[int]
    tercih_21: Optional[int]
    tercih_22: Optional[int]
    tercih_23: Optional[int]
    tercih_24: Optional[int]

class OrtTercih(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    toplam: Optional[int]
    ilk_bir: Optional[int]
    ilk_bir_orn: Optional[float]
    ilk_uc: Optional[int]
    ilk_uc_orn: Optional[float]
    ilk_on: Optional[int]
    ilk_on_orn: Optional[float]
    ort_tercih: Optional[float]
    tercihler: Optional[OrtTercihDetay]

class TercihGenel(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    genel: Optional[int]
    t_tercih: Optional[int]
    k_tercih: Optional[int]
    bos_tercih: Optional[int]
    ort_tercih: Optional[int]


class TercihUniTur(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    devlet: Optional[int]
    vakif: Optional[int]
    kibris: Optional[int]
    yabanci: Optional[int]

class UniModelDetay(BaseModel):
    isim: Optional[str]
    sayi: Optional[int]

class TercihUni(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    devlet: Optional[list[UniModelDetay]]
    vakif: Optional[list[UniModelDetay]]
    kibris: Optional[list[UniModelDetay]]
    yabanci: Optional[list[UniModelDetay]]
    

class IlModelDetay(BaseModel):
    isim: Optional[str]
    sayi: Optional[int]

class TercihIl(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    iller: Optional[list[IlModelDetay]]

class TercihFark(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    ayni: Optional[int]
    farkli: Optional[int]
    kibris: Optional[int]
    onlisans: Optional[int]
    yabanci: Optional[int]
    
class TercihFarkOnlisans(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    ayni: Optional[int]
    farkli: Optional[int]
    kibris: Optional[int]
    lisans: Optional[int]
    yabanci: Optional[int]


class ProgramModelDetay(BaseModel):
    isim: Optional[str]
    sayi: Optional[int]

class TercihProgram(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    programlar: Optional[list[ProgramModelDetay]]

class KosulModelDetay(BaseModel):
    no: Optional[int]
    aciklama: Optional[str]

class YerlesmeKosul(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    kosullar: Optional[list[KosulModelDetay]]

class OgretimUyesi(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    prof: Optional[int]
    docent: Optional[int]
    dou: Optional[int]
    toplam: Optional[int]

class KayitliOgrenci(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    toplam: Optional[int]
    toplam_orn: Optional[float]
    kiz: Optional[int]
    kiz_orn: Optional[float]
    erkek: Optional[int]
    erkek_orn: Optional[float]

class MezunYilModelDetay(BaseModel):
    yil: Optional[str]
    toplam: Optional[int]
    erkek: Optional[int]
    kiz: Optional[int]
    
class MezunOgrenci(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    yillar: Optional[list[MezunYilModelDetay]]

class DegisimModelDetay(BaseModel):
    program: Optional[str]
    giden: Optional[int]
    gelen: Optional[int]

class DegisimOgrenci(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    degisimler: Optional[list[DegisimModelDetay]]

class YatayGecisModelDetay(BaseModel):
    madde: Optional[str]
    once: Optional[int]
    simdi: Optional[int]

class YatayGecis(BaseModel):
    osym_kod: Optional[int]
    year: Optional[int]
    gelen: Optional[list[YatayGecisModelDetay]]
    giden: Optional[list[YatayGecisModelDetay]]
