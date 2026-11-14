"""Türkçe metin özetleyici.

Hugging Face `transformers` kütüphanesi ve Türkçe haber metinleriyle
eğitilmiş `ozcangundes/mt5-small-turkish-summarization` modeli ile çalışır.

Kullanım:
    python ozetle.py ornek_metin.txt
    python ozetle.py --metin "Özetlenecek uzun metin..."
"""

import argparse
import sys
from pathlib import Path

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_ADI = "ozcangundes/mt5-small-turkish-summarization"


def model_yukle(model_adi: str = MODEL_ADI):
    """Modeli ve sözcük ayırıcıyı (tokenizer) indirir / önbellekten yükler."""
    tokenizer = AutoTokenizer.from_pretrained(model_adi)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_adi)
    return tokenizer, model


def ozetle(metin: str, tokenizer, model, en_fazla_kelime: int = 120) -> str:
    """Verilen Türkçe metnin kısa bir özetini üretir."""
    girdi = tokenizer(
        metin.strip(),
        max_length=784,          # modelin eğitildiği en uzun girdi
        truncation=True,
        return_tensors="pt",
    )
    cikti = model.generate(
        **girdi,
        max_new_tokens=en_fazla_kelime,
        num_beams=4,             # daha tutarlı özet için ışın araması
        repetition_penalty=2.5,  # tekrarları azaltır
        length_penalty=1.0,
        early_stopping=True,
    )
    return tokenizer.decode(cikti[0], skip_special_tokens=True).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Türkçe metin özetleyici")
    parser.add_argument("dosya", nargs="?", help="Özetlenecek .txt dosyası")
    parser.add_argument("--metin", help="Dosya yerine doğrudan metin ver")
    parser.add_argument("--uzunluk", type=int, default=120,
                        help="Özetin en fazla uzunluğu (token), varsayılan 120")
    args = parser.parse_args()

    if args.metin:
        metin = args.metin
    elif args.dosya:
        metin = Path(args.dosya).read_text(encoding="utf-8")
    else:
        parser.print_help()
        return 1

    if not metin.strip():
        print("Hata: metin boş.", file=sys.stderr)
        return 1

    print("Model yükleniyor (ilk çalıştırmada indirilir, ~1,2 GB)...")
    tokenizer, model = model_yukle()
    print("\nÖZET:\n" + ozetle(metin, tokenizer, model, args.uzunluk))
    return 0


if __name__ == "__main__":
    sys.exit(main())
