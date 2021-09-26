from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://beta-flight.naver.com/'
browser.get(url)

# time.sleep(1)

# 가는 날 선택 클릭
# browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()



# 이번달 27일, 28일 선택 
# browser.find_elements_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button').click() # [0] - 이번달
# browser.find_elements_by_link_text('28')[1].click() # [1] - 다음달

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div/ul/li[2]/a')))
    # 성공했을 때 동작 수행
finally:
    browser.quit()



# 제주도 선택
elem = browser.find_elements_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div/ul/li[2]/a').click()







