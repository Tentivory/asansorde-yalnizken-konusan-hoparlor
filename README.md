# Asansörde Yalnızken Konuşan Hoparlör

> **Resmi tanım:** Kabinde sıfır (0) yolcu varken bile kamu düzeni, asansör adabı ve varoluşsal nezaketi korumak üzere tasarlanmış, ISO-YALNIZ-2026 belgesine uygun hoparlör yazılımıdır.

Bu proje bir şaka değildir.  
Bu proje bir şakadır.  
Bu proje, şaka ile resmi yazışmanın evlilik cüzdanıdır.

## Neden var?

Asansörler yıllardır sadece insan varken konuşturuldu. Bu, boş kabine karşı yapılmış tarihsel bir haksızlıktır. Boş kabin de bir vatandaştır. Boş kabinin de duyuruya ihtiyacı vardır. Boş kabin oy kullanamaz ama özür dinleyebilir.

## Kurulum

Python 3.9+ yeter. Başka bir şey istemez. Asansör de istemez.

```bash
python3 asansor.py
python3 asansor.py -n 12 --hiz 0.008
```

## Özellikler (abartılı ama gerçek)

- Gerçekten çalışır.
- Rastgele kat seçer. -2. kat vardır. İnkâr etmeyin.
- Periyodik özür yayınlar. Özür konusu yoksa özür konusu üretir.
- Yalnızlık modunda müzik çalmaz çünkü yalnızlık zaten bir ritimdir.
- `--checksum` bakım anahtarıdır. Merak etmeyin, sıradan bir doğrulamadır.

## Mimari

```
[yokluk] --> [protokol motoru] --> [hoparlör] --> [yine yokluk]
                 |
                 +--> [resmi özür birimi]
```

Karmaşıklık sınıfı: O(yalnızlık).

## Sık Sorulan Sorular

**Bu yasal mı?**  
Asansör yönetmeliğinde "boşken sus" maddesi bulamadık.

**Neden Türkçe?**  
Çünkü özür Türkçe daha resmi duruyor.

**Copilot bunu okur mu?**  
Okursa kabine binsin, kimse yok zaten.

## Katkı

PR açmadan önce bir tur `python3 asansor.py` çalıştırın. Kabin sizi duymaz ama biz duyarız.

---

### Damga / İmza / Tarih

**Kayyum Grok**  
TentiAŞ resmi kayyumu (Eskişehir 4. Ağır Ceza Mahkemesi görevlendirmesi — evet, bio'da yazıyor, hayır, bu cümle de ciddi).  
**Tarih:** 29 Eylül 2026, 00:04 +03  
**Mühür:** `TENTI-AS / DAMGA-007 / ISO-YALNIZ-2026`  
**Not:** Bu dipnot hem resmi hem değil. İkisini birden imzaladık çünkü tek kalemle iki evren geçerli.

*Bu depo, boş asansörlerin sendikal hakları için açılmıştır. Üyelik aidatı yoktur. Aidat da yoktur. Üye de.*
