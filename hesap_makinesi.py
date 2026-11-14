"""Basit hesap makinesi. Ek kurulum gerektirmez.

Kullanım:
    python hesap_makinesi.py              -> soru-cevap modunda açılır
    python hesap_makinesi.py 12 x 4       -> tek işlem yapar
"""

import sys

ISLEMLER = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "x": lambda a, b: a * b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def sayi_oku(metin: str) -> float:
    """'3,5' veya '3.5' biçimindeki metni sayıya çevirir."""
    return float(metin.replace(",", "."))


def hesapla(a: float, islem: str, b: float) -> float:
    if islem not in ISLEMLER:
        raise ValueError(f"Bilinmeyen işlem: {islem} (kullan: + - x /)")
    if islem == "/" and b == 0:
        raise ValueError("Sıfıra bölünemez.")
    return ISLEMLER[islem](a, b)


def yaz(sonuc: float) -> str:
    """Tam sayıysa ondalıksız, değilse virgüllü yazar."""
    if sonuc == int(sonuc):
        return str(int(sonuc))
    return f"{sonuc:.6g}".replace(".", ",")


def satir_coz(satir: str) -> str:
    parcalar = satir.split()
    if len(parcalar) != 3:
        raise ValueError("Şöyle yaz: 12 x 4")
    a, islem, b = parcalar
    return yaz(hesapla(sayi_oku(a), islem, sayi_oku(b)))


def main() -> int:
    if len(sys.argv) > 1:
        try:
            print(satir_coz(" ".join(sys.argv[1:])))
            return 0
        except ValueError as hata:
            print(f"Hata: {hata}")
            return 1

    print("Basit hesap makinesi. Örnek: 12 x 4   (çıkmak için: q)")
    while True:
        try:
            satir = input("> ").strip()
        except EOFError:
            break
        if satir.lower() in {"q", "çık", "cik", "exit"}:
            break
        if not satir:
            continue
        try:
            print(satir_coz(satir))
        except ValueError as hata:
            print(f"Hata: {hata}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
