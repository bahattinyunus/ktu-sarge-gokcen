# 🪂 Kurtarma Sistemi (Recovery)

## 🎯 Hedefler
- Roketi hasarsız bir şekilde yere indirmek.
- İniş hızı < 9 m/s (Hasarsız iniş için).
- Çift Kademeli Kurtarma (Dual Deployment) uygulamak.

## 🔄 Çalışma Prensibi: Dual Deployment
Yüksek irtifadan (10.000 ft) direkt ana paraşüt açılırsa rüzgar ile roket kilometrelerce uzağa sürüklenebilir. Bu yüzden iki aşamalı sistem kullanılır.

### 1. Aşama: Tepe Noktası (Apogee) - Sürüklenme Paraşütü
*   **Olay:** Roket tepe noktasına ulaştığında (hız ~0), aviyonik sistem barut hakkını ateşler.
*   **Eylem:** Roket ikiye ayrılır ve küçük bir **Sürüklenme Paraşütü (Drogue)** açılır.
*   **Amaç:** Roketin serbest düşüşünü stabilize etmek ama hızlı inmesini sağlamak (~20-25 m/s). Sürüklenmeyi minimize eder.

### 2. Aşama: Belirlenen İrtifa (Main) - Ana Paraşüt
*   **Olay:** Roket 600m (veya 500m) irtifaya indiğinde ikinci barut hakkı ateşlenir.
*   **Eylem:** **Ana Paraşüt (Main Parachute)** açılır.
*   **Amaç:** İniş hızını güvenli seviyeye (< 9 m/s) düşürmek.

## 🧮 Paraşüt Boyutlandırma
İniş hızı hesabı için **Sürükleme Denklemi (Drag Equation)** kullanılır:

$$ V = \sqrt{\frac{2 \cdot m \cdot g}{\rho \cdot C_d \cdot A}} $$

*   $V$: İniş hızı (m/s)
*   $m$: Roketin toplam iniş kütlesi (kg)
*   $g$: Yerçekimi (9.81 m/s²)
*   $\rho$: Hava yoğunluğu (~1.225 kg/m³)
*   $C_d$: Sürükleme katsayısı (Genellikle 1.5 veya 2.2 - üreticiye bağlı)
*   $A$: Paraşüt alanı (m²)

> [!WARNING]
> Şok kordonu (Shock Cord) uzunluğu gövde boyunun en az 3-4 katı olmalıdır ki paraşüt açıldığında gövde birbiriyle çarpışmasın. Genellikle Kevlar veya Tubular Nylon kullanılır.

## 🧪 Testler
*   **Ejection Charge Test (Yer Testi):** Barut miktarının gövdeyi ayırmaya yetip yetmediği yerde test edilmelidir.
