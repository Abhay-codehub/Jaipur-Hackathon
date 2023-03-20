import requests
from bs4 import BeautifulSoup
from newspaper import Article

req = requests.get(
    "https://www.practo.com/search/hospitals?results_type=hospital&q=%5B%7B%22word%22%3A%22hospital%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22type%22%7D%5D&city=Jaipur")

soup = BeautifulSoup(req.content, "html.parser")

# -----------------------------

# for h2 in h2:
articles = soup.find_all('div', class_='c-estb-info')
for item in articles:
    a2 = ', '.join([x.get_text() for x in item.find_all('a')])
    print(a2)

#
# -----------------------------
res = soup.text

# print(soup.prettify())