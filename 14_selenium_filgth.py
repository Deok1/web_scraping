from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 전체화면으로 전환

url = "https://m-flight.naver.com/"
browser.get(url) # url로 이동

# 가는날 선택 클릭
browser.find_element_by_link_text("가는 날").click()


# 이번달 27, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[7]/div/ul/li[1]/button/figure/img")

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 10초 동안 기다림, until 어떤 element가 나올 때까지, 시도하고 실패하면 종료, 성공하면 계속
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "xpath")))
    #성공했을 때 동작 수행
    print(elem.text) # 첫번째 동작 출력
finally:
    browser.quit() 


# 첫번 째 결과 출력
elem = browser.find_element_by_xpath("xpath")
print(elem.text)

