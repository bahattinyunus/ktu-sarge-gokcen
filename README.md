﻿<div align="center">
  <img src="assets/university_logo.png" alt="University Logo" width="120" />
  <img src="assets/teknofest_logo.png" alt="Teknofest Logo" width="120" />

  # 🚀 Teknofest Roket Yarışması 2026
  ### Karadeniz Teknik Üniversitesi Roket Takımı - Görev Kontrol Sistemi

  [![](https://img.shields.io/badge/Teknofest-2026-red?style=for-the-badge&logo=rocket)](https://teknofest.org/tr/)
  [![](https://img.shields.io/badge/Category-High_Altitude-blue?style=for-the-badge)](https://teknofest.org/tr/)
  [![](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
  [![](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)
  [![](https://img.shields.io/badge/Streamlit-Live_Dashboard-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
  [![CI Status](https://github.com/bahattinyunus/teknofest-rocket-2026/actions/workflows/ci.yml/badge.svg?style=for-the-badge)](https://github.com/bahattinyunus/teknofest-rocket-2026/actions)
  [![](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

  <br>

  **"Göklerdeki istikbalimiz için, daha yükseğe! Yerli mühendislik, gelişmiş aviyonik."**

</div>

---

## � İçindekiler
- [Proje Özeti](#-proje-özeti)
- [Sistem Mimarisi](#-sistem-mimarisi)
- [Temel Özellikler](#-temel-özellikler)
- [Modül Detayları](#-modül-detayları)
- [Hızlı Başlangıç](#-hızlı-başlangıç-quick-start)
- [Galeri](#-galeri)
- [Sıkça Sorulan Sorular (SSS)](/-sıkça-sorulan-sorular-sss)
- [Katkıda Bulunma](#-katkıda-bulunma-contributing)
- [İletişim](#-i̇letişim)

---

## 📋 Proje Özeti
Bu proje, **Teknofest 2026 Roket Yarışması** kapsamında geliştirilen, tamamen otonom uçuş algoritmalarını simüle eden ve yer istasyonu ile gerçek zamanlı haberleşmeyi sağlayan gelişmiş bir yazılım paketidir.

Proje sadece bir simülasyon değil, aynı zamanda gerçek uçuşta kullanılacak **Yer Kontrol İstasyonu (Ground Control Station - GCS)** yazılımının ta kendisidir.

---

## 🏗️ Sistem Mimarisi

Sistem, endüstri standardı **Microservices** mimarisi kullanılarak tasarlanmıştır.

```mermaid
graph TD
    subgraph "Rocket Segment (Simulation)"
        A[Sender Sim] -->|UDP (5005)| B
        A -->|Physics Engine| A
        A -.->|Listen (5006)| D[Command Receiver]
    end

    subgraph "Ground Segment"
        B[Receiver (Ground Station)] -->|Parse & Log| C[(CSV Database)]
        C <-->|Read Data| E[Dashboard (Streamlit)]
        E -->|UDP (5006)| D
    end

    style A fill:#ff9999,stroke:#333,stroke-width:2px
    style B fill:#99ff99,stroke:#333,stroke-width:2px
    style E fill:#99ccff,stroke:#333,stroke-width:2px
```

---

## ✨ Temel Özellikler

Bu repo, yarışma standartlarının üzerinde, profesyonel aviyonik özellikler sunar:

| Özellik | Açıklama | Teknoloji |
| :--- | :--- | :--- |
| **🚀 3D Uçuş Fiziği** | Rüzgar sürüklenmesi, fırlatma açısı ve aerodinamik sürüklenme (drag) simülasyonu. | `Python`, `Physics` |
| **🌍 GPS Entegrasyonu** | **Tuz Gölü** fırlatma alanına göre gerçek zamanlı GPS koordinat hesaplaması. | `Geospatial Calc` |
| **📈 Kalman Filtresi** | Sensör gürültüsünü (noise) temizleyen gelişmiş sinyal işleme algoritması. | `NumPy`, `Control Theory` |
| **🎮 Telekomut (Uplink)** | Roket ile çift yönlü haberleşme. Yerden **ARM**, **LAUNCH**, **DEPLOY** komutları gönderme. | `UDP Socket`, `Thread` |
| **🖥️ Görev Kontrol Paneli** | Canlı akan veriler, 3D yörünge çizimi ve harita takibi içeren web arayüzü. | `Streamlit`, `Plotly` |
| **🐳 Tam Konteynerizasyon** | Tek komutla tüm sistemi ayağa kaldıran `Docker` altyapısı. | `Docker`, `Compose` |

---

## � Modül Detayları

### 1️⃣ Simülasyon (`src/telemetry/sender_sim.py`)
Roketin sensör verilerini (İvme, Jiroskop, Barometre, GPS) fizik kurallarına uygun olarak üretir.
- **Multithreaded:** Hem fizik hesaplar hem de komut dinler.
- **Durum Makinesi:** IDLE -> READY -> ASCENT -> DESCENT -> LANDED durumları arasında geçiş yapar.

### 2️⃣ Algoritmalar (`src/algorithms/kalman.py`)
Gürültülü sensör verilerini temizlemek için tek boyutlu (1D) Kalman Filtresi uygular.
- **Tahmin (Predict):** Bir sonraki durumu öngörür.
- **Güncelleme (Update):** Ölçüm verisi ile tahmini düzeltir.

### 3️⃣ Görev Kontrol (`src/dashboard/dashboard.py`)
Operatörün roketi izlediği ve yönettiği ana ekrandır.
- **Grafikler:** Yükseklik, Hız, 3D Konum.
- **Harita:** Roketin düşeceği tahmini koordinat.
- **Fire Control:** Ateşleme ve kurtarma butonları.

---

## 🚀 Hızlı Başlangıç (Quick Start)

### Yöntem 1: Docker (Önerilen 🌟)
Tüm sistemi (Simülasyon, Yer İstasyonu, Dashboard) tek seferde başlatır.

```bash
make docker-up
```
*Durdurmak için: `make docker-down`*

### Yöntem 2: Manuel Kurulum (Geliştiriciler İçin)
Python 3.9+ gereklidir.

1.  **Kurulum:**
    ```bash
    make install
    ```
2.  **Simülasyonu Başlat:**
    ```bash
    make run-telemetry  # Roketi başlatır
    ```
3.  **Yer İstasyonunu Başlat:**
    ```bash
    make run-ground     # Verileri dinler ve kaydeder
    ```
4.  **Dashboard'u Aç:**
    ```bash
    make run-dashboard  # Web arayüzünü (localhost:8501) açar
    ```

---

## �️ Galeri

| Uçuş Analizi | Dashboard (Temsili) |
| :---: | :---: |
| ![Flight Analysis](flight_analysis.png) | *Dashboard ekran görüntüsü buraya gelebilir* |
| *Python ile oluşturulan uçuş sonrası analiz grafiği* | *Canlı telemetri ve 3D takibi* |

---

## ❓ Sıkça Sorulan Sorular (SSS)

**S: Bu yazılım gerçek roketle çalışır mı?**
C: Evet, `sender_sim.py` yerine gerçek uçuş bilgisayarından gelen seri port verisini okuyan bir modül koyarak doğrudan kullanılabilir.

**S: Kalman filtresi neden gerekli?**
C: Barometreler rüzgar ve titreşimden etkilenir. Kalman filtresi bu gürültüyü matematiksel olarak temizleyerek doğru irtifayı tahmin eder.

**S: Docker neden kullanıyoruz?**
C: "Benim bilgisayarımda çalışıyordu" sorununu çözmek için. Tüm takım üyeleri aynı ortamda çalışır.

---

## 🤝 Katkıda Bulunma (Contributing)

Bu proje açık kaynaklıdır ve katkılara açıktır. Lütfen [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyunuz. Herhangi bir güvenlik ihlali veya davranış kuralları için [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) geçerlidir.

---

<div align="center">
  <h3>🏆 Sponsorlarımız</h3>
  <table align="center">
    <tr>
      <td align="center" width="150"><img src="https://via.placeholder.com/100?text=Sponsor+1" alt="Sponsor 1"><br><b>Platin</b></td>
      <td align="center" width="150"><img src="https://via.placeholder.com/100?text=Sponsor+2" alt="Sponsor 2"><br><b>Altın</b></td>
      <td align="center" width="150"><img src="https://via.placeholder.com/100?text=Sponsor+3" alt="Sponsor 3"><br><b>Gümüş</b></td>
    </tr>
  </table>
  
  <br>

  <p>📬 İletişim: <a href="mailto:iletisim@ktu.edu.tr">iletisim@ktu.edu.tr</a></p>
  <p>© 2026 Karadeniz Teknik Üniversitesi Roket Takımı</p>
  <i>"İstikbal Göklerdedir" - K. Atatürk</i>
</div>
