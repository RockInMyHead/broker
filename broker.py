from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary
import urllib
import time
##
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print ('start...')

site = "https://invest.yandex.ru/catalog/fund/fxwo/"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()
driver.get(site)

#one_prise = driver.find_element_by_id("root")
#print (one_prise)
#print('нихуя но все же норм')
import requests
from bs4 import BeautifulSoup

def big_broker(price):
    price2 = price
    def broker(price2):
        #селениум#
        site = "https://invest.yandex.ru/catalog/fund/fxwo/"

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome()
        driver.get(site)
        #селениум#
        url = 'https://invest.yandex.ru/catalog/fund/fxwo/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find('div', class_='_2NhGI8HVO_OG2E2pWl10IY')
        for i in quotes:
            quotes = i
            quotes = quotes.replace('₽','')
            quotes = quotes.replace(' ','') # чистим цифры

            newquotes = ""
            b = 0
            for i in quotes:
                b +=1
                if b < 7 and i != ',': # убираем запятую
                    newquotes += i
                    quotes = newquotes # 18440
                    old_price = int(newquotes)
                    #print(old_price)
        print ('Старая цена' + str(price2))
        print ('Новая цена' + str(old_price))
        #print (old_price)
        if price2 < old_price:
            print ('продаю')
            sell = driver.ffind_element_by_xpath("Icon Icon_svg Icon_type_star-outline Button2-Icon2").click()
        if price2 == old_price:
            print ('держу')
        if price2 > old_price:
            print ('покупаю')
        return old_price # выводим спарсенное число

    i = 0
    while i < 5:
        new_price = broker(price2) # вызываем функцию с новым значением
        #print (new_price)
        price = new_price
        return price # выводим спарсенное число
#print(quotes)
price = 0
big = big_broker(price)
price = big
h = 0
while h <3:
    big_broker(price) # вызываем главную функцию
    h+=1
