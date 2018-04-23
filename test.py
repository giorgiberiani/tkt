import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://tkt.ge/')

elemrnt  = driver.find_element_by_link_text('კინო').click()
movie = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/a/div[1]/img').click()
ticket = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[4]/div/a').click()

time.sleep(3)
action_chains = ActionChains(driver)
place = driver.find_element_by_xpath('//*[@id="XMLID_34_"]')
action_chains.move_to_element(place).click().perform()

time.sleep(3)
buy = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/div/div/div[2]/a').click()


time.sleep(4)
continue_without_registration = driver.find_element_by_xpath('//*[@id="Guest"]')
continue_without_registration.click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="Name"]').send_keys('name')
driver.find_element_by_xpath('//*[@id="Email"]').send_keys('male')
driver.find_element_by_xpath('//*[@id="Phone"]').send_keys('phone number')

driver.find_element_by_xpath('//*[@id="js-continue-btn"]').click()
time.sleep(5)
driver.quit()
