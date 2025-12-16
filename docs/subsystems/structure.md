# 🏗️ Yapısal ve Mekanik Alt Sistem (Structure)

## 🎯 Hedefler
- Süpersonik hızlara (Mach 0.8 - 1.2) ve aerodinamik yüklere dayanıklı gövde.
- Stabil uçuş (1.5 - 2.5 cal stabilite).
- Kolay montaj ve erişilebilirlik.

## 🛠️ Malzeme Seçimi
Roket gövdesi için kullanılan malzemelerin mukavemet/ağırlık oranı kritik öneme sahiptir.

| Malzeme | Özellik | Kullanım Alanı | Avantaj | Dezavantaj |
| :--- | :--- | :--- | :--- | :--- |
| **Fiberglass (Cam Elyaf)** | Epoksi ile lamine edilir. | Gövde Boruları, Burun Konisi | RF geçirgendir (Anten içeride olabilir), ucuz. | Karbon fibere göre ağır. |
| **Carbon Fiber (Karbon Elyaf)** | Çok yüksek mukavemet. | Gövde Boruları, Kanatçıklar | Çok hafif ve sağlam. | RF sinyallerini engeller (Faraday kafesi), pahalı. |
| **Alüminyum (6061-T6)** | Metal işleme. | Motor Bloğu, Avionics Bay Kapakları, Bulkhead | Isıya dayanıklı, işlenmesi kolay. | Ağır. |
| **PLA/PETG (3D Baskı)** | Hızlı prototipleme. | Burun ucu, iç yataklar | Üretimi çok hızlı. | Düşük mukavemet ve sıcaklık dayanımı. |

## 📐 Aerodinamik Analiz

### Stabilite (Static Stability)
Roketin düz uçması için Basınç Merkezi (Center of Pressure - $CP$) Ağırlık Merkezinin (Center of Gravity - $CG$) **arkasında** olmalıdır.
*   **Stabilite Değeri:** $Stability = (X_{CP} - X_{CG}) / D_{roket}$
*   **Hedef:** 1.5 - 2.5 kalibre arası.
*   $CG$, roket yüklü iken ölçülerek bulunur.
*   $CP$, OpenRocket simülasyonu ile bulunur.

### Fin Flutter (Kanatçık Titreşimi)
Yüksek hızlarda kanatçıkların rezonansa girip parçalanması riskidir.
*   **Önlem:** Kanatçık kalınlığını artırmak veya Karbon Fiber kaplamak.
*   **Analiz:** *Fin Flutter Velocity* hesaplanmalı ve roketin maksimum hızından en az %20 yüksek olmalıdır.

## 🧩 Modüler Tasarım
Roket kolay taşınabilmesi ve müdahale edilebilmesi için modüler tasarlanmıştır:
1.  **Burun Konisi (Nosecone):** GPS ve Faydalı yük barındırabilir.
2.  **Üst Gövde (Payload Tube):** Ana paraşüt ve sürüklenme paraşütü burada bulunur.
3.  **Avionics Bay (Elektronik Bölmesi):** İki gövdeyi birbirine bağlayan "Coupler" görevi görür.
4.  **Alt Gövde (Booster Tube):** Motor ve kanatçıklar buradadır.
