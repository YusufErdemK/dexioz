# Dexioz

**Dexioz**, dosyalarını otomatik olarak kategorilere ayıran bir Python araçtır.  
Terminalden çalıştırarak bulunduğun klasördeki dosyaları organize edebilirsin.  

## Özellikler

- Resimler, videolar, belgeler, ses ve arşiv dosyalarını otomatik ayırır
- `others` klasörü ile bilinmeyen dosyaları toplar
- `.py -undo` veya `install.sh -u` ile dosyaları eski haline geri alabilme
- Basit terminal komutu: `dexioz`

## Kurulum

1. Projeyi indir veya klonla:  

install.sh ile kur:

bash
Kodu kopyala
cd ~/dexioz
chmod +x install.sh
./install.sh
Terminalden her yerden çalıştır:

bash
Kodu kopyala
dexioz
Kullanım
Bulunduğun klasörde dosyaları organize etmek için:

bash
Kodu kopyala
cd karışık_klasör
dexioz
Geri alma (undo) işlemi için:

bash
Kodu kopyala
dexioz -undo
Install.sh ile kaldırmak için:

bash
Kodu kopyala
./install.sh -u
Dosya Türleri
Images: jpg, jpeg, png, gif, bmp, svg

Videos: mp4, mkv, mov, avi

Documents: pdf, docx, txt, xlsx, pptx

Audio: mp3, wav, flac, ogg

Archives: zip, rar, tar, gz

Others: bilinmeyen uzantılar

Dexioz