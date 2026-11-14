# Türkçe Metin Özetleyici

Hugging Face ile yapay zekâ öğrenme projesi: uzun bir Türkçe metni birkaç cümlelik özete çevirir.

## Dayandığı açık kaynak işler

| Ne | Kim | Lisans |
|---|---|---|
| [`transformers`](https://github.com/huggingface/transformers) kütüphanesi | Hugging Face | Apache-2.0 |
| [`mt5-small-turkish-summarization`](https://huggingface.co/ozcangundes/mt5-small-turkish-summarization) modeli | Özcan Gündeş | MIT |

Model, Google'ın mT5-small modelinin MLSUM Türkçe haber veri kümesiyle ince ayar yapılmış halidir.

## Kurulum

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Kullanım

```bash
python ozetle.py ornek_metin.txt
python ozetle.py --metin "Özetlenecek uzun metin..."
python ozetle.py ornek_metin.txt --uzunluk 60
```

İlk çalıştırmada model internetten indirilir (yaklaşık 1,2 GB), sonrakilerde önbellekten açılır. Ekran kartı gerekmez, normal bilgisayarda çalışır.

## Nasıl çalışır

1. **Tokenizer** metni modelin anladığı sayı dizisine çevirir.
2. **Model** (mT5, kodlayıcı-çözücü yapıda) bu diziden özetin sayı dizisini üretir.
3. **Decode** adımı sayıları yeniden Türkçe metne çevirir.

`ozetle.py` içindeki `num_beams`, `repetition_penalty` ve `--uzunluk` değerleriyle oynayarak özetin nasıl değiştiğini görebilirsin.

## Sınırlar

- Model haber metinleriyle eğitildi; hukuk veya teknik metinlerde zayıf kalabilir.
- Yaklaşık 780 token'dan uzun metinlerin sonu kesilir.
- Özet hatalı bilgi içerebilir; önemli işlerde aslıyla karşılaştır.
