# Requirements
# pip install requests beautifulsoup4 lxml

# Adım 1. requests Kullanarak Web sayfası Çekme
import requests

url = "https://httpbin.org/get"

response = requests.get(url)

print(url)
print(response.content)    # Raw response (ham yanıt içeriği)
print(response.text)       # Text response (metinsel yanıt içeriği)
text = response.text
type(text)

print(response.json())     # JSON yanıt içeriği
r_json = response.json()
type(r_json)


# Adım 2. BeautifulSoup ile HTML Ayrıştırma (Parsing HTML)
from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")
type(soup)

# HTML'in düzenli görüntülenmesi
print(soup.prettify())

# Farklı elemanlara erişim
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.p)
print(soup.a)
print(soup.a.string)

print(soup.body)

# Bir etiketin tüm örneklerini bulma
print(soup.find_all("p"))
p_list = soup.find_all("p")
type(p_list)
len(p_list)
