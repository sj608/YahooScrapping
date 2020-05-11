from bs4 import BeautifulSoup
import requests


class scrap_data:
    
    def __init__(self, url):
        self.source = requests.get(url).text
        self.soup = BeautifulSoup(self.source, 'lxml')
        self.usd = False

    def current_price(self, rate):
        price =  float(self.soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all('span')[0].text)
        currency =str(self.soup.find_all('div',{'class':'C($tertiaryColor) Fz(12px)'})[0].find_all('span')[0].contents[0])
        if "USD" in currency:
            self.usd = True
            price = price * rate               
        return price

    def dividend(self, rate):
        dividend = str(self.soup.find_all('table', {'class':'W(100%) M(0) Bdcl(c)'})[0].find_all('tr')[5].contents[1].text).split(' ')[0]
        if dividend == 'N/A':
            return 0
        else:
            dividend = float(dividend)
            if self.usd == True:
                dividend = dividend * rate
        return dividend