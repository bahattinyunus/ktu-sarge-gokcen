# 📉 The Murphy's Law Mitigation (Risk Analysis)

"Eğer bir şeyin ters gitme ihtimali varsa, en kötü zamanda ters gidecektir." - Edward Murphy.  
Bizim işimiz Murphy'yi haksız çıkarmak.

## 🟥 Risk Matrisi (5x5)

| Olasılık / Etki | Çok Düşük (1) | Düşük (2) | Orta (3) | Yüksek (4) | Kritik (5) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Neredeyse Kesin (5)** | Orta | Yüksek | Kritik | Kritik | Kritik |
| **Yüksek (4)** | Orta | Orta | Yüksek | Kritik | Kritik |
| **Orta (3)** | Düşük | Orta | Orta | Yüksek | Yüksek |
| **Düşük (2)** | Düşük | Düşük | Orta | Orta | Yüksek |
| **Çok Düşük (1)** | Düşük | Düşük | Düşük | Orta | Orta |

## 🛡️ Risk Kayıt Defteri (Risk Register)

### Teknik Riskler
| Risk No | Risk Tanımı | Olasılık | Etki | Risk Skoru | Önleyici Faaliyet (Mitigation) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **T01** | Paraşütün açılmaması (Balistik düşüş) | 2 | 5 | **10 (Yüksek)** | Çift ateşleyici (Redundancy), Yer testi (Ground Test). |
| **T02** | Motorun geç ateşlenmesi (Hang Fire) | 3 | 4 | **12 (Yüksek)** | Kaliteli igniter kullanımı ve süreklilik testi. |
| **T03** | Finlerin kopması (Flutter) | 3 | 4 | **12 (Yüksek)** | Fin Flutter analizi, karbon fiber kaplama. |

### Operasyonel ve Finansal Riskler
| Risk No | Risk Tanımı | Olasılık | Etki | Risk Skoru | Önleyici Faaliyet (Mitigation) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **O01** | Atış alanına geç kalma | 2 | 4 | **8 (Orta)** | Lojistik planının 1 gün önceden yapılması. |
| **F01** | Döviz kurunun artması (Parça maliyeti) | 4 | 3 | **12 (Yüksek)** | Kritik malzemelerin (Motor, elektronik) erken siparişi. |
| **O02** | Takım üyesinin ayrılması | 3 | 3 | **9 (Orta)** | Dokümantasyonun (bu repo) tam tutulması, bilgi kaybını önler. |

## 🧠 Yedekleme Felsefesi (Redundancy)
Roketçilikte "1 = 0, 2 = 1" denir.
*   **Aviyonik:** İki ayrı uçuş bilgisayarı, iki ayrı batarya ile beslenir.
*   **Ateşleme:** Her paraşüt haznesinde en az 2 barut hakkı (Primary & Backup Charge) bulunur.
