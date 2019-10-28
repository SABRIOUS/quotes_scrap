from bs4 import BeautifulSoup

import requests

data = requests.get("http://quotes.toscrape.com/").text

soup = BeautifulSoup(data,'html.parser')

all_quote = soup.find_all('div',{'class':'quote'})

for title in all_quote:
    print(title.find('span',{'class',"text"}).string)
