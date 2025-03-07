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
  <img src="https://img.shields.io/pypi/status/YokAPI" alt="PyPI Status">
  <img src="https://img.shields.io/pypi/v/YokAPI" alt="PyPI Version">
</p>


## İletişim - Contact Me
- Telegram: [`izcipy`](https://t.me/izcipy)
- Mail: [`ramazan.izcir@gmail.com`](mailto:ramazan.izcir@gmail.com)

## 📦 Kurulum
```sh
pip install YokAPI
```

#### 📄 Örnek Kullanımlar
```python
from YokAPI import Lisans, Onlisans
import asyncio

async def main():
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
``` pythonfrom YokAPI import Lisans, Onlisans
import asyncio

async def main():
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
import certifi
import ssl

async def main():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    session_ = aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=ssl_context), # ssl=False 
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

### ✔ Yapılacaklar 
- [ ] Dokümantasyon düzenlenecek
- [ ] Akademik YÖK API eklenecek
- [ ] Model yapısı düzenlenecek


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


### [`ModelDetay`](#modeldetay)
| **Alan**  | **Tür**   | **Bilgi**       |
|-----------|----------|----------------|
| `sayi`    | `int`    | Sayısal değer  |
| `orn`     | `float`  | Oran değeri    |

### [`Cinsiyet`](#cinsiyet)
| **Alan**  | **Tür**       | **Bilgi**                       |
|-----------|--------------|--------------------------------|
| `osym_kod` | `int`       | ÖSYM program kodu             |
| `year`     | `int`       | Yıl                            |
| `erkek`    | [`ModelDetay`](#modeldetay) | Erkek aday verileri  |
| `kadin`    | [`ModelDetay`](#modeldetay) | Kadın aday verileri  |

### [`Bolgeler`](#bolgeler)
| **Alan**              | **Tür**                 | **Bilgi**                      |
|----------------------|------------------------|--------------------------------|
| `toplam`            | [`ModelDetay`](#modeldetay)  | Genel toplam verileri        |
| `akdeniz`           | [`ModelDetay`](#modeldetay)  | Akdeniz bölgesi verileri     |
| `dogu_anadolu`      | [`ModelDetay`](#modeldetay)  | Doğu Anadolu bölgesi verileri |
| `ege`               | [`ModelDetay`](#modeldetay)  | Ege bölgesi verileri         |
| `guneydogu_anadolu` | [`ModelDetay`](#modeldetay)  | Güneydoğu Anadolu verileri  |
| `ic_anadolu`        | [`ModelDetay`](#modeldetay)  | İç Anadolu bölgesi verileri  |
| `karadeniz`         | [`ModelDetay`](#modeldetay)  | Karadeniz bölgesi verileri   |
| `marmara`           | [`ModelDetay`](#modeldetay)  | Marmara bölgesi verileri     |
| `belli_degil`       | [`ModelDetay`](#modeldetay)  | Bölgesi belli olmayan veriler |

### [`ModelDetayCinsiyet`](#modeldetaycinsiyet)
| **Alan**  | **Tür**   | **Bilgi**                          |
|-----------|----------|----------------------------------|
| `sayi`    | `int`    | Toplam sayısal değer            |
| `orn`     | `float`  | Oran değeri                     |
| `erkek`   | `int`    | Erkek sayısı                    |
| `kadin`   | `int`    | Kadın sayısı                    |

### [`SehirDurum`](#sehirdurum)
| **Alan**       | **Tür**                                  | **Bilgi**                     |
|---------------|-----------------------------------------|-------------------------------|
| `toplam`      | [`ModelDetayCinsiyet`](#modeldetaycinsiyet) | Toplam şehir verileri       |
| `ayni`        | [`ModelDetayCinsiyet`](#modeldetaycinsiyet) | Aynı şehirde kalanlar       |
| `farkli`      | [`ModelDetayCinsiyet`](#modeldetaycinsiyet) | Farklı şehire gidenler      |
| `belli_degil` | [`ModelDetayCinsiyet`](#modeldetaycinsiyet) | Şehir bilgisi belli olmayanlar |

### [`CografiBolgeler`](#cografibolgeler)
| **Alan**    | **Tür**                        | **Bilgi**             |
|------------|---------------------------------|-----------------------|
| `osym_kod` | `int`                           | ÖSYM program kodu     |
| `year`     | `int`                           | Yıl                   |
| `bolge`    | [`Bolgeler`](#bolgeler)         | Coğrafi bölge verileri |
| `sehir`    | [`SehirDurum`](#sehirdurum)     | Şehir bazlı veriler    |

### [`Il`](#il)
| **Alan**  | **Tür**   | **Bilgi**         |
|-----------|----------|-------------------|
| `isim`    | `str`    | Şehir adı         |
| `sayi`    | `int`    | Sayısal değer     |
| `orn`     | `float`  | Oran değeri       |

### [`Iller`](#iller)
| **Alan**    | **Tür**          | **Bilgi**               |
|------------|-----------------|-------------------------|
| `osym_kod` | `int`            | ÖSYM program kodu       |
| `year`     | `int`            | Yıl                     |
| `sehirler` | _list[_[`Il`](#il)_]_       | Şehir bazlı detaylar    |

### [`OgrenimDurumu`](#ogrenimdurumu)
| **Alan**      | **Tür**                    | **Bilgi**                |
|--------------|---------------------------|--------------------------|
| `osym_kod`   | `int`                      | ÖSYM program kodu        |
| `year`       | `int`                      | Yıl                      |
| `toplam`     | [`ModelDetay`](#modeldetay) | Toplam kayıtlar          |
| `lise_yeni`  | [`ModelDetay`](#modeldetay) | Yeni lise mezunları      |
| `lise_mezun` | [`ModelDetay`](#modeldetay) | Önceki lise mezunları    |
| `uni_ogr`    | [`ModelDetay`](#modeldetay) | Üniversite öğrencileri   |
| `uni_mezun`  | [`ModelDetay`](#modeldetay) | Üniversite mezunları     |
| `diger`      | [`ModelDetay`](#modeldetay) | Diğer kategoriler        |

### [`YilModelDetay`](#yilmodeldetay)
| **Alan**  | **Tür**   | **Bilgi**         |
|-----------|----------|-------------------|
| `yil`     | `str`    | Mezuniyet yılı    |
| `sayi`    | `int`    | Sayısal değer     |
| `orn`     | `float`  | Oran değeri       |

### [`MezunYil`](#mezunyil)
| **Alan**    | **Tür**                   | **Bilgi**               |
|------------|--------------------------|-------------------------|
| `osym_kod` | `int`                     | ÖSYM program kodu       |
| `year`     | `int`                     | Yıl                     |
| `yillar`   | _list[_[`YilModelDetay`](#yilmodeldetay)_]_   | Mezuniyet yılları       |

### [`LiseAlanModelDetay`](#lisealanmodeldetay)
| **Alan**  | **Tür**   | **Bilgi**         |
|-----------|----------|-------------------|
| `alan`    | `str`    | Lise alan adı     |
| `sayi`    | `int`    | Sayısal değer     |
| `orn`     | `float`  | Oran değeri       |

### [`LiseAlan`](#lisealan)
| **Alan**    | **Tür**                       | **Bilgi**               |
|------------|------------------------------|-------------------------|
| `osym_kod` | `int`                         | ÖSYM program kodu       |
| `year`     | `int`                         | Yıl                     |
| `alanlar`  | _list[_[`LiseAlanModelDetay`](#lisealanmodeldetay)_]_    | Lise alan detayları     |

### [`LiseTip`](#lisetip)
| **Alan**       | **Tür**                                                 | **Bilgi**               |
|---------------|-----------------------------------------------------|-------------------------|
| `osym_kod`    | `int`                                               | ÖSYM program kodu       |
| `year`        | `int`                                               | Yıl                     |
| `genel_lise`  | _list[_[`LiseAlanModelDetay`](#lisealanmodeldetay)_]_   | Genel lise detayları    |
| `meslek_lise` | _list[_[`LiseAlanModelDetay`](#lisealanmodeldetay)_]_  | Meslek lisesi detayları |

### [`LiseModelDetay`](#lisemodeldetay)
| **Alan**      | **Tür**      | **Bilgi**                   |
|---------------|--------------|-----------------------------|
| `isim`        | `str`        | Lise ismi                  |
| `toplam`      | `int`        | Toplam öğrenci sayısı      |
| `yeni_mezun`  | `int`        | Yeni mezun öğrenci sayısı  |
| `eski_mezun`  | `float`      | Eski mezunların oranı      |

### [`Liseler`](#liseler)
| **Alan**    | **Tür**                                         | **Bilgi**               |
|------------|---------------------------------------------|-------------------------|
| `osym_kod` | `int`                                     | ÖSYM program kodu       |
| `year`     | `int`                                     | Yıl                     |
| `liseler`  | _list[_[`LiseModelDetay`](#lisemodeldetay)_]_ | Lise bazlı detaylar     |

### [`LiseYerlesme`](#liseyerlesme)
| **Alan**     | **Tür**      | **Bilgi**                |
|--------------|--------------|--------------------------|
| `kont_turu`  | `str`        | Kontenjan türü           |
| `isim`       | `str`        | Lise ismi                |


### [`OkulBirinciKontenjan`](#okulbirincikontenjan)
| **Alan**       | **Tür**                                        | **Bilgi**                     |
|---------------|------------------------------------------|-----------------------------|
| `osym_kod`    | `int`                                    | ÖSYM program kodu           |
| `year`        | `int`                                    | Yıl                         |
| `toplam`      | `int`                                    | Toplam kontenjan            |
| `genel`       | `int`                                    | Genel kontenjan             |
| `okul_bir`    | `int`                                    | Okul birincisi kontenjanı   |
| `sehit_gazi`  | `int`                                    | Şehit/gazi yakını kontenjanı |
| `depremzede`  | `float`                                  | Depremzede kontenjanı       |
| `kadin_34yas` | `int`                                    | 34 yaş üstü kadın kontenjanı |
| `liseler`     | _list[_[`LiseYerlesme`](#liseyerlesme)_]_   | Lise yerleşme detayları     |

### `PuanModelDetay`
| **Alan**      | **Tür**      | **Bilgi**                           |
|---------------|--------------|-------------------------------------|
| `kont_turu`   | `str`        | Kontenjan türü                     |
| `kont`        | `int`        | Kontenjan sayısı                   |
| `yerlesen`    | `int`        | Yerleşen öğrenci sayısı            |
| `puan`        | `float`      | Puan değeri                        |

### `SiraModelDetay`
| **Alan**        | **Tür**      | **Bilgi**                           |
|-----------------|--------------|-------------------------------------|
| `kont_turu`     | `str`        | Kontenjan türü                     |
| `kont`          | `int`        | Kontenjan sayısı                   |
| `yerlesen`      | `int`        | Yerleşen öğrenci sayısı            |
| `sira_012`      | `int`        | 0.12 katsayılı yerleşen sıra       |
| `sira_012_006`  | `int`        | 0.18 katsayılı yerleşen sıra       |


### [`TabanPuan`](#tabanpuan)
| **Alan**    | **Tür**                                          | **Bilgi**               |
|------------|----------------------------------------------|-------------------------|
| `osym_kod` | `int`                                        | ÖSYM program kodu       |
| `year`     | `int`                                        | Yıl                     |
| `puanlar`  | _list[_[`PuanModelDetay`](#puanmodeldetay)_]_  | Puan detayları          |
| `siralar`  | _list[_[`SiraModelDetay`](#siramodeldetay)_]_   | Başarı sıraları         |

### `PuanOnlisansModelDetay`
| **Alan**        | **Tür**      | **Bilgi**                           |
|-----------------|--------------|-------------------------------------|
| `kont_turu`     | `str`        | Kontenjan türü                     |
| `kont`          | `int`        | Kontenjan sayısı                   |
| `yerlesen`      | `int`        | Yerleşen öğrenci sayısı            |
| `puan_012`      | `float`      | 0.12 katsayılı puan                |
| `puan_012_006`  | `float`      | 0.18 katsayılı puan                |


### [`TabanPuanOnlisans`](#tabanpuanonlisans)
| **Alan**    | **Tür**                                                  | **Bilgi**               |
|------------|------------------------------------------------------|-------------------------|
| `osym_kod` | `int`                                                | ÖSYM program kodu       |
| `year`     | `int`                                                | Yıl                     |
| `puanlar`  | _list[_[`PuanOnlisansModelDetay`](#puanonlisansmodeldetay)_]_ | Önlisans puan detayları |
| `siralar`  | _list[_[`SiraModelDetay`](#siramodeldetay)_]_            | Başarı sıraları         |

### [`SonProfil`](#sonprofil)
| **Alan**         | **Tür**     | **Bilgi**                 |
|-----------------|---------|-------------------------|
| `osym_kod`      | `int`   | ÖSYM program kodu       |
| `year`          | `int`   | Yıl                     |
| `ogrnm_durumu`  | `str`   | Öğrenim durumu          |
| `mezun_yil`     | `int`   | Mezuniyet yılı          |
| `lise_alan`     | `str`   | Lise alanı              |
| `puan`          | `float` | Puan                    |
| `sira`          | `int`   | Sıralama                |
| `katsayi`       | `float` | Katsayı                 |
| `obp`           | `float` | OBP puanı               |
| `dn`            | `float` | Diploma notu            |
| `cinsiyet`      | `str`   | Cinsiyet                |
| `il`           | `str`   | İl                      |

### [`DersModelDetay`](#dersmodeldetay)
| **Alan**     | **Tür**      | **Bilgi**                    |
|--------------|--------------|------------------------------|
| `ders`       | `str`        | Ders adı                     |
| `net_012`    | `float`      | 0.12 katsayılı net           |
| `net_012_006`| `float`      | 0.18 katsayılı net           |

### [`YksNet`](#yksnet)
| **Alan**            | **Tür**      | **Bilgi**                              |
|---------------------|--------------|----------------------------------------|
| `osym_kod`          | `int`        | ÖSYM program kodu                     |
| `year`              | `int`        | Yıl                                    |
| `yerlesen_012`      | `float`      | 0.12 katsayılı yerleşen oranı         |
| `yerlesen_012_006`  | `float`      | 0.18 katsayılı yerleşen oranı         |
| `ort_obp_012`       | `float`      | 0.12 katsayılı ortalama OBP           |
| `ort_obp_012_006`   | `float`      | 0.18 katsayılı ortalama OBP           |
| `dersler`           | _list[_[`DersModelDetay`](#dersmodeldetay)_]_ | Derslerin detayları           |

### [`YksPuanModelDetay`](#ykspuanmodeldetay)
| **Alan**          | **Tür**      | **Bilgi**                              |
|-------------------|--------------|----------------------------------------|
| `yer_012`         | `int`        | 0.12 katsayılı yerleşen sayısı        |
| `yer_012_006`     | `int`        | 0.18 katsayılı yerleşen sayısı        |
| `obp_012`         | `float`      | 0.12 katsayılı OBP                    |
| `obp_012_006`     | `float`      | 0.18 katsayılı OBP                    |
| `tyt_012`         | `float`      | 0.12 katsayılı TYT puanı              |
| `tyt_012_006`     | `float`      | 0.18 katsayılı TYT puanı              |

### [`YksPuan`](#ykspuan)
| **Alan**        | **Tür**      | **Bilgi**                              |
|-----------------|--------------|----------------------------------------|
| `osym_kod`      | `int`        | ÖSYM program kodu                     |
| `year`          | `int`        | Yıl                                    |
| `ort_puan`      | _list[_[`YksPuanModelDetay`](#ykspuanmodeldetay)_]_ | Ortalama puanlar                     | 
| `dusuk_puan`    | _list[_[`YksPuanModelDetay`](#ykspuanmodeldetay)_]_ | Düşük puanlar                        |

### [`YksSiraModelDetay`](#ykssiramodeldetay)
| **Alan**        | **Tür**      | **Bilgi**                           |
|-----------------|--------------|-------------------------------------|
| `yer_012`       | `int`        | 0.12 katsayılı yerleşen sayısı      |
| `yer_012_006`   | `int`        | 0.18 katsayılı yerleşen sayısı      |
| `tyt_012`       | `int`        | TYT 0.12 katsayılı yerleşen sayısı  |
| `tyt_012_006`   | `int`        | TYT 0.18 katsayılı yerleşen sayısı  |

### [`YksSira`](#ykssira)
| **Alan**        | **Tür**      | **Bilgi**                           |
|-----------------|--------------|-------------------------------------|
| `osym_kod`      | `int`        | ÖSYM kodu                          |
| `year`          | `int`        | Yıl                                 |
| `ort_sira`      | _list[_[`YksSiraModelDetay`](#ykssiramodeldetay)_]_  | Ortalama sıralama detayları     |
| `dusuk_sira`    | _list[_[`YksSiraModelDetay`](#ykssiramodeldetay)_]_  | Düşük sıralama detayları       |

### [`TercihSiraDetay`](#tercihsiradetay)
| **Alan**        | **Tür**      | **Bilgi**                           |
|-----------------|--------------|-------------------------------------|
| `tercih_1`      | `int`        | 1. tercih sırası                    |
| `tercih_2`      | `int`        | 2. tercih sırası                    |
| `tercih_3`      | `int`        | 3. tercih sırası                    |
| `tercih_4`      | `int`        | 4. tercih sırası                    |
| `tercih_5`      | `int`        | 5. tercih sırası                    |
| `tercih_6`      | `int`        | 6. tercih sırası                    |
| `tercih_7`      | `int`        | 7. tercih sırası                    |
| `tercih_8`      | `int`        | 8. tercih sırası                    |
| `tercih_9`      | `int`        | 9. tercih sırası                    |
| `tercih_10_sonra` | `int`      | 10. tercih sonrası                  |

### [`TercihIstatistik`](#tercihistatistik)
| **Alan**        | **Tür**      | **Bilgi**                           |
|-----------------|--------------|-------------------------------------|
| `osym_kod`      | `int`        | ÖSYM kodu                          |
| `year`          | `int`        | Yıl                                 |
| `toplam`        | `int`        | Toplam tercih sayısı               |
| `aday`          | `float`      | Aday sayısı                        |
| `ort_tercih`    | `float`      | Ortalama tercih sayısı             |
| `ilk_bir`       | `int`        | İlk tercih yapılan sayısı          |
| `ilk_bir_orn`   | `float`      | İlk tercih oranı                   |
| `ilk_uc`        | `int`        | İlk üç tercih yapılan sayısı       |
| `ilk_uc_orn`    | `float`      | İlk üç tercih oranı                |
| `ilk_dokuz`     | `int`        | İlk dokuz tercih yapılan sayısı    |
| `ilk_dokuz_orn` | `float`      | İlk dokuz tercih oranı             |
| `tercihler`     | _list[_[`TercihSiraDetay`](#tercihsiradetay)_]_ | Tercih sırası detayları        | 

### [`OrtTercihDetay`](#orttercihdetay)
| **Alan**        | **Tür**      | **Bilgi**                           |
|-----------------|--------------|-------------------------------------|
| `tercih_1`      | `int`        | 1. tercih sırası                    |
| `tercih_2`      | `int`        | 2. tercih sırası                    |
| `tercih_3`      | `int`        | 3. tercih sırası                    |
| `tercih_4`      | `int`        | 4. tercih sırası                    |
| `tercih_5`      | `int`        | 5. tercih sırası                    |
| `tercih_6`      | `int`        | 6. tercih sırası                    |
| `tercih_7`      | `int`        | 7. tercih sırası                    |
| `tercih_8`      | `int`        | 8. tercih sırası                    |
| `tercih_9`      | `int`        | 9. tercih sırası                    |
| `tercih_10`     | `int`        | 10. tercih sırası                   |
| `tercih_11`     | `int`        | 11. tercih sırası                   |
| `tercih_12`     | `int`        | 12. tercih sırası                   |
| `tercih_13`     | `int`        | 13. tercih sırası                   |
| `tercih_14`     | `int`        | 14. tercih sırası                   |
| `tercih_15`     | `int`        | 15. tercih sırası                   |
| `tercih_16`     | `int`        | 16. tercih sırası                   |
| `tercih_17`     | `int`        | 17. tercih sırası                   |
| `tercih_18`     | `int`        | 18. tercih sırası                   |
| `tercih_19`     | `int`        | 19. tercih sırası                   |
| `tercih_20`     | `int`        | 20. tercih sırası                   |
| `tercih_21`     | `int`        | 21. tercih sırası                   |
| `tercih_22`     | `int`        | 22. tercih sırası                   |
| `tercih_23`     | `int`        | 23. tercih sırası                   |
| `tercih_24`     | `int`        | 24. tercih sırası                   |

### [`OrtTercih`](#orttercih)
| **Alan**        | **Tür**      | **Bilgi**                           |
|-----------------|--------------|-------------------------------------|
| `osym_kod`      | `int`        | ÖSYM kodu                          |
| `year`          | `int`        | Yıl                                 |
| `toplam`        | `int`        | Toplam tercih sayısı               |
| `ilk_bir`       | `int`        | İlk tercih yapılan sayısı          |
| `ilk_bir_orn`   | `float`      | İlk tercih oranı                   |
| `ilk_uc`        | `int`        | İlk üç tercih yapılan sayısı       |
| `ilk_uc_orn`    | `float`      | İlk üç tercih oranı                |
| `ilk_on`        | `int`        | İlk on tercih yapılan sayısı       |
| `ilk_on_orn`    | `float`      | İlk on tercih oranı                |
| `ort_tercih`    | `float`      | Ortalama tercih sayısı             |
| `tercihler`     | _list[_[`OrtTercihDetay`](#orttercihdetay)_]_ | Tercih sırası detayları         | 

### [`TercihGenel`](#tercihgenel)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `genel`          | `int`        | Genel tercih sayısı               |
| `t_tercih`       | `int`        | Tam tercih sayısı                 |
| `k_tercih`       | `int`        | Kayıtlı tercih sayısı             |
| `bos_tercih`     | `int`        | Boş tercih sayısı                 |
| `ort_tercih`     | `int`        | Ortalama tercih sayısı            |

### [`TercihUniTur`](#tercihunitur)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `devlet`         | `int`        | Devlet üniversite tercih sayısı   |
| `vakif`          | `int`        | Vakıf üniversite tercih sayısı    |
| `kibris`         | `int`        | Kıbrıs üniversite tercih sayısı   |
| `yabanci`        | `int`        | Yabancı üniversite tercih sayısı  |

### [`UniModelDetay`](#unimodeldetay)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `isim`           | `str`        | Üniversite ismi                   |
| `sayi`           | `int`        | Üniversiteye yapılan başvuru sayısı |

### [`TercihUni`](#tercihuni)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `devlet`         | _list[_[`UniModelDetay`](#unimodeldetay)_]_ | Devlet üniversite detayları   | 
| `vakif`          | _list[_[`UniModelDetay`](#unimodeldetay)_]_ | Vakıf üniversite detayları    |
| `kibris`         | _list[_[`UniModelDetay`](#unimodeldetay)_]_ | Kıbrıs üniversite detayları   |
| `yabanci`        | _list[_[`UniModelDetay`](#unimodeldetay)_]_ | Yabancı üniversite detayları  |

### [`IlModelDetay`](#ilmodeldetay)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `isim`           | `str`        | İl ismi                           |
| `sayi`           | `int`        | İl bazındaki tercihlerin sayısı   |

### [`TercihIl`](#tercihil)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `iller`          | _list[_[`IlModelDetay`](#ilmodeldetay)_]_ | İllerle ilgili tercih detayları| 

### [`TercihFark`](#tercihfark)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `ayni`           | `int`        | Ayni tercihler                    |
| `farkli`         | `int`        | Farklı tercihler                  |
| `kibris`         | `int`        | Kıbrıs tercihler                  |
| `onlisans`       | `int`        | Ön lisans tercihler               |
| `yabanci`        | `int`        | Yabancı tercihler                 |

### [`TercihFarkOnlisans`](#tercihfarkonlisans)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `ayni`           | `int`        | Ayni tercihler                    |
| `farkli`         | `int`        | Farklı tercihler                  |
| `kibris`         | `int`        | Kıbrıs tercihler                  |
| `lisans`         | `int`        | Lisans tercihler                  |
| `yabanci`        | `int`        | Yabancı tercihler                 |

### [`ProgramModelDetay`](#programmodeldetay)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `isim`           | `str`        | Program ismi                      |
| `sayi`           | `int`        | Program tercihlerinin sayısı      |

### [`TercihProgram`](#tercihprogram)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `programlar`     | _list[_[`ProgramModelDetay`](#programmodeldetay)_]_ | Program detayları     | 

### [`KosulModelDetay`](#kosulmodeldetay)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `no`             | `int`        | Kosul numarası                    |
| `aciklama`       | `str`        | Kosul açıklaması                  |

### [`YerlesmeKosul`](#yerlesmekosul)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `kosullar`       | _list[_[`KosulModelDetay`](#kosulmodeldetay)_]_ | Kosul detayları         | 

### [`OgretimUyesi`](#ogretimuyesi)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `prof`           | `int`        | Profesör sayısı                   |
| `docent`         | `int`        | Doçent sayısı                     |
| `dou`            | `int`        | Dr. Öğretim Üyesi sayısı          |
| `toplam`         | `int`        | Toplam öğretim üyesi sayısı       |

### [`KayitliOgrenci`](#kayitliogrenci)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `toplam`         | `int`        | Toplam öğrenci sayısı             |
| `toplam_orn`     | `float`      | Toplam öğrenci oranı              |
| `kiz`            | `int`        | Kız öğrenci sayısı                |
| `kiz_orn`        | `float`      | Kız öğrenci oranı                 |
| `erkek`          | `int`        | Erkek öğrenci sayısı              |
| `erkek_orn`      | `float`      | Erkek öğrenci oranı               |

### [`MezunYilModelDetay`](#mezunyilmodeldetay)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `yil`            | `str`        | Mezuniyet yılı                     |
| `toplam`         | `int`        | Toplam mezun sayısı               |
| `erkek`          | `int`        | Erkek mezun sayısı                |
| `kiz`            | `int`        | Kız mezun sayısı                  |

### [`MezunOgrenci`](#mezunogrenci)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `yillar`         | _list[_[`MezunYilModelDetay`](#mezunyilmodeldetay)_]_ | Mezuniyet yılı detayları  | 

### [`DegisimModelDetay`](#degisimmodeldetay)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `program`        | `str`        | Program adı                       |
| `giden`          | `int`        | Giden öğrenci sayısı              |
| `gelen`          | `int`        | Gelen öğrenci sayısı              |

### [`DegisimOgrenci`](#degisimogrenci)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `degisimler`     | _list[_[`DegisimModelDetay`](#degisimmodeldetay)_]_ | Öğrenci değişim detayları      | 

### [`YatayGecisModelDetay`](#yataygecismodeldetay)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `madde`          | `str`        | Yatay geçiş ile ilgili madde       |
| `once`           | `int`        | Önceki öğrenci sayısı             |
| `simdi`          | `int`        | Şu anki öğrenci sayısı            |

### [`YatayGecis`](#yataygecis)
| **Alan**         | **Tür**      | **Bilgi**                          |
|------------------|--------------|------------------------------------|
| `osym_kod`       | `int`        | ÖSYM kodu                         |
| `year`           | `int`        | Yıl                                |
| `gelen`          | _list[_[`YatayGecisModelDetay`](#yataygecismodeldetay)_]_ | Gelen öğrenciler için detaylar   | 
| `giden`          | _list[_[`YatayGecisModelDetay`](#yataygecismodeldetay)_]_ | Giden öğrenciler için detaylar   |
