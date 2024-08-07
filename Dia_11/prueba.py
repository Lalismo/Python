import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

url = url_base.format('1')

resultado =  requests.get(url)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

paginas = sopa.select('.product_pod')

for pagina in paginas:

    print(len(pagina.select('.star-rating.Four')))
