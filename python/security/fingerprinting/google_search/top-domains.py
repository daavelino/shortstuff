import sys
import platform
from selenium import webdriver
import os

from selenium.common.exceptions import NoSuchElementException

# Please, not modify:
# Binaries dir:
BIN_DIR = './bin'

domain = 'globalhitss.com.br'

def connect():
    '''Returns a webdriver browser authenticated session.'''

    url = 'https://www.google.com'
    #### checking for the PhantomJS who suits better:
    if platform.system() == 'Windows':
        PHANTOMJS_PATH = os.path.join(BIN_DIR, 'phantomjs.exe')
    else:
        PHANTOMJS_PATH = os.path.join(BIN_DIR, 'phantomjs')

    #### Enabling the webkit:
    browser = webdriver.PhantomJS(PHANTOMJS_PATH)
    
    try:
        browser.get(url)
    except:
        print('Unable to connect to ' + url + 'Exit.', file=sys.stderr)
        return(False)

    return(browser)

def setSearchPreferences(browser):
    url = 'https://www.google.com/preferences'

    #### Xpath for the select page number output:
    selectXpath = '//*[@id="numsel"]'
    resnumXpath = '//*[@id="numsel"]/option[text()="100"]'

    try:
        browser.get(url)
        browser.find_element_by_xpath(selectXpath).click()    
        browser.find_element_by_xpath(resnumXpath).click()    
        browser.find_element_by_name('submit2').click()
        browser.switch_to.alert
#        browser.switch_to.alert.accept()
#        browser.switch_to.default_content
        return(browser)
    except: 
        print('Unable to set search configurations. Exit.', file=sys.stderr)
        return(False)
   
def search(browser, domain):
    #### This is the xpath of Google search form:
    searchString = 'site:' + str(domain) + ' -www.' + domain

    #### Performing the search:
    try:
        browser.find_element_by_name('q').send_keys(searchString)
        browser.find_element_by_name('btnG').click()
        return(browser)
    except:
        print('Unable to perform Google search. Exit.', file=sys.stderr)
        return(False)
    
def parseResult(browser):
    xpath = '//*[@id="ires"]/ol/div/div/div/cite'
    tmp = browser.find_elements_by_xpath(xpath)
    for i in tmp:
        print(i.text)

def getArguments():
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<domain>. Exit', file=sys.stderr)
        sys.exit(1)
  
    domain = sys.argv[1]
    return(domain)
    
def main():
    domain = getArguments()
    b = connect()
    b = setSearchPreferences(b)
    b = search(b, domain)
    parseResult(b)
#    print(b.page_source)

if __name__=="__main__":
    main()
 
