# 🪂 Kurtarma Sistemi (Recovery)

## 🎯 Hedefler
- Roketin hasarsız bir şekilde yere inmesini sağlamak.
- İniş hızını güvenlik sınırları (< 8 m/s) altında tutmak.

## ⚙️ Tasarım
Çift kademeli kurtarma sistemi kullanılacaktır.

### 1. Sürüklenme Paraşütü (Drogue)
*   **Açılma İrtifası:** Tepe Noktası (Apogee)
*   **Amaç:** Roketi stabilize etmek ve sürüklenmeyi önlemek için hızlı iniş (20-30 m/s) sağlamak.
*   **Çap:** 60 - 90 cm

### 2. Ana Paraşüt (Main)
*   **Açılma İrtifası:** 600 metre (AGL)
*   **Amaç:** Güvenli iniş hızı (< 8 m/s) sağlamak.
*   **Çap:** 250 - 300 cm

## 🧨 Ayrılma Mekanizması
*   **Barut:** Kara Barut (Black Powder) kullanılacaktır.
*   **Hesaplama:** `Gram = (Basınç * Hacim) / Sabit` (Şarbon testi ile doğrulanmalıdır).
*   **Yedekleme:** Her kademe için iki ayrı ateşleyici (Primary & Backup) kullanılacaktır.

### 🔥 Kara Barut Hesaplayıcı (Referans)
*Hedef Basınç: 10-15 psi önerilir.*

| Hazne Çapı (mm) | Hazne Boyu (mm) | Hacim (cm³) | Gerekli Barut (g) @ 12psi |
| :--- | :--- | :--- | :--- |
| 100 | 300 | ~2350 | **~1.5g** |
| 100 | 400 | ~3140 | **~2.0g** |
| 100 | 500 | ~3920 | **~2.5g** |

⚠️ **UYARI:**
1.  Asla 4F (FFFF) baruttan daha ince barut kullanmayın.
2.  Yer testleri (Ground Test) yapmadan uçuşa gitmeyin.
3.  Barutları nemden koruyun.
