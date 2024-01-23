################## UYGULAMA 1: BBC NEWS HABER BAŞLIKLARINI ÇEKMEK ##################

# Gerekli kütüphaneleri import ediyoruz
import requests
from bs4 import BeautifulSoup

# BBC News web sitesinin URL'sini bir değişkende saklıyoruz
url = "https://www.bbc.com/news"

# URL'ye bir HTTP GET isteği göndererek sayfanın içeriğini alıyoruz
response = requests.get(url)

# BeautifulSoup ile HTML içeriğini ayrıştırıyoruz
soup = BeautifulSoup(response.text, "html.parser")

# h3 etiketlerini buluyoruz çünkü bu etiketler genellikle haber başlıkları için kullanılıyor
h3_tags = soup.find_all("h3")

# Bulduğumuz h3 etiketlerinin içindeki metinleri (yani haber başlıklarını) yazdırıyoruz
for tag in h3_tags:
    print(tag.text.strip())  # .strip() fonksiyonu başındaki ve sonundaki boşlukları temizler


############### UYGULAMA 2: BBC NEWS HABER BAŞLIKLARI VE İÇERİKLERİNİ ÇEKMEK ###############

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

news_items = soup.find_all("h3")
for item in news_items:
    parent_a_tag = item.find_parent("a")

    # Üst a etiketi varsa işlemleri gerçekleştiriyoruz
    if parent_a_tag and 'href' in parent_a_tag.attrs:
        headline = item.text.strip()
        link = parent_a_tag["href"]

        # Eğer bağlantı tam bir URL değilse, ana URL ile birleştiriyoruz
        if not link.startswith("http"):
            link = "https://www.bbc.com" + link

        # Haberin detay sayfasına istek gönderiyoruz
        detail_response = requests.get(link)
        detail_soup = BeautifulSoup(detail_response.text, "html.parser")

        # Haber metnini buluyoruz
        article_body = detail_soup.find("article")
        if article_body:
            paragraphs = article_body.find_all("p")
            content = ' '.join([para.text for para in paragraphs])

            # Haber başlığı ve içeriğini yazdırıyoruz
            print(f"Başlık: {headline}\nİçerik: {content}\nLink: {link}\n\n")
