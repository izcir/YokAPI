# ▪ YokAPI
- YokAtlas için resmi olmayan API
- Unoffical API for YokAtlas

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Made with Python">
</p>
<p align="center">
  <img src="https://img.shields.io/github/repo-size/izcir/YokAPI?style=flat-square" alt="Repo Size">
  <img src="https://komarev.com/ghpvc/?username=izcir" alt="Profile Views">
  <img src="https://img.shields.io/github/license/izcir/YokAPI" alt="GitHub license">
  <img src="https://img.shields.io/github/last-commit/izcir/YokAPI" alt="GitHub last commit">
  <img src="https://img.shields.io/pypi/v/YokAPI" alt="PyPI Version">
</p>


## İletişim - Contact Me
- Telegram: [`izcipy`](https://t.me/izcipy)
- Mail: [`ramazan.izcir@gmail.com`](mailto:ramazan.izcir@gmail.com)

#### 🆕 **Net Sihirbazı desteği eklendi!** Bölüm bazlı tüm bölümlere son giren kişilerin netlerine ve obpsine ulaşın.


## 📦 Kurulum
```sh
pip install YokAPI
```

#### 📄 Örnek Kullanımlar
```python
from YokAPI import Lisans, Onlisans
import asyncio

async def main():
    # Bölüm arama ve ÖSYM program kodu bulma için aşağıdaki CSV bölümüne bakınız.
    async with Lisans(program_id=108210665, year=2024) as lisans:

        r = await lisans.kontenjan() # -> Kontenjan
        """ ---> Kontenjan(
                osym_kod=108210665,
                year=2024,
                kont_gte=85,
                genel_kont=85,
                yer_oran=100.0,
                kesn_kayt=88,
                kayt_yptrmyn=0,
                tubitak=None,
                engelli=None,
                okl_bir_kont=3,
                okl_bir_yer=3,
                t_kont=88,
                t_yer=88,
                ek_yer=0
            )
        """

        print(r.osym_kod) # -> 108210665
        print(r.year) # -> 2024
        print(r.genel_kont) # -> 85

        r_iller = await lisans.iller() # -> Iller
        """ ---> Iller(
                osym_kod=108210665,
                year=2024,
                sehirler=[Il(
                    isim="Toplam",
                    sayi=88,
                    oran=100.0
                ),
                Il(
                    isim="Samsun",
                    sayi=16,
                    orn=18.2
                ),
                ]
            )
        """
        print(r_iller.sehirler[1].isim) # -> Samsun
        print(r_iller.sehirler[1].sayi) # -> 16
        print(r_iller.sehirler[1].orn) # -> 18.2
        lise_dict = r_iller.model_dump()  # pydantic.BaseModel methods
        print(lise_dict) # -> {'osym_kod': 108210665, 'year': 2024, 'sehirler': [{'isim': 'Toplam', 'sayi': 88, 'orn': 100.0}, {'isim': 'Samsun', 'sayi': 16, 'orn': 18.2}, ...]

if __name__ == "__main__":
    asyncio.run(main())

```

### With Olmadan Kullanım
``` python
from YokAPI import Lisans, Onlisans
import asyncio

async def main():
    # Bölüm arama ve ÖSYM program kodu bulma için aşağıdaki CSV bölümüne bakınız.

    lisans_1 = Lisans(program_id=108210665, year=2024)
    r = await lisans_1.kontenjan() # -> Kontenjan
    print(r.tubitak) # -> None # 0

    await lisans_1.close() # oluşan sessionu kendimiz kapatmalıyız. with bloğu kendi kapatır.


if __name__ == "__main__":
    asyncio.run(main())
```

### Ayrı Session Kullanma
- Program session parametresi vermezseniz kendi sessionunu oluşturur. Kendi sessionuzu vermek isterseniz aşağıdaki kodu inceleyin.
  
```python
from YokAPI import Lisans, Onlisans
import asyncio
import aiohttp
# import certifi
# import ssl

async def main():
    # ssl_context = ssl.create_default_context(cafile=certifi.where())
    session_ = aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False),  # İsterseniz ssl_context kullanarak doğrulamayı açabilirsiniz.
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        }        
    )
    onlisans_1 = Onlisans(program_id=108250346, year=2024, session=session_)
    r = await onlisans_1.genel_blg() # -> GenelBilgilerOnlisans
    print(r.bos_kontenjan) # -> None # 0
    await session_.close()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🔎 Bölüm OSYM Kodu CSV’si (data/universities_departments.csv)

YokAPI kullanıcılarının bölümlerin ÖSYM program kodunu (osym_kod / program_code) hızlıca bulup veri çekebilmesi için, ÖSYM’nin yayımladığı kaynaklardan derlenmiş toplu ve temizlenmiş bir CSV dosyası eklenmiştir: `data/universities_departments.csv`.

- CSV sütunları:
  - program_code (ÖSYM kodu)
  - department_name (Bölüm adı)
  - university_name (Üniversite adı)
  - faculty_name (Fakülte adı)
  - is_undergraduate (Lisans=True, Önlisans=False)
  - years (ör. 2022,2023,2024)
  - tags (İngilizce, KKTC, vb.)
  - score_type (ör. SAY/SÖZ/EA/TYT)
  - scholarship_type (ör. Ücretsiz/Burslu/%50 İndirimli)

Kısa bir örnek satırlar:

| program_code | department_name             | university_name        | faculty_name              | is_undergraduate | years           | tags | score_type | scholarship_type |
|--------------|-----------------------------|------------------------|---------------------------|------------------|-----------------|------|------------|------------------|
| 103390230    | Abaza Dili ve Edebiyatı     | DÜZCE ÜNİVERSİTESİ     | Fen-Edebiyat Fakültesi    | True             | 2024            |      | SÖZ        | Ücretsiz         |
| 108690161    | Acil Durum ve Afet Yönetimi | PAMUKKALE ÜNİVERSİTESİ | Serinhisar Meslek Yüksekokulu            | False            | 2022,2023,2024  |      | TYT        | Ücretsiz         |

Notlar ve öneriler:
- Şu an YÖK Atlas’ta mevcut yıllar: 2022, 2023, 2024. Bir bölüm bazı yıllarda bulunmayabilir; istek atmadan önce CSV’deki `years` sütununu kontrol edip uygun yılı seçin.
- Büyük boyutlu JSON’u repo’ya eklemedim; isterseniz `data/data_csv_to_json.py` ile CSV’yi üniversiteye göre gruplanmış JSON’a dönüştürüp kullanabilirsiniz.
- YokAPI scraper ile üretilmiş daha detaylı ve temizlenmiş bir veri seti için: https://github.com/izcir/turkish-university-admissions-dataset

### Hızlı kullanım örnekleri

CSV’den osym_kod bulup YokAPI ile veri çekme (Lisans örneği):

```python
import pandas as pd
from YokAPI import Lisans
import asyncio

async def run():
    df = pd.read_csv("data/universities_departments.csv")

    row = df[(df["university_name"] == "ONDOKUZ MAYIS ÜNİVERSİTESİ") &
             (df["department_name"] == "Bilgisayar Mühendisliği") &
             (df["is_undergraduate"] == True)].iloc[0]

    program_id = int(row["program_code"]) # 108210665
    years = str(row.get("years")).split(",") # -> ['2022', '2023', '2024']
    year = years[-1] # -> 2024    

    async with Lisans(program_id=program_id, year=year) as lisans:
        genel = await lisans.genel_blg()
        print(genel.toplam_kontenjan, genel.yer_012_son_sira)

asyncio.run(run())
```

Önlisans bölümleri için benzer şekilde `is_undergraduate == False` filtreleyip `Onlisans` sınıfını kullanın.

---


## 📌 `Lisans` Fonksiyonlar ve Modeller <a name="Lisans"></a>
- Modeller `pydantic.BaseModel` sınıfındandır. [BaseModel docs](https://docs.pydantic.dev/latest/api/base_model/)

#### 🔹 Temel Bilgiler  
- `cinsiyet()` → [`Cinsiyet`](#cinsiyet)
- `kontenjan()` → [`Kontenjan`](#kontenjan)
- `ogr_durum()` → [`OgrenimDurumu`](#ogrenimdurumu)  
- `genel_blg()` → [`GenelBilgiler`](#genelbilgiler)

#### 📊 YKS Verileri
- `yks_net()` → [`YksNet`](#yksnet)
- `yks_puan()` → [`YksPuan`](#ykspuan)
- `yks_sira()` → [`YksSira`](#ykssira)
- `son_profil()` → [`SonProfil`](#sonprofil)

#### 🏫 Lise Bilgileri
- `lise_alan()` → [`LiseAlan`](#lisealan)
- `liseler()` → [`Liseler`](#liseler)
- `lise_grup_tip()` → [`LiseTip`](#lisetip)
- `okul_birinci()` → [`OkulBirinciKontenjan`](#okulbirincikontenjan)

#### 🎓 Üniversite Tercih Verileri
- `tercih_il()` → [`TercihIl`](#tercihil)
- `tercih_fark()` → [`TercihFark`](#tercihfark)
- `tercih_program()` → [`TercihProgram`](#tercihprogram)
- `tercih_uni()` → [`TercihUni`](#tercihuni)
- `tercih_uni_tur()` → [`TercihUniTur`](#tercihunitur)
- `tercih_istatistik()` → [`TercihIstatistik`](#tercihistatistik)
- `ort_tercih()` → [`OrtTercih`](#orttercih)
- `taban_puan()` → [`TabanPuan`](#tabanpuan)
- `tercih_genel()` → [`TercihGenel`](#tercihgenel)

#### 🔄 Öğrenci Hareketleri
- `mezun_yil()` → [`MezunYil`](#mezunyil)
- `degisim_ogr()` → [`DegisimOgrenci`](#degisimogrenci)
- `mezun_ogr()` → [`MezunOgrenci`](#mezunogrenci)
- `kayitli_ogr()` → [`KayitliOgrenci`](#kayitliogrenci)
- `yatay_gecis()` → [`YatayGecis`](#yataygecis)

#### 🏛 Akademik Bilgiler
- `ogretim_uyesi()` → [`OgretimUyesi`](#ogretimuyesi)
- `yerlesme_kosul()` → [`YerlesmeKosul`](#yerlesmekosul)

#### 🌍 Coğrafi Bilgiler
- `cograf_bolg()` → [`CografiBolgeler`](#cografibolgeler)
- `iller()` → [`İller`](#iller) 


## 📌 `Önlisans` Fonksiyonlar ve Modeller  <a name="Onlisans"></a>
- Modeller `pydantic.BaseModel` sınıfındandır. [BaseModel docs](https://docs.pydantic.dev/latest/api/base_model/)
- [`Lisans`](#Lisans)tan farklı Modeller: [`TercihFarkOnlisans`](#TercihFarkOnlisans), [`TabanPuanOnlisans`](#TabanPuanOnlisans), [`GenelBilgilerOnlisans`](#GenelBilgilerOnlisans)
- `Önlisans`ta bulunmayan YKS verileri: `yks_puan()`, `yks_sira()`


#### 🔹 Temel Bilgiler
- `cinsiyet()` → [`Cinsiyet`](#cinsiyet)
- `kontenjan()` → [`Kontenjan`](#kontenjan)
- `ogr_durum()` → [`OgrenimDurumu`](#ogrenimdurumu)
- `genel_blg()` → [`GenelBilgilerOnlisans`](#genelbilgiler)

#### 📊 YKS Verileri
- `yks_net()` → [`YksNet`](#yksnet)
- `son_profil()` → [`SonProfil`](#sonprofil)

#### 🏫 Lise Bilgileri
- `lise_alan()` → [`LiseAlan`](#lisealan)
- `liseler()` → [`Liseler`](#liseler)
- `lise_grup_tip()` → [`LiseTip`](#lisetip)
- `okul_birinci()` → [`OkulBirinci`](#okulbirincikontenjan)

#### 🎓 Üniversite Tercih Verileri
- `tercih_il()` → [`TercihIl`](#tercihil)
- `tercih_fark()` → [`TercihFarkOnlisans`](#tercihfarkonlisans)
- `tercih_program()` → [`TercihProgram`](#tercihprogram)
- `tercih_uni()` → [`TercihUni`](#tercihuni)
- `tercih_uni_tur()` → [`TercihUniTur`](#tercihunitur)
- `tercih_istatistik()` → [`TercihIstatistik`](#tercihistatistik)
- `ort_tercih()` → [`OrtTercih`](#orttercih)
- `taban_puan()` → [`TabanPuanOnlisans`](#tabanpuanonlisans)
- `tercih_genel()` → [`TercihGenel`](#tercihgenel)

#### 🔄 Öğrenci Hareketleri
- `mezun_yil()` → [`MezunYil`](#mezunyil)
- `degisim_ogr()` → [`DegisimOgrenci`](#degisimogrenci)
- `mezun_ogr()` → [`MezunOgrenci`](#mezunogrenci)
- `kayitli_ogr()` → [`KayitliOgrenci`](#kayitliogrenci)
- `yatay_gecis()` → [`YatayGecis`](#yataygecis)

#### 🏛 Akademik Bilgiler
- `ogretim_uyesi()` → [`OgretimUyesi`](#ogretimuyesi)
- `yerlesme_kosul()` → [`YerlesmeKosul`](#yerlesmekosul)

#### 🌍 Coğrafi Bilgiler
- `cograf_bolg()` → [`CografiBolgeler`](#cografibolgeler)
- `iller()` → [`İller`](#iller)

---

## 📌 `NetSihirbaziLisans` ve `NetSihirbaziOnlisans` Kullanımı

Net Sihirbazı, belirli bir bölüm için tüm üniversitelerdeki yerleşen son kişinin net ortalamalarını getirir.

### Örnek Kullanım

```python
from YokAPI import NetSihirbaziLisans, NetSihirbaziOnlisans
import asyncio

async def main():
    # Lisans için (bolum_id: data/bolumler_lisans.csv dosyasından alınır)
    async with NetSihirbaziLisans(bolum_id=11685) as net_lisans:  # 11685 = Abaza Dili ve Edebiyatı
        data = await net_lisans.net_sihirbazi()
        print(data.model_dump())
    
    # Önlisans için (bolum_id: data/bolumler_onlisans.csv dosyasından alınır)
    async with NetSihirbaziOnlisans(bolum_id=32020) as net_onlisans:  # 32020 = Bilgisayar Programcılığı
        data = await net_onlisans.net_sihirbazi()
        print(data.model_dump())

asyncio.run(main())
```

### Örnek Çıktı (Lisans - Abaza Dili ve Edebiyatı)

```json
{
  "bolum_id": 11685,
  "bolumler": [
    {
      "osym_kod": 103390230,
      "year": 2025,
      "uni": "DÜZCE ÜNİVERSİTESİ (4 Yıllık)",
      "katsayi": 0.12,
      "obp": 308.126,
      "puan": 213.28355,
      "bolum_yerlesen": "21",
      "dersler": {
        "TYT Türkçe": 8.0,
        "TYT Sosyal": 7.0,
        "TYT Mat": -1.75,
        "TYT Fen": 2.0,
        "AYT TDE": 0.5,
        "AYT Tar1": 3.25,
        "AYT Coğ1": -0.5,
        "AYT Tar2": 2.25,
        "AYT Coğ2": 5.0,
        "AYT Fel": -0.25,
        "AYT Din": 0.75
      }
    },
    {
      "osym_kod": 103390231,
      "year": 2025,
      "uni": "DÜZCE ÜNİVERSİTESİ (İÖ) (4 Yıllık)",
      "katsayi": 0.12,
      "obp": 295.432,
      "puan": 198.54321,
      "bolum_yerlesen": "15",
      "dersler": {
        "TYT Türkçe": 6.5,
        "TYT Sosyal": 5.0,
        "TYT Mat": 1.25,
        "TYT Fen": 3.0,
        "AYT TDE": 1.0,
        "AYT Tar1": 2.5,
        "AYT Coğ1": 0.75,
        "AYT Tar2": 1.5,
        "AYT Coğ2": 3.25,
        "AYT Fel": 0.5,
        "AYT Din": 1.25
      }
    }
  ]
}
```

### Notlar
- `bolum_id` değerleri `data/bolumler_lisans.csv` ve `data/bolumler_onlisans.csv` dosyalarından alınabilir.
- `dersler` alanı dinamik olarak oluşturulur ve bölümün puan türüne göre farklı dersler içerebilir (SAY/SÖZ/EA/TYT).
- Her üniversitedeki yerleşen son kişinin net ortalamaları döndürülür.

---


# 📌 Modeller  

- Bu bölümde, veri modelleri ve içerikleri açıklanmaktadır.

### [`GenelBilgiler`](#genelbilgiler)

| **Alan**              | **Tür**   | **Bilgi** |
|----------------------|---------|-----------|
| `osym_kod`          | `int`    | ÖSYM program kodu |
| `year`              | `int`    | Yıl |
| `bolum_ismi`        | `str`    | Bölüm adı |
| `program_kod`       | `int`    | Program kodu |
| `uni_tur`           | `str`    | Üniversite türü |
| `uni`               | `str`    | Üniversite adı |
| `fakulte`           | `str`    | Fakülte adı |
| `puan_tur`          | `str`    | Puan türü |
| `burs_tur`          | `str`    | Burs durumu |
| `genel_kontenjan`   | `int`    | Genel kontenjan |
| `ob_kontenjan`      | `int`    | OBP kontenjanı |
| `toplam_kontenjan`  | `int`    | Toplam kontenjan |
| `genel_yerlesen`    | `int`    | Genel yerleşen |
| `ob_yerlesen`       | `int`    | OBP yerleşen |
| `toplam_yerlesen`   | `int`    | Toplam yerleşen |
| `bos_kontenjan`     | `int`    | Boş kontenjan |
| `ilk_yer_oran`      | `float`  | İlk yerleşme oranı |
| `kayit_yaptirmayan` | `int`    | Kayıt yaptırmayan |
| `ek_yerlesen`       | `int`    | Ek yerleşen |
| `yer_012_son_puan`  | `float`  | 0.12 katsayı puanı |
| `yer_018_son_puan`  | `float`  | 0.18 katsayı puanı |
| `yer_012_son_sira`  | `int`    | 0.12 katsayı sıra |
| `yer_018_son_sira`  | `int`    | 0.18 katsayı sıra |
| `tavan_puan`        | `float`  | En yüksek puan |
| `tavan_basari_sira` | `int`    | En iyi sıra |
| `obp_kirilan`       | `int`    | OBP kırılan |
| `ort_obp`           | `float`  | Ortalama OBP |
| `ort_diploma`       | `float`  | Ortalama diploma |


### [`GenelBilgilerOnlisans`](#genelbilgileronlisans)  

| **Alan**              | **Tür**   | **Bilgi**                            |
|----------------------|-----------|--------------------------------------|
| `osym_kod`           | `int`     | ÖSYM program kodu                   |
| `year`               | `int`     | Yıl                                  |
| `bolum_ismi`         | `str`     | Bölüm adı                           |
| `program_kod`        | `int`     | Program kodu                        |
| `uni_tur`            | `str`     | Üniversite türü                     |
| `uni`                | `str`     | Üniversite adı                      |
| `fakulte`            | `str`     | Fakülte adı                         |
| `puan_tur`           | `str`     | Puan türü                           |
| `burs_tur`           | `str`     | Burs durumu                         |
| `genel_kontenjan`    | `int`     | Genel kontenjan                     |
| `ob_kontenjan`       | `int`     | OBP kontenjanı                      |
| `toplam_kontenjan`   | `int`     | Toplam kontenjan                    |
| `genel_yerlesen`     | `int`     | Genel yerleşen                      |
| `ob_yerlesen`        | `int`     | OBP yerleşen                        |
| `toplam_yerlesen`    | `int`     | Toplam yerleşen                     |
| `bos_kontenjan`      | `int`     | Boş kontenjan                       |
| `ilk_yer_oran`       | `float`   | İlk yerleşme oranı                  |
| `kayit_yaptirmayan`  | `int`     | Kayıt yaptırmayan                   |
| `ek_yerlesen`        | `int`     | Ek yerleşen                         |
| `yer_012_son_puan`   | `float`   | 0.12 katsayı puanı                  |
| `yer_018_son_puan`   | `float`   | 0.18 katsayı puanı                  |
| `yer_012_son_sira`   | `int`     | 0.12 katsayı sıra                   |
| `yer_018_son_sira`   | `int`     | 0.18 katsayı sıra                   |
| `tavan_2024_puan`    | `float`   | En yüksek puan (2024)               |
| `tavan_2024_sira`    | `int`     | En iyi sıra (2024)                  |
| `ort_obp_2024`       | `float`   | Ortalama OBP (2024)                 |
| `ort_dn_2024`        | `float`   | Ortalama diploma notu (2024)        |

### [`Kontenjan`](#kontenjan) 

| **Alan**            | **Tür**   | **Bilgi**                          |
|---------------------|-----------|------------------------------------|
| `osym_kod`         | `int`     | ÖSYM program kodu                 |
| `year`             | `int`     | Yıl                                |
| `kont_gte`        | `int`     | Kontenjan Genel, Tübitak, Engelli toplam    |
| `genel_kont`       | `int`     | Genel kontenjan                   |
| `yer_oran`         | `float`   | Yerleşme oranı                    |
| `kesn_kayt`        | `int`     | Kesin kayıt yaptıran              |
| `kayt_yptrmyn`     | `int`     | Kayıt yaptırmayan                 |
| `tubitak`          | `int`     | TÜBİTAK kontenjanı                 |
| `engelli`          | `int`     | Engelli kontenjanı                |
| `okl_bir_kont`     | `int`     | Okul birincisi kontenjanı         |
| `okl_bir_yer`      | `int`     | Okul birincisi yerleşen           |
| `t_kont`           | `int`     | Toplam kontenjan                  |
| `t_yer`            | `int`     | Toplam yerleşen                   |
| `ek_yer`           | `int`     | Ek yerleşen                       |

...existing code...
