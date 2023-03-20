import requests
from bs4 import BeautifulSoup
from newspaper import Article


req = requests.get("https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22doctor%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22common_name%22%7D%5D&city=Mumbai")

soup = BeautifulSoup(req.content, "html.parser")


# -----------------------------

# for h2 in h2:
articles = soup.find_all('div', class_ = 'listing-doctor-card')
for item in articles:
    h2 = ', '.join([x.get_text() for x in item.find_all('h2')])
    # print(h2)
    
    
    
articles = soup.find_all('span', class_ = 'u-c-pointer u-t-hover-underline')
for item in articles:
    h = ', '.join([x.get_text() for x in item.find_all('span')])
    # print(h2)
#
# -----------------------------
res = soup.text

print(soup.prettify())