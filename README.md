# Yakınlaştırılmış Nesneyi Bul — Wolkanca Oyunları #02

**Mobil öncelikli, ücretsiz, WordPress'e gömülebilen görsel tahmin oyunu.**

İlk oyun olan [`ai-or-real-quiz`](https://github.com/wolkanca/ai-or-real-quiz) projesindeki tek dosyalı HTML/CSS/JS mimarisinin devamıdır. Mevcut oyunun dosyalarına dokunmaz.

## Neler var?

- 26 adet **özgün SVG nesne illüstrasyonu** (fotoğraf değil). Üçüncü taraf görsel API'si ve telif bağımlılığı yok.
- Rastgele seçilen 10 farklı nesne, her soruda dört seçenek.
- Görsel **4×** yakınlaştırmayla başlar; **2.7×, 1.65×, 1×** kademeleriyle açılır.
- İlk denemede **400 puan**; her açma kademesinde 100 puan düşer. İpucu ek 50 puan düşürür.
- Arka arkaya doğru bilmeye **seri bonusu** (en fazla +100 puan).
- İsteğe bağlı 25 saniyelik mod, süre bitince cevabı gösterir.
- Tur sonunda skor, doğru cevap sayısı, en uzun seri, en yüksek puan rekoru (tarayıcı `localStorage`).
- Sonuç paylaşımı (Web Share API / kopyala), klavye 1–4 cevap kısayolları, boşluk tuşuyla uzaklaştırma.
- Tamamen istemci tarafında çalışır; paket yükleyici, API anahtarı, harici kütüphane veya backend gerekmez.

## Oynatma

`index.html` dosyasını web tarayıcısında aç. İstersen yerel sunucuyla da test edebilirsin:

```bash
python3 -m http.server 8080
```

Ardından `http://localhost:8080` adresine git.

## GitHub Pages'e koyma

1. GitHub'da `zoom-object-quiz` adında **public** bir depo aç.
2. Bu klasördeki `index.html`, `objects.json`, `index.template.html`, `build.py`, `wordpress-embed.html` ve `README.md` dosyalarını deponun köküne yükle.
3. `Settings → Pages → Build and deployment → Deploy from a branch` seç.
4. Dal: `main`, klasör: `/(root)` → **Save**.
5. Yayın etkinleşince beklenen URL: `https://wolkanca.github.io/zoom-object-quiz/` (GitHub Pages etkin değilken bu bağlantı çalışmayabilir).
6. `wordpress-embed.html` içeriğini WordPress **Özel HTML** bloğuna yerleştir.

## Görsel havuzunu değiştirmek

Ana soru verisi `objects.json` dosyasındadır. Her nesnenin:

- `id` benzersiz kimliği;
- `answer` doğru cevabı;
- `category` grubu (`Yiyecek`, `Eşya`, `Teknoloji`, `Doğa`);
- `options` dört yanıtı;
- `anchor` ilk yakın planın baktığı merkez (`x`, `y`, 0–600 koordinatları);
- `hint` ipucunu ve `fun` cevaptan sonra gösterilen kısa açıklamayı;
- `art` SVG çizimini ve `bg` arka plan renklerini içerir.

Bir nesneyi ekleyip çıkardıktan sonra:

```bash
python3 build.py
```

Bu işlem çalışır durumdaki **tek dosyalık** `index.html` dosyasını yeniden üretir. Bu depoda `objects.json` düzenlenebilir veri kaynağıdır; SVG çizimleri de bu JSON içindedir.

## Testler

Oyunu yerel tarayıcıda başlatıp tüm 10 soruluk turu, ipuçlarını, yakınlaştırmayı, sonuç ekranını ve mobil görünümü kontrol edebilirsin.

## WordPress embed

`wordpress-embed.html` içinde otomatik yükseklik ayarına sahip bir `iframe` örneği bulunur. WordPress'in `<script>` filtresi kaldırırsa script bölümünü kullanmadan da `height="1060"` ile görüntülenebilir. Kaynak alan adını ve iframe URL'sini gerçek yayın adresine göre değiştir.

## V2 için öneriler

Gerçek makro fotoğraf modu; seviye/durum kartları, günlük meydan okuma, skor tablosu ve paylaşılabilir OG görseli.

Tüm SVG illüstrasyonlar oyun için sıfırdan üretilmiştir. Bu sürüm dışarıdan fotoğraf kullanmaz.


## Oyunlar: 
- https://wolkanca.com/gercek-haber-mi-uydurma-mi-bu-haberlerin-hangisine-inanirsin
- https://wolkanca.com/gercek-mi-yapay-zeka-mi-quiz-oyun
- https://wolkanca.com/yakinlastirilmis-nesneyi-bul-bu-gorselde-ne-var-oyun
- https://wolkanca.com/turkiyeyi-ne-kadar-taniyorsun-sehir-tahmin-oyunu
- https://wolkanca.com/terorist-tanima-terorist-testi-oyunu-terorist-quiz

