﻿<div align="center">
  <img src="assets/university_logo.png" alt="University Logo" width="120" />
  <img src="assets/teknofest_logo.png" alt="Teknofest Logo" width="120" />

  # 📋 Teknofest 2026 Roket Takımı - Planlama ve Arşiv
  ### Karadeniz Teknik Üniversitesi - Gökçen Roket Takımı

  [![](https://img.shields.io/badge/Teknofest-2026-red?style=for-the-badge&logo=rocket)](https://teknofest.org/tr/)
  [![](https://img.shields.io/badge/Durum-Planlama-blue?style=for-the-badge)](https://teknofest.org/tr/)
  [![](https://img.shields.io/badge/Lisans-MIT-green?style=for-the-badge)](LICENSE)

  <br>

  **"Göklerdeki istikbalimiz için planlı, disiplinli ve bilimsel çalışma."**

</div>

---

> [!IMPORTANT]
> **📢 Takım Duyurusu ve Görevlendirme**
>
> 1.  **Erişim:** Repo üzerinde çalışmak isteyenler kullanıcı adlarını ileterek "Collaborator" olabilir veya doğrudan PR (Pull Request) açabilirler.
> 2.  **Rapor Analizi:** `geçmis_raporlar` klasöründe dosyalar "1. kişi", "2. kişi" şeklinde gruplandırılmıştır.
>     *   **Görev:** Bir klasör seçin ve adını **kendi adınızla (Ad_Soyad)** değiştirin.
>     *   İçindeki 3 raporu inceleyip önemli noktaları ve analizlerinizi not alın.
>     *   Herkese kolay gelsin! 🚀

---

## 📌 Depo Amacı
Bu repository, **KTÜ Gökçen Roket Takımı**'nın 2026 Teknofest Yarışması sürecindeki **tasarım, analiz, raporlama ve yönetim** belgelerini barındırır.
**Bu depoda aktif yazılım kodu bulunmamaktadır.** Yazılım geliştirme süreçleri ayrı repolarda yürütülmektedir.

---

## 🚀 Yarışma Hakkında (Teknofest Roket Kategorisi)

**T3 Vakfı** ve **Roketsan** öncülüğünde düzenlenen bu yarışma, öğrencilerin uzay teknolojileri alanında yetkinlik kazanmasını hedefler.

### 🏆 Kategoriler
Takımımız **Yüksek İrtifa (High Altitude)** kategorisinde yarışmaktadır.
*   **Orta İrtifa:** 5.000 feet (yaklaşık 1.500m) hedef irtifa.
*   **Yüksek İrtifa:** 10.000 feet (yaklaşık 3.000m) hedef irtifa - *Bizim Hedefimiz*
*   **Zorlu Görev:** 10.000 feet + Değişken Faydalı Yük görevi.

### 📝 Değerlendirme Süreci
Yarışma süreci 4 temel rapordan oluşur. Her aşama elemeli sistemdir:
1.  **KTR (Kavramsal Tasarım Raporu):** Projenin yapılabilirliği, takım yapısı ve literatür taraması puanlanır.
2.  **ÖTR (Ön Tasarım Raporu):** Matematiksel analizler, CFD simülasyonları ve detaylı CAD çizimleri istenir.
3.  **KTR (Kritik Tasarım Raporu):** Üretim planı, entegrasyon adımları ve nihai uçuş simülasyonları sunulur.
4.  **AHR (Atış Hazırlık Raporu):** Montajı tamamlanmış roketin test sonuçları ve uçuşa elverişlilik kanıtları sunulur.

### 🎯 Puanlama Kriterleri
*   **Raporlar:** %40 (Mühendislik hesapları ve dokümantasyon kalitesi).
*   **Atış ve Kurtarma:** %40 (Roketin sağlıklı şekilde tepe noktasına ulaşması ve paraşütlerin açılması).
*   **Faydalı Yük:** %10 (Görevin başarıyla icra edilmesi).
*   **Özgünlük:** %10 (Yerli tasarım ve inovatif çözümler).

---

## 📅 Çalışma Takvimi
Takım yönetim planına göre ana kilometre taşları:

| Dönem | Faaliyet | Durum |
| :--- | :--- | :--- |
| **Ocak 2026** | Takım Kurulumu ve Literatür Taraması | ✅ Tamamlandı |
| **Şubat 2026** | Kavramsal Tasarım Raporu (KTR) Hazırlığı | 🟡 Devam Ediyor |
| **Nisan 2026** | Ön Tasarım Raporu (ÖTR) Teslimi | 🔴 Bekleniyor |
| **Haziran 2026** | Kritik Tasarım Raporu (KTR) Teslimi | 🔴 Bekleniyor |
| **Ağustos 2026** | Montaj ve Entegrasyon (AIT) | 🔴 Bekleniyor |
| **Eylül 2026** | *TEKNOFEST FİNAL* 🚀 | 🔴 Bekleniyor |

---

## 📂 Dokümantasyon Yapısı

Tüm teknik ve idari belgeler `docs/` klasörü altındadır. Teknofest standartlarına uygun olarak kategorize edilmiştir:

### 📄 Rapor Şablonları
Yarışma isterlerine uygun taslaklar:
*   [Kavramsal Tasarım Raporu (KTR) Taslağı](docs/templates/KTR_Sablonu.md)
*   [Ön Tasarım Raporu (ÖTR) Taslağı](docs/templates/OTR_Sablonu.md)

### 🛠️ Alt Sistemler (Workspaces)
Her ekibin teknik notları ve tasarımları:
*   [Aerodinamik & Yapısal](docs/subsystems/aerodynamics.md)
*   [Aviyonik & Yazılım](docs/subsystems/avionics.md)
*   *Diğer alt sistemler `docs/subsystems/` altında oluşturulacaktır.*

### 📊 Yönetim ve Arşiv
*   [Bütçe ve Finans](docs/management/budget.md)
*   [Tasarım Notları (Ham)](docs/design_notes/)
*   [Geçmiş Raporlar](geçmis_raporlar/) - *(Raporlar takımdaki 11 kişiye 3'erli gruplar halinde paylaştırılmıştır)*
*   [İç Hesaplamalar](docs/internal/calculations_rationale.md)

---

## 🤝 Takım İçi Kurallar
1.  **Toplantı Disiplini:** Her Pazar 20:00'de haftalık toplantı yapılır.
2.  **Belgeleme:** Yapılan her hesaplama ve araştırma `docs/` altına işlenir.
3.  **İletişim:** WhatsApp grubu ve bu depo üzerindeki "Issues" sekmesi kullanılır.

---

## 📞 İletişim

*   **Takım Kaptanı:** [İsim Soyisim] (email@ktu.edu.tr)
*   **Akademik Danışman:** [Ünvan İsim Soyisim]

<div align="center">
  <p>© 2026 KTÜ Gökçen Roket Takımı</p>
</div>
