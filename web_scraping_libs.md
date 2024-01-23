# Python Web Scraping Kütüphaneleri ve Parser'lar

Web scraping, web sitelerinden veri çekme işlemidir ve Python, bu amaçla kullanılan birçok kütüphane ve parser sunar. İşte en popüler Python web scraping kütüphaneleri ve parser'lar:

## 1. `BeautifulSoup`

`BeautifulSoup`, HTML ve XML dosyalarını ayrıştırmak için kullanılan popüler bir Python kütüphanesidir. Kolay kullanımı ve güçlü ayrıştırma yetenekleriyle bilinir.

- **Özellikler**:
  - HTML ve XML dosyalarını kolayca ayrıştırabilir.
  - Çeşitli parser'larla (lxml, html5lib) uyumludur.
  - Karmaşık HTML yapısında gezinmeyi ve veri çekmeyi kolaylaştırır.

- **Kurulum**:
  ```bash
  pip install beautifulsoup4
  ```

- **Kullanım Örneği**:
  ```python
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html_content, 'html.parser')
  ```

## 2. `lxml`

`lxml` hızlı ve özellik zengini bir XML ve HTML parser'dır. C dilinde yazılmıştır ve büyük XML/HTML veri setleri üzerinde yüksek performans sağlar.

- **Özellikler**:
  - Çok hızlı ve verimli bir parser.
  - XPath ve XSLT destekleri mevcuttur.
  - Büyük dosyalar üzerinde etkili çalışabilir.

- **Kurulum**:
  ```bash
  pip install lxml
  ```

## 3. `Scrapy`

`Scrapy`, web crawling ve scraping için kullanılan bir Python framework'üdür. Büyük ölçekli web scraping projeleri için idealdir.

- **Özellikler**:
  - Güçlü ve hızlı crawling kabiliyetleri.
  - Çeşitli çıktı formatlarını destekler (JSON, CSV).
  - Özel middlewares ve extensions ile genişletilebilir.

- **Kurulum**:
  ```bash
  pip install scrapy
  ```

## 4. `selenium`

`selenium`, web browser'ları otomatik olarak kontrol etmek için kullanılır. JavaScript ile yüklenen içeriği ayrıştırmak için idealdir.

- **Özellikler**:
  - Tam bir web browser kontrolü sağlar.
  - JavaScript içeren dinamik web sayfalarını işleyebilir.
  - Otomatik testler için de kullanılır.

- **Kurulum**:
  ```bash
  pip install selenium
  ```

## 5. `requests-html`

`requests-html`, modern web sitelerini ayrıştırmak için kullanılan bir kütüphanedir. `requests` kütüphanesinin gelişmiş özelliklerini sunar.

- **Özellikler**:
  - JavaScript destekli sayfaları ayrıştırabilir.
  - Asenkron destek sağlar.
  - Kolay ve kullanışlı API.

- **Kurulum**:
  ```bash
  pip install requests-html
  ```
## 6. `html.parser`

`html.parser`, Python'ın standart kütüphanesine dahil edilmiş bir HTML parser'dır. Dışa bağımlılıkları olmayan bu parser, BeautifulSoup ile birlikte kullanıldığında ekstra kurulum gerektirmez.

- **Özellikler**:
  - Python ile birlikte gelen bir kütüphanedir, ek kurulum gerektirmez.
  - Küçük-orta ölçekli projeler için yeterli olabilir.
  - `lxml` ve `html5lib` gibi üçüncü parti parser'lara göre daha yavaş olabilir, ama basit ayrıştırma işlemleri için uygun bir seçenektir.

- **Kullanım Örneği**:
  ```python
  from bs4 import BeautifulSoup
  # BeautifulSoup'ın default parser'ı olarak kullanılır.
  soup = BeautifulSoup(html_content, 'html.parser')
  ```


## Parser Seçimi

Web scraping yaparken kullanılacak parser, projenin gereksinimlerine ve hedeflenen web sayfasının yapısına göre değişebilir. Örneğin, `lxml` hız açısından üstünken, `html5lib` daha toleranslı ve esnektir. 

Parser seçimi yaparken, eğer ekstra kütüphaneler yüklemek istemiyorsanız veya daha basit bir ayrıştırma işlemi yapıyorsanız `html.parser` iyi bir seçenektir. Ancak, performans ve özellik açısından daha zengin bir parser gerektiren durumlarda `lxml` veya `html5lib` gibi alternatifler tercih edilebilir. `lxml` genellikle en hızlı BeautifulSoup parser'ı olarak bilinir ve büyük ve karmaşık HTML belgeleri için önerilir. Öte yandan, `html5lib` HTML5 özelliklerini destekler ve hatalı biçimlendirilmiş HTML ile daha iyi başa çıkabilir, bu nedenle toleranslı bir ayrıştırma gerektiren durumlarda tercih edilir.