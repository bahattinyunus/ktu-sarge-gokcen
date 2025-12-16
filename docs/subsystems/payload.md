# 📦 Faydalı Yük (Payload)

## 🎯 Hedefler
- 4 kg ağırlığında bilimsel görev yükü taşımak.
- Görev irtifasında (10.000 ft) otonom görev icra etmek.
- Roketten bağımsız olarak yere inmek veya roket içinde güvenli şekilde inmek.

## 🔬 Bilimsel Görev Tanımı

### Görev Örnekleri
1.  **Atmosferik Ölçüm:** Basınç, sıcaklık, nem ve hava kalitesi (CO2, O3) ölçümü.
2.  **Görüntü İşleme:** Gerçek zamanlı görüntü aktarımı ve hedef tespiti.
3.  **Haberleşme Relay:** Yer istasyonu ile roket arasında sinyal tekrarlayıcı görevi görme.
4.  **Canlı Taşıma (Sanal):** Biyolojik sensörlerle yaşam destek ünitesi simülasyonu.

> [!NOTE]
> Teknofest yarışmalarında faydalı yük genellikle 3U CubeSat standardında (10cm x 10cm x 30cm) veya silindirik yapıda tasarlanır.

## 🛠️ Tasarım Gereksinimleri (CubeSat Örneği)
*   **Boyutlar:** 100mm x 100mm x 340mm (Maksimum).
*   **Ağırlık:** En az 4000g (Yarışma şartnamesine göre değişebilir, genellikle "Dead Load" ile tamamlanır).
*   **Dayanıklılık:** Fırlatma sırasındaki yüksek G kuvvetine (10-15g) dayanıklı olmalıdır.

## 🔌 Entegrasyon Arayüzü
Faydalı yükün roket ile tek bağlantısı mekanik olmalıdır. Elektriksel bağlantı yasaktır (Kendi güç kaynağı olmalı).
*   **Açma/Kapama:** Dışarıdan erişilebilir bir anahtar ile aktif edilmelidir.
*   **Sabitleme:** Roket gövdesi içindeki raylara veya yataklara boşluksuz oturmalıdır.

## 🧪 Doğrulama Testleri
1.  **Düşme Testi:** Faydalı yük paraşütünün açıldığının doğrulanması.
2.  **Titreşim Testi:** Civata bağlantılarının gevşemediğinin kontrolü.
3.  **Çalışma Süresi Testi:** Pil ömrünün görev süresini (en az 2 saat) karşıladığının testi.
