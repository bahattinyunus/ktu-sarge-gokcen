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
