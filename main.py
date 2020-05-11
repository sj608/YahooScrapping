from bs4 import BeautifulSoup
import numpy
import matplotlib.pyplot as plt
import requests
import string
import math
import readtxt
import scrapping

ex_source = requests.get('https://ca.finance.yahoo.com/quote/CAD=X?p=CAD=X&.tsrc=fin-srch').text
ex_soup = BeautifulSoup(ex_source, 'lxml')
rate = float(str(ex_soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all('span')[0].contents[0]))


def main():
    portfolio = readtxt.readtxt("myportfolio.txt")
    url, shares= portfolio.read_file()
    price = []
    dividend = []
    total_share_price = []
    for element in url:
        WebScrap = scrapping.scrap_data(element)
        price.append(WebScrap.current_price(rate))
        dividend.append(WebScrap.dividend(rate))
    for i in range(len(price)):
        total_share_price.append(price[i] * shares[i])
    total = sum(total_share_price)
    stocks_in_percentage = (numpy.array(total_share_price)/total*100).astype(int)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(stocks_in_percentage, autopct = '%1.1f%%', startangle = 90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


if __name__ == "__main__":
    main()