import time, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument(r"user-data-dir=C:/Users/gabri/AppData/Local/Google/Chrome/User Data")
#prefs = {"profile.default_content_setting_values.geolocation" :2}
#chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

currentTime = time.time()

checkoutUrl = 'https://www.supremenewyork.com/checkout'
keyword = 'Boxer'
color1 = 'Black'
color2 = ''
url = 'http://www.supremenewyork.com/shop/all/accessories'


##### FUNCTIONS #####

def findItem(keyword, color1, color2):
    keywordTrue = False
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for div in soup.find_all('div', 'turbolink_scroller'):
        for a in div.find_all(href=True):            
            if keywordTrue:    #make if div class sold_out then get return false or get the next color, personal preference
                if color1 or color2 in a.text:
                    browser.get('http://www.supremenewyork.com' + a['href'])
                    return True #success, breaks operation

            if keyword in a.text: #checks the keyword (works)
                keywordTrue = True
            else:
                keywordTrue = False
    #parses through the h1 and p tags. h1 for keyword and p for color. The next tag after an h1 is a p(has to be checked again)
    #so the next p after the checked previous h1 will be checked for color and the href will be copied and opened
    
    return False #assuming the whole url was searched and keyword and color was not found

def copTime():
    return

def copRestock():
    return

def checkout(browser):
    # Fills in personal info
    Select(browser.find_element_by_id('order_billing_state')).select_by_visible_text('WA')
    browser.execute_script("document.getElementById('order_billing_name').value = 'Ermano Winata'")
    browser.execute_script("document.getElementById('order_email').value = 'gabrielgilbiyanto@gmail.com'")
    browser.execute_script("document.getElementById('order_tel').value = '206-849-9598'")
    browser.execute_script("document.getElementById('bo').value = '15524 Corliss Ave N'")
    #browser.execute_script("document.getElementById('oba3').value = '325'")
    browser.execute_script("document.getElementById('order_billing_zip').value = '98133'")
    browser.execute_script("document.getElementById('order_billing_city').value = 'Shoreline'")

    # Fills in card info
    browser.execute_script("document.getElementById('nnaerb').value = '11111111111'")
    browser.find_element_by_xpath('//*[@id="orcer"]').send_keys('648')
    browser.execute_script("document.getElementById('credit_card_month').value = '01'")
    browser.execute_script("document.getElementById('credit_card_year').value = '2021'")

    # Checks checkbox and checks out
    browser.execute_script("document.getElementsByClassName('iCheck-helper')[1].click()")
    browser.execute_script("document.getElementsByName('commit')[0].click()")



def main():
    ''' 
    NOTES: (IMPORTANT)
    
    Using google sign in does not work. I can only think of harvesting cookies by doing a lot of captchas before the launch using .sleep doing captchas on copmenot.com
    if we solve the cpatcha during the process, it will tremendously slow down the cop time
    
    '''

    browser.get(url)
    #browser.execute_script("window.open(url);")
    
    startInput = input("Start?: ")
    while (startInput!='start'):
        startInput = input("Start?: ")

    start_time = time.time()

    findItem(keyword, color1, color2)
    browser.execute_script("document.getElementsByName('commit')[0].click()") # Clicks on add to cart button 
    WebDriverWait(browser,10).until(EC.visibility_of_any_elements_located((By.ID,'cart')))
        
    #test which one is faster
    #checkstart = time.time()
    #browser.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    browser.execute_script("document.getElementsByClassName('button checkout')[0].click()")
    #print("--- %s seconds ---" % (time.time() - checkstart))
        
    checkout(browser)

    print("--- %s seconds ---" % (time.time() - start_time)) #timer check

#Things to check-
#What if we entered the wrong color but right keyword, or even the wrong keyword?
#->What will happen is that the while loop will keep running once the program runs and I think that this is
#  a bad program design. But it should work with all substring of the words.
#  We should tell the program to stop after a few seconds so we can run it again with another keyword.
#If sold out: check another color or exit the program
#This code has bugs if there is another turbolink_scroller class with the a same item keyword and color substring

##### CALL HERE #####

main()