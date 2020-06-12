#web scraping
import requests, bs4
url = ('https://www.facebook.com/')
res = requests.get(url)
res.raise_for_status
soup = bs4.BeautifulSoup(res.text,'html.parser')
elems = soup.find_all('div span')
info = soup.find_all("dl", {'class':'attributes dl-horizontal'})
elems = elems.getText()
print (elems)
