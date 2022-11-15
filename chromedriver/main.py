# import requests
# from bs4 import BeautifulSoup
#
# from requests.auth import HTTPBasicAuth
#
# s = requests.session()
#
# auth = HTTPBasicAuth('an4romeda@yandex.ru', '240804qqq')
# url = "https://passport.yandex.ru/auth"
#
# data = {"login" : "an4romeda@yandex.ru", "password" : "240804qqq"}
# r = s.post(url, data = data)
#
# s.cookies
# print(r.status_code)
#
# urlData = "https://realty.ya.ru/moskva/kupit/kvartira/"
#
# response = requests.get(urlData)
# soup = BeautifulSoup(response.text, 'lxml')
# print(soup)
import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#url = "https://passport.yandex.ru/auth?origin=realty_moscow&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Frealty.ya.ru%252Fmoskva%252Fkupit%252Fkvartira%252Fdvuhkomnatnaya%252F%26uuid%3D05c3f67f-1d9f-4e5a-9f73-e1f59c44438d"
url = "https://accounts.google.com/v3/signin/identifier?dsh=S1409646430%3A1668440691054184&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAsSx9ZiDg_LVE8xE1quMrPrMKQvvukfShnmyoXX1FceFmzQgdMSaAhtu4MPNmoKjZ2WIFoI"
driver = webdriver.Chrome()

try:
    driver.get(url=url)
    time.sleep(5)

    # login_input = driver.find_element(By.ID, "passp-field-login")
    # login_input.clear()
    # login_input.send_keys("an4romeda@yandex.ru")
    #
    # time.sleep(3)
    # driver.find_element(By.ID, "passp:sign-in").click()
    #
    # time.sleep(5)
    # pass_input = driver.find_element(By.ID, "passp-field-passwd")
    # pass_input.clear()
    # pass_input.send_keys("240804qqq")
    #
    # time.sleep(3)
    # driver.find_element(By.ID, "passp:sign-in").click()

    login_input = driver.find_element(By.ID, "identifierId")
    login_input.clear()
    login_input.send_keys("nekit991tka2017@gmail.com")

    time.sleep(5)

    driver.find_element(By.ID, "identifierNext").click()

    time.sleep(5)

    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("240804qqq")


    time.sleep(5)

    driver.find_element(By.ID, "passwordNext").click()

    time.sleep(10)

    pickle.dump(driver.get_cookies(), open("cookies", "wb"))
    # driver.add_cookie("cookies")
    # time.sleep(5)
    # driver.get(url=url)
    time.sleep(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
