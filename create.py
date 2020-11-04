import sys
import os
from selenium import webdriver
from dotenv import load_dotenv
import config

load_dotenv()


webdriver = webdriver.Chrome("chromedriver.exe")

def create():
    folderName = str(sys.argv[1])
    os.makedirs(config.path + str(folderName))
    webdriver.get("https://github.com/")
    b1 = webdriver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
    b1.click()
    t1 = webdriver.find_element_by_id("login_field")
    t1.send_keys(config.username)
    t2 = webdriver.find_element_by_id("password")
    t2.send_keys(config.password)
    b3 = webdriver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')
    b3.click()
    button = webdriver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
    button.click()
    textbox = webdriver.find_element_by_xpath('//*[@id="new_repository"]/div[2]/auto-check/dl/dd')
    textbox.send_keys(folderName)
    button2 = webdriver.find_element_by_xpath('//*[@id="repository_auto_init"]')
    button2.click()
    finishedButton = webdriver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
    finishedButton.click()
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()