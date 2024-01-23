############ UYGULAMA 1: WIKIPEDIA'DAN LIVERPOOL F.C. HISTORY KISMINI ÇEKMEK ############

# Gerekli kütüphaneleri import ediyoruz
import requests
from bs4 import BeautifulSoup

# Wikipedia'dan Liverpool FC sayfasının URL'si
url = "https://en.wikipedia.org/wiki/Liverpool_F.C."

# URL'den içeriği çekiyoruz
response = requests.get(url)

# BeautifulSoup ile HTML içeriğini ayrıştırıyoruz
soup = BeautifulSoup(response.text, "html.parser")

# Liverpool FC'nin tarih bölümünü buluyoruz
history_sec = soup.find("span", id="History").parent

# Tarih bölümünün hemen ardından gelen ilk dört paragrafı buluyoruz
first_4 = history_sec.find_next_siblings("p", limit=4)

# Bu dört paragrafı yazdırıyoruz
for p in first_4:
    print(p.text)

# Tarih bölümünün hemen ardından gelen ilk on bir paragrafı buluyoruz ve yazdırıyoruz
for p in history_sec.find_next_siblings("p", limit=11):
    print(p.text)


########## UYGULAMA 2: WIKIPEDIA'DAN LIVERPOOL F.C. COLOURS AND BADGE KISMINI ÇEKMEK ##########

# Renkler ve Rozet bölümünü buluyoruz
colors_badge_sec = soup.find("span", id="Colours_and_badge").parent

# Bu bölümün hemen ardından gelen ilk dört paragrafı buluyoruz ve yazdırıyoruz
for p in colors_badge_sec.find_next_siblings("p", limit=4):
    print(p.text)


############# UYGULAMA 3. LIVERPOOL FC KULÜP KAPTANLARI VERI ÇEKME SCRIPTI #############

# Kulüp kaptanları bölümünü buluyoruz
captains_sec = soup.find('span', id="Club_captains")

# Kulüp kaptanları bölümünün içindeki bir sonraki table etiketini buluyoruz
captains_table = captains_sec.find_next("table")

# Tablonun tüm satırlarını buluyoruz, ilk satırı (başlık) atlıyoruz
rows = captains_table.find_all('tr')[1:]

# Her satırdaki bilgileri ayrıştırarak kulüp kaptanlarının listesini oluşturuyoruz
captains = []
for row in rows:
    cols = row.find_all('td')
    if len(cols) > 1:
        captains_name = cols[0].get_text(strip=True)
        captains_years = cols[1].get_text(strip=True)
        captains.append((captains_name, captains_years))

# Kulüp kaptanlarının adlarını ve görev yaptıkları yılları yazdırıyoruz
for captain in captains:
    print(f"Kaptan Adı: {captain[0]}\tYıllar: {captain[1]}")


############ UYGULAMA 4. BASIT HTML TABLO AYRIŞTIRMA SCRIPTI ############

# Bir satırın analizi için örnek HTML içeriği ayrıştırıyoruz
one_row = """
<tr>
<td>...</td>
<td>1892–1895</td>
</tr>
"""

# BeautifulSoup ile bu örnek HTML içeriğini ayrıştırıyoruz
soup = BeautifulSoup(one_row, "html.parser")

# td etiketlerini buluyoruz
td_info = soup.find_all("td")

# Her bir td etiketinin metnini alıyoruz ve yazdırıyoruz
for td in td_info:
    print(td.get_text(strip=True))
