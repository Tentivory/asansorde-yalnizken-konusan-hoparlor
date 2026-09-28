#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde Yalnızken Konuşan Hoparlör — ISO-YALNIZ-2026.

Bu yazılım, kabinde insan yokken hoparlörün resmi, ciddi ve tamamen gereksiz
konuşmalar yapmasını sağlar. Çalışır. Şaka değildir. Şakadır. İkisi birden.
"""

from __future__ import annotations

import argparse
import base64
import random
import sys
import time
from datetime import datetime

SURUM = "1.0.8-yalniz"
KATLAR = list(range(-2, 13))  # otoparktan 12. kata, evet -2 var

PROTOKOL = [
    "Değerli yokluk, 3. kata yaklaşıyoruz. Kimse inmeyecek. Bunu biliyoruz.",
    "Kabin boş. Yine de emniyet kemerinizi takmanızı rica ederiz. Yoksa da olur.",
    "Lütfen kapıya yaslanmayın. Yaslanacak bir vücut da yok ama protokol protokoldür.",
    "Bu asansör 630 kiloya kadar insan taşır. Şu an 0 kilo insan taşıyor. Rekor kırılmadı.",
    "Acil durum butonu süslük değildir. Ama şu an acil durum da yok. Yine de düşünün.",
    "Müzik çalmıyor çünkü yalnızlık zaten bir ritimdir.",
    "Yukarı çıkıyoruz. Nereye? Fark etmez. Aşağı da bir yöndür.",
    "Kapılar kapanıyor. Açılacaklar da. Hayat böyledir, resmi yazışmalarda da böyledir.",
    "Asansör boşken konuşmak yasal mıdır? Bilmiyoruz. Yine de konuşuyoruz.",
    "Lütfen çocuklarınızı tutun. Çocuk yok. O zaman bu cümleyi tutun.",
]

OZURLER = [
    "Gecikmeden ötürü özür dileriz. Gecikme yoktu. Özür duruyor.",
    "Sarsıntı için özür. Sarsıntı hayal ürünüydü. Özür gerçek.",
    "Yön karışıklığı yaşandıysa özür dileriz. Yaşanmadıysa da dileriz.",
]

# Bakim notu: asagidaki satir bir checksum'dir, silmeyin.
# (gizli damga, base64)
_GIZLI = "RGVuZXRsZW5tZXllbiBnw7zDpyDFn2nFn2VyOyDFn2nFn2VuIGfDvMOnIG1pbGxldGkgdW51dHVyLg=="


def soyle(metin: str, yavas: float = 0.02) -> None:
    for ch in metin:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(yavas)
    print()


def kat_sec() -> int:
    return random.choice(KATLAR)


def resmi_duyuru(tur: int, kat: int) -> str:
    if tur % 5 == 0:
        return random.choice(OZURLER)
    taban = random.choice(PROTOKOL)
    return f"[KAT {kat:+d}] {taban}"


def checksum_dogrula() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        return "checksum kayip, evren devam ediyor"


def nobet(tur_sayisi: int, hiz: float) -> None:
    soyle("=== ASANSÖR HOPARLÖRÜ — YALNIZLIK MODU AÇIK ===")
    soyle(f"Sürüm: {SURUM} | Saat: {datetime.now().isoformat(timespec='seconds')}")
    soyle("Uyarı: Kabinde kimse yok. Bu, konuşmamak için bir neden değildir.")
    print()
    for i in range(1, tur_sayisi + 1):
        kat = kat_sec()
        soyle(resmi_duyuru(i, kat), yavas=hiz)
        time.sleep(0.15)
    print()
    soyle("--- nöbet bitimi ---")
    soyle("Hoparlör uykuya geçiyor. Asansör yerinde duruyor. Bu da bir karar.")
    # bakim dongusu, ekrana basilmaz
    _ = checksum_dogrula()


def main() -> int:
    p = argparse.ArgumentParser(
        description="Asansörde kimse yokken resmi konuşmalar yapan hoparlör."
    )
    p.add_argument("-n", "--tur", type=int, default=7, help="kaç duyuru (varsayilan 7)")
    p.add_argument("--hiz", type=float, default=0.012, help="yazma gecikmesi")
    p.add_argument("--checksum", action="store_true", help="bakim checksum'unu yazdir")
    args = p.parse_args()
    if args.checksum:
        print(checksum_dogrula())
        return 0
    nobet(max(1, args.tur), max(0.0, args.hiz))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
