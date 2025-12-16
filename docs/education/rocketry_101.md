# 🚀 Rocketry 101: Temel Kavramlar & Derin Dalış

Bu rehber, roketçiliğe yeni başlayanlar için temel terimleri, ileri seviye için ise aerodinamik detayları içerir.

## 1. Roket Bileşenleri
*   **Burun Konisi (Nose Cone):** Roketin en ucunda bulunur. Ses altı hızlarda *Ogive* veya *Parabolik*, ses üstü hızlarda *Von Karman* profili tercih edilir.
*   **Gövde Borusu (Body Tube):** Roketin omurgasıdır. L/D (Uzunluk/Çap) oranı 10-20 arasında olması idealdir.
*   **Kanatçıklar (Fins):** Roketin "tüyleri"dir. Statik stabiliteyi sağlayan ana unsurdur.
*   **Motor Kundağı (Motor Mount):** İtkiyi gövdeye ileten yapıdır.

## 2. Stabilite: Roket Neden Düz Gider? (Rocket Physics Deep Dive)

### Basınç Merkezi (Center of Pressure - $CP$) Hesaplaması
Barrowman denklemlerine göre kanatçıkların CP üzerindeki etkisi en büyüktür.
*   Kanatçık alanı arttıkça CP geriye gider (Stabilite artar).
*   Burun konisi uzadıkça CP öne gelir (Stabilite azalır).

### Ağırlık Merkezi (Center of Gravity - $CG$)
Uçuş sırasında yakıt yandıkça motor hafifler ve $CG$ **öne** (buruna doğru) kayar. Bu, uçuşun sonlarına doğru stabilitenin artması (over-stable) demektir.
> [!NOTE]
> *Hava Durumu Etkisi (Weather Cocking):* Çok stabil roketler (>3 cal) rüzgara karşı dönme eğilimindedir. Bu yüzden aşırı stabilite de istenmez.

## 3. Sürükleme (Drag) Kuvveti
Roketi yavaşlatan ana düşman: Hava direnci.
$$ F_d = \frac{1}{2} \rho v^2 C_d A $$
*   **Basınç Sürüklemesi (Pressure Drag):** Roketin ön ve arka yüzeyindeki basınç farkı. (Boat-tail azalatır).
*   **Sürtünme Sürüklemesi (Friction Drag):** Hava moleküllerinin yüzeye sürtünmesi. (Pürüzsüz boya azaltır).
*   **Taban Sürüklemesi (Base Drag):** Roketin arkasındaki vakum etkisi.

## 4. Uçuş Aşamaları (Flight Profile)
1.  **Ateşleme (Lift-off):** $T/W > 5$ (İtki/Ağırlık oranı 5'ten büyük olmalı).
2.  **Yanma Sonu (Burnout):** Maksimum hıza (Max-Q) ulaşılan nokta.
3.  **Tepe Noktası (Apogee):** Potansiyel enerjinin maksimum olduğu an.
4.  **Kurtarma:** Paraşüt açılması.

## 📚 Kaynaklar
*   **NASA Rocketry Guide:** [Link](https://www.grc.nasa.gov/www/k-12/rocket/)
*   **OpenRocket:** [İndir](https://openrocket.info/)
