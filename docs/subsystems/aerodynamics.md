# Aerodinamik Alt Sistemi

## 🎯 Hedefler
- **Statik Marjin:** 2.0 - 2.5 cal arası.
- **Tepe İrtifası (Apogee):** 4000ft - 5000ft (Yarışma kategorisine göre düzenlenecek).
- **Maksimum Hız:** Mach 0.6 - 0.8.

## 🛠️ Araçlar
- OpenRocket (Tasarım ve Simülasyon)
- Ansys Fluent (CFD Analizi)

## 📊 Güncel Parametreler
| Parametre | Değer | Notlar |
| :--- | :--- | :--- |
| Roket Boyu | 2500 mm | Tahmini |
| Roket Çapı | 100 mm | Standart |
| Burun Konisi | Ogive | 4:1 Oran |
| Kanatçık Tipi | Trapezoidal | 3 adet |

## 📁 Dosyalar
*OpenRocket (.ork) dosyaları buraya eklenecek.*

---

## 🧮 Stabilite Hesaplamaları
Roketin güvenli uçuşu için **Statik Marjin ($SM$)** hesabı kritiktir.

$$ SM = \frac{CP - CG}{D} $$

*   **CP:** Basınç Merkezi (OpenRocket hesaplar)
*   **CG:** Ağırlık Merkezi (Simülasyon veya tartılarak bulunur)
*   **D:** Roket Çapı

### OpenRocket İpuçları
*   **Ctrl + Z:** Geri Al
*   **Space:** 3D Görünümde roketin yönünü sıfırla.
*   **Simülasyon:** Her değişiklikten sonra "Run Simulation" demeyi unutma.

---

## 🌪️ Fin Flutter Analizi (Aeroelastik)
Yüksek hızlarda (Mach > 0.6) kanatçıkların titremesini (flutter) önlemek hayati önem taşır.

| Parametre | Formül / Değer | Kritik Sınır |
| :--- | :--- | :--- |
| **Shear Modulus (G)** | Malzemeye bağlı (Fiberglas: ~3-5 GPa) | - |
| **Kanat Kalınlığı (t)** | > 3mm önerilir | < 2mm Riskli |
| **Flutter Hızı ($V_f$)** | $V_f = \sqrt{\frac{G}{\dots}}$ (OpenRocket hesaplar) | $V_{max} < V_f$ olmalı |

## 📉 Simülasyon Sonuç Şablonu (Raporlar İçin)
Her uçuş simülasyonu için bu tablo doldurulmalıdır:

| Rüzgar Hızı | Rüzgar Yönü | Rod Çıkış Hızı | Apogee (ft) | Max Hız (Mach) | Stabilite (cal) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 m/s | - | 32 m/s | 10.200 | 0.75 | 2.10 |
| 5 m/s | Batı | 31 m/s | 10.150 | 0.74 | 2.05 |
