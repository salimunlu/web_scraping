# Web Scraping Projeleri

Bu repository, farklı web kaynaklarından veri çekmek için Python dili kullanılarak oluşturulmuş bir dizi web scraping scriptini içermektedir.

## İçerikler

- `bs4_basics.py` - BeautifulSoup kullanarak HTML ayrıştırma temelleri.
- `bbc_news.py` - BBC News web sitesinden haber başlıklarını çeken script.
- `wikipedia_liverpoolFC.py` - Wikipedia'dan Liverpool F.C. tarihi ve kulüp kaptanları bilgisi çeken script.

## Ön Koşullar

Projeyi kullanmadan önce, gerekli Python paketlerinin yüklenmiş olduğundan emin olun:

```bash
pip install requests beautifulsoup4 lxml
```

## Kullanım

Her scripti ayrı ayrı çalıştırarak ilgili web sayfasından verileri çekebilirsiniz:

```bash
python bbc_news.py
python wikipedia_liverpoolFC.py
```

## Katkıda Bulunma

Projeye katkılarınızı bekliyoruz! Lütfen bir 'pull request' açarak veya hataları 'issues' olarak bildirerek katkıda bulunun.