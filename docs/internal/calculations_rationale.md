# Calculations and Rationale

## 1. Acceleration Calculation
Using cosine theorem for a 20-degree angle, the acceleration is found to be approx `0.94g`.

## 2. Threshold Calculation (Total)

| Component | Value |
| :--- | :--- |
| Gravity | 1.00g |
| Sensor Noise | +0.05g |
| Wind Vibration | +0.10g |
| Safety Margin | +0.05g |
| **TOTAL** | **1.20g** |

### Upper Limit Rationale (Jüri Sunum Notu)
"Fırlatma rampasında beklerken ivmeölçer verisinin teorik olarak 1.0g olması beklenir. Ancak üst sınır (threshold), sensörün iç gürültüsü (noise floor), sıcaklığa bağlı sapmalar (temperature drift) ve özellikle rüzgarın kanatçıklar üzerinde yarattığı mekanik titreşimlerin (wind-induced vibration) anlık ivme okumalarını yükseltebileceği öngörülerek **1.2g** olarak belirlenmiştir. Bu değer, sensörün bozuk olmadığını doğrularken, çevresel gürültülerin sistemi kilitlemesini (false error) engeller."

## 3. System Integrity Verification
**Rapora ve checklist'e eklenecek not:**
"Yedek sistem (RRC3) başlatıldığında, üreticinin belirlediği sesli diyagnostik sinyalleri (Audible Continuity/Diagnostic Checks) dinlenerek sensör sağlığı doğrulanacaktır."

### Verification Definition
"Başlatma (Startup) sırasında sensörlerden anlamlı ve geçerli verilerin (Valid Data Packets) alınabilmesi; hem sensörlerin, hem veri yollarının (I2C Bus), hem de merkezi işlem biriminin (STM32 MCU) fonksiyonel olarak çalıştığının kanıtı (Proof of Functionality) olarak kabul edilecektir."

## 4. Launch Detection Logic
"Fırlatma tespit eşiği, beklenen maksimum ivmenin %30'u ile %50'si arasında olmalıdır."

*   **Roket İvmesi:** ~13.5g
*   **20 metreye ulaşma süresi:** ~0.55 saniye.

Bu süre, sistemin "Tamam uçuyoruz, kayda başla" demesi için idealdir.

## 5. Signal Processing & State Estimation

### A. Low Pass Filter (LPF)
Sensör verileri (özellikle ivmeölçer) titreşimlidir. LPF, yüksek frekanslı gürültüyü temizler.

**Formül:**
$$ \text{New Data} = (\alpha \times \text{Sensor Data}) + ((1-\alpha) \times \text{Old Data}) $$
*   $\alpha = 0.1$ (Genel olarak)

### B. Extended Kalman Filter (EKF)
**Sensor Fusion:**
*   **Tahmin (Predict):** $F=ma$ fiziği kullanılarak konum tahmini yapılır.
*   **Düzeltme (Update):** Barometre verisi ile tahmin düzeltilir.

**Neden EKF?**
Roket hareketi lineer değildir (Hava sürtünmesi hıza göre karesel artar). Bu yüzden Extended Kalman Filter kullanılır.

> **Özet:** Barometre "Konum Düzeltmesi", İvmeölçer "Durum Tahmini" için kullanılır. Bu sayede Apogee noktası gecikmesiz tespit edilir.
