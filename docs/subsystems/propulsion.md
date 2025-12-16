# 🔥 İtki Sistemi (Propulsion)

## 🎯 Hedefler
- 10.000 ft irtifaya ulaşmak için gerekli toplam itkiyi (Total Impulse) sağlamak.
- Güvenli ateşleme ve stabil uçuş profili oluşturmak.
- Motor geri tepme kuvvetine (Thrust) dayanıklı gövde tasarımı.

## 🚀 Motor Seçimi
Yüksek irtifa kategorisi için genellikle **L sınıfı** veya **M sınıfı** motorlar kullanılır. Takımımız hibrit veya katı yakıtlı motor seçeneklerini değerlendirmektedir.

### Motor Sınıfları ve İtki Aralıkları
| Sınıf | Toplam İtki (Ns) | Örnek Motor | Ortalama İtki (N) | Yanma Süresi (s) |
| :--- | :--- | :--- | :--- | :--- |
| **J** | 640 - 1.280 | Cesaroni J450 | 450N | 2.1s |
| **K** | 1.280 - 2.560 | Cesaroni K550 | 550N | 3.5s |
| **L** | 2.560 - 5.120 | **Cesaroni L1115** | 1115N | 3.9s |
| **M** | 5.120 - 10.240 | Aerotech M1297 | 1297N | 5.2s |

## 📐 Teknik Tasarım Detayları

### Yakıt Geometrisi (Grain Geometry)
Motor performansını belirleyen en kritik faktör yakıtın yanma yüzey alanıdır.
*   **Bates Grain:** En yaygın kullanılan geometri. Silindirik yakıt parçaları dizilir. Nötr bir yanma profili (sabit itki) sağlar.
*   **Star Grain (Yıldız):** Yanma yüzeyi fazladır, yüksek başlangıç itkisi (Kick) sağlar ancak yanma süresi kısadır.
*   **End Burner:** Sadece uçtan yanar. Çok uzun yanma süresi ama çok düşük itki sağlar. (Genelde tercih edilmez).

### Lüle Tasarımı (Nozzle Design)
Süpersonik egzoz çıkışı sağlamak için **De Laval (Yakınsak-Iraksak)** lüle kullanılır.
Kritik parametreler:
1.  **Boğaz Alanı (Throat Area - $A_t$):** Yanma odası basıncını belirler.
2.  **Çıkış Alanı (Exit Area - $A_e$):** Egzoz gazının ideal genişlemesini sağlar.
3.  **Genişleme Oranı ($\epsilon$):** $\epsilon = A_e / A_t$.

> [!TIP]
> Deniz seviyesinde ideal genişleme için tipik oran 3-4 arasıdır. Yüksek irtifaya çıktıkça dış basınç azalır, bu yüzden roket motorlarında genellikle "hafifçe az genişletilmiş" (underexpanded) lüle tercih edilir.

## ⚙️ Entegrasyon ve Montaj

### Motor Kundağı (Motor Mount)
*   **Malzeme:** Yüksek sıcaklığa ve basınca dayanıklı *Kraft Fenolik* veya *Epoksi Fiberglas* tüp.
*   **Çap:** Motor çapına (75mm veya 98mm) tam uyumlu olmalıdır.

### Thrust Transferi
İtki kuvveti roket gövdesine **Thrust Plate (İtki Plakası)** veya **Centering Rings (Merkezleme Halkaları)** üzerinden aktarılır.
*   **Öneri:** L ve M sınıfı motorlarda mutlaka gövdeye vidalanan metal bir Thrust Plate kullanılmalıdır. Sadece epoksi ile yapıştırılmış halkalar risklidir.

## ⚠️ Güvenlik Uyarıları
*   **Depolama:** Motor yakıtları nemsiz ve serin ortamda saklanmalıdır.
*   **Statik Ateşleme Testi:** Motoru rokete takmadan önce yer test düzeneğinde test verisi alınmalıdır.
*   **Ateşleme Mesafesi:** Ateşleme sistemi en az **50 metre** (M sınıfı için 100m) uzaktan kontrol edilmelidir.
