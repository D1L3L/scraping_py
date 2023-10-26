from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def valor_dollar_hoje():
    url = "https://www.google.com/search?q=dollar+hj&oq=dollar+hoje" 
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    #driver.find_element("g-card-section", ({"class" ="DFlfde SwHCTb"}).find)
    return price
    driver.quit()
    
price = valor_dollar_hoje()
sleep(5)

print (f"O valor do dollar hoje é: {price}")
