# Live Exchange Rates

This project fetches live exchange rate data from the Central Bank of the Republic of Turkey (CBRT) and Bloomberg HT to create and serve an XML file.

---

## English

### Project Goal

The main goal of this project is to fetch live exchange rates from the CBRT's `today.xml` file and Bloomberg HT's website and consolidate them into a single source. When data is pulled from Bloomberg HT, the generated XML file is automatically updated, ensuring access to the most current exchange rates at all times.

### Features

* Fetches real-time exchange rate data from CBRT and Bloomberg HT.
* Presents the data in XML format.
* Automatically updates when new data is fetched from Bloomberg HT.

### Technologies Used

* **Python:** The main programming language of the project. Data scraping and processing operations are handled with Python.
* **HTML/CSS/JavaScript:** Used for the web interface and user interactions.
* **XML:** The format used to store and serve the exchange rate data.
* **Data Sources:**
    * Central Bank of the Republic of Turkey (CBRT)
    * Bloomberg HT

### Installation and Usage

Follow the steps below to run the project on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/muhammedyayla/live-exchange-rates.git](https://github.com/muhammedyayla/live-exchange-rates.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd live-exchange-rates
    ```
3.  **Install the required dependencies:**
    *(Note: A `requirements.txt` file is not present in the repository. You might need to install libraries like `requests`, `beautifulsoup4`, `lxml` manually.)*
    ```bash
    pip install requests beautifulsoup4 lxml
    ```
4.  **Run the application:**
    ```bash
    python main.py
    ```

When the application runs, a file named `live-exchange-rates.xml` will be created, and you can access the latest exchange rates through this file.

---

## Türkçe

### Projenin Amacı

Bu projenin temel amacı, Türkiye Cumhuriyet Merkez Bankası'nın (TCMB) `today.xml` dosyasından ve Bloomberg HT'nin web sitesinden canlı döviz kurlarını alarak tek bir kaynakta birleştirmektir. Bloomberg HT'den veri çekildiğinde, oluşturulan XML dosyası otomatik olarak güncellenir, böylece her zaman en güncel döviz kurlarına erişim sağlanır.

### Özellikler

* TCMB ve Bloomberg HT'den anlık döviz kuru verilerini alır.
* Verileri XML formatında sunar.
* Bloomberg HT'den veri alındığında otomatik olarak güncellenir.

### Kullanılan Teknolojiler

* **Python:** Projenin ana programlama dili. Veri çekme ve işleme işlemleri Python ile gerçekleştirilmiştir.
* **HTML/CSS/JavaScript:** Web arayüzü ve kullanıcı etkileşimleri için kullanılmıştır.
* **XML:** Döviz kuru verilerinin saklandığı ve sunulduğu format.
* **Veri Kaynakları:**
    * Türkiye Cumhuriyet Merkez Bankası (TCMB)
    * Bloomberg HT

### Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Repository'yi klonlayın:**
    ```bash
    git clone [https://github.com/muhammedyayla/live-exchange-rates.git](https://github.com/muhammedyayla/live-exchange-rates.git)
    ```
2.  **Proje dizinine gidin:**
    ```bash
    cd live-exchange-rates
    ```
3.  **Gerekli bağımlılıkları yükleyin:**
    *(Not: Repository'de `requirements.txt` dosyası bulunmamaktadır. `requests`, `beautifulsoup4`, `lxml` gibi kütüphaneleri manuel olarak kurmanız gerekebilir.)*
    ```bash
    pip install requests beautifulsoup4 lxml
    ```
4.  **Uygulamayı çalıştırın:**
    ```bash
    python main.py
    ```

Uygulama çalıştırıldığında, `live-exchange-rates.xml` adında bir dosya oluşturulacak ve bu dosya üzerinden güncel döviz kurlarına erişebileceksiniz.
