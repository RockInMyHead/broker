from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as ec
import chromedriver_binary
import urllib
import time
import pickle
##
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print ('st.')

#site = "https://invest.yandex.ru/catalog/fund/fxwo/"

#chrome_options = Options()
#chrome_options.add_argument("--headless")

#driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()
#driver.get(site)

#one_prise = driver.find_element_by_id("root")
#print (one_prise)
#print('нихуя но все же норм')
import requests
from bs4 import BeautifulSoup

#def big_broker(price):
    #price2 = price
prise_list = [0]
old_price = 0
def broker( prise_list ): # 18440
        old_price = 0
        paper = 5
        #селениум#
        site = "https://invest.yandex.ru/catalog/fund/fxwo/"

        #chrome_options = Options()
        #chrome_options.add_argument("--headless")

        #driver = webdriver.Chrome()
        #driver.get(site)
             #picklein.dump(driver.get_cookies(), open ("session","wb"))
        chromedriver = 'C:/chromedriver'
        #options = webdriver.ChromeOptions()
        #options = Options()
        #options.add_argument("--headless") # для открытия headless-браузераoptimize
        options = webdriver.ChromeOptions()
        options.add_argument('‐‐headless')  # для открытия hea
        options.add_argument("‐‐log level = 3")
        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
        driver.get(site)



        #селениум#
        def buy_paper():
             print ('/////////////////покупаю')
             time.sleep(7)
             #WebDriverWait(driver, 300).until(lambda x: x.find_element_by_css_selector('.test'))
             element_one =driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div[1]/div/div/div/div[6]/div[3]/button")
             element_one.click()
             time.sleep(7)
             buy = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div[2]/label[1]/label/input").send_keys(5)
             #enter = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div[2]/label[1]/label/input").send_keys(u'\ue007')
             time.sleep(4)
             button_1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[2]/div/div").click()
             time.sleep(3)
             button_buy = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div[5]/button").click()
             #sell = driver.ffind_element_by_xpath("Icon Icon_svg Icon_type_star-outline Button2-Icon2").click()
        def sell_paper():
            print ('/////////////////продаю')
            time.sleep(5)
            print ('///////////////////////разница:'+ str(price2 - old_price))
            element_one =driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div[1]/div/div/div/div[6]/div[2]/button")
            #                                           /html/body/div[2]/div[1]/div/div/div/div/div[1]/div/div/div/div[5]/div[2]
            element_one.click()
            time.sleep(5)
            sell = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div[2]/label[1]/label/input").send_keys(5)
            #enter = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div[3]/div[2]/label[1]/label/input").send_keys(u'\ue007')
            time.sleep(4)
            button_2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[2]/div/div").click()
            time.sleep(4)
            button_sell = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div[5]/button").click()
        def register_on_site():

            reg_path = "/html/body/div[2]/div[1]/header/div/span[2]/a[1]" #"/html/body/div[2]/div[1]/header/div/span[2]/a[1]"
            #element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/header/div/span[2]/a[1]")))
            register = driver.find_element_by_xpath("/html/body/div[2]/div[1]/header/div/span[2]/a[1]").click()
            yandex_id = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/span/input"
            password = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/span/input"
            register_id = driver.find_element_by_xpath(yandex_id).send_keys("arty.butcko@yandex.ru")
            register_button_1 =driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button").click()
            #/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button
            time.sleep(4)
            cookie = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/button").click()
            register_password = driver.find_element_by_xpath(password).send_keys("135797531AaA")
            #/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button
            register_button_2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button").click()
        ind = 0
        h = 0
        register_on_site()
        #driver.get(site)
        #pickle.dump(driver.get_cookies(), open ("session","wb"))
        #driver.get(site)
        #for cookies in pickle.load(open('session', 'rb')):
            #driver.add_cookie(cookies)
        #driver.get(site)
        #time.sleep(20)
        #driver.get(site)
        #url_auth = "https://passport.yandex.ru/auth?retpath=https%3A%2F%2Finvest.yandex.ru%2Fcatalog%2Ffund%2Ffxwo%2F"
        #session_1 = requests.Session()
        #auth_1 = session_1.post(url_auth, data = {'login':'arty.butcko@yandex.ru'})
        #print (auth_1)
        #url_auth_2 = "https://passport.yandex.ru/registration-validations/auth/multi_step/commit_password"
        #session_2 = requests.Session()
        #auth_2 = session_2.post(url_auth_2, data = {'password':'135797531AaA'})
        #print (auth_2)
        x = 1
        if x == 1:
            driver.get("https://invest.yandex.ru/catalog/fund/fxwo/")
            rehtml = driver.page_source
            #url = 'https://invest.yandex.ru/catalog/fund/fxwo/'
            #response = requests.get(site)
            soup = BeautifulSoup(rehtml, 'html5lib')
            quotes = soup.find('div', class_='_2NhGI8HVO_OG2E2pWl10IY')
            print (quotes)
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
                        quotes = newquotes # 2 0000
                price2 = int(newquotes)
            ind += 1
            print (price2)
            print (prise_list)
            if price2 != prise_list[-1] and prise_list[-1] != 0 :
                    #print(old_price)
        #print (old_price)
        #print (prise_list)
        #print (prise_list)
                i = 0
                if prise_list[0] == 0 :
                    i = 1
                else:

            #print (old_price)
            #print (prise_list)
            #print ('Старая цена' + str(prise_list[-1]))
                    print ('Новая цена' + str(price2))
                    time.sleep(5)
                    if len(prise_list) < 7 and prise_list[0] != 0:
                        if price2 > prise_list[-1] : # если разница между ценами больше 2 процента то продаем
                            try:
                                buy_paper() # покупа
                                prise_list.insert(0,price2)
                                print ("/////////////////////Покупаю")
                            except NoSuchElementException:
                                print ("Повторная покупка ошибка : NoSuchElementException")
                                print ("Не купил")
                                pass
                            except WebDriverException:
                                print ("Повторная покупка ошибка : WebDriverException")
                                print ("Не купил")
                                pass
                            except ElementClickInterceptedException:
                                print ("Повторная покупка ошибка : ElementClickInterceptedException")
                                print ("Не купил")
                                pass
                    if price2 == prise_list[-1] :
                        print ('/////////////////держу')
                #buy_paper(
                    k = 0
                    for i in prise_list:
                        k += 1
                        if price2 < i:
                            try:
                                sell_paper() # покупа
                                del prise_list[k-1]
                                print ("////////////////////////продаю")
                            except NoSuchElementException:
                                print ("Повторная продажа ошибка : NoSuchElementException")
                                print ("Не продал")
                                pass
                            except WebDriverException:
                                print ("Повторная продажа ошибка : WebDriverException")
                                print ("Не продал")
                                pass
                            except ElementClickInterceptedException:
                                print ("Повторная продажа ошибка : ElementClickInterceptedException")
                                print ("Не продал")
                                pass

                    if len(prise_list) > 10:
                        print ("Бумаги сильно падают в цене!")
            # [2000, 2200, 23000
        #if len(prise_list) > 0:
        if prise_list[0] == 0:
            prise_list[0] = price2
        else:

            del prise_list[-1]
            prise_list.append(int(price2)) # [20000, 21000, ...]
        new_price = price2
        print (prise_list)
        print (new_price)
        #return new_price  #2 0000 # выводим спарсенное число
        return prise_list # выводим список
        old_price = new_price
        return old_price

i = 1
while i<2:
    #price = broker(prise_list) # вызываем функцию с новым значением
        #print (new_price)
        #price = new_price
        #return price # выводим спарсенное число
    broker( prise_list )
#print(quotes)
#price = 0
#big = big_broker(price)
#price = big
#h = 0
#while h <100:
#    big_broker(price) # вызываем главную функцию
    #h+=1

    #h+=1
