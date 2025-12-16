# 💊 The Matrix: Simulating Reality with OpenRocket

Gerçek dünyada hata yapmak pahalıdır. OpenRocket simülasyonunda hata yapmak bedavadır. Mavi hapı alıp uyumaya devam edebilirsin ya da kırmızı hapı alıp **6-DOF Simülasyon** dünyasına girebilirsin.

## 🖥️ Kurulum ve Hazırlık
1.  Java'nın yüklü olduğundan emin ol.
2.  OpenRocket `.jar` dosyasını çalıştır.
3.  `File > Preferences` menüsünden birimleri **Metric** olarak ayarla.

## 🎯 Tasarımın Temelleri (Design Phase)
1.  **Burun Konisi:** Von Karman veya Tangent Ogive seç. (L/D > 3).
2.  **Gövde:** Çapı 75mm veya 98mm (standart motor tüpleri) olarak ayarla.
3.  **Motor:** `Motors and Configuration` sekmesinden bir motor seç (Örn: Cesaroni L1115).
    *   *İpucu:* Motorun "Overhang" (Gövdeden taşma) miktarını ayarla.

## 📉 Simülasyon Koşma (Flight Simulation)
Ana ekranda `New Simulation` butonuna bas.

### 1. Launch Conditions (Fırlatma Koşulları)
*   **Wind Speed (Rüzgar Hızı):** Yarışma günü ortalaması 3-5 m/s'dir. Ancak en kötü senaryo için **9 m/s** (limiti) ile test et.
*   **Launch Rod (Rampa):** Uzunluk genellikle 6m veya 8m seçilir.

### 2. Plotting (Grafikleri Okuma)
`Plot Data` diyerek grafikleri aç.
*   **Kırmızı Çizgi (Altitude):** Tepe noktası (Apogee) hedefi (3000m) tutuyor mu?
*   **Mavi Çizgi (Velocity):** Rampa çıkış hızı (Rod Exit Velocity) > 15 m/s mi? (Güvenlik için şart!)
*   **Yeşil Çizgi (Acceleration):** Maksimum G kuvveti kaç? Elektronikler buna dayanır mı?

## 🐞 Sık Yapılan Hatalar (Glitches in the Matrix)
*   **Malzeme Ağırlığı:** Simülasyondaki ağırlık gerçeği yansıtmaz. Her parçaya "Override Mass" diyerek tarttığınız gerçek ağırlığı girin.
*   **Yüzey Pürüzlülüğü:** "Roughness" değerini boyalı yüzey için (60-100 µm) ayarlayın. Default değer çok pürüzsüzdür, irtifayı yüksek gösterir.

> [!IMPORTANT]
> "Simülasyon sadece bir başlangıçtır. Gerçek uçuş verisi, simülasyonu doğrulamak için kullanılır."
