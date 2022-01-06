from typing import Counter
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li",attrs={"class":re.compile("^search-product")}) # ^search-product로 시작하는것들 
#print(items[0].find("div",attrs={"class":"name"}).get_text())
for item in items:

    #광고상품은 제외
    ad_badge = item.find("span",attrs={"class":"ad-badge-text"}) 
    if ad_badge: #광고문구가 있다면
        print("     <광고상품제외>")
        continue  #광고 제품은 걍 넘어감

    name = item.find("div",attrs={"class":"name"}).get_text()
    # HP 제품 제외
    if "HP" in name:
        print("     <HP 상품 제외합니다")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

    # 리뷰 500개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점 
    if rate: #rate가 있다면
        rate = rate.get_text()
    else:
        print("     <평점 없는 상품 제외>")
        continue

    rate_count = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
    if rate_count: #rate_count가 있다면
        rate_count = rate_count.get_text() #(26)으로 나옴 ()를 없애야 함
        rate_count = rate_count[1:-1] # 1번째 인덱스~-1번째 인덱스 까지
        #print("리뷰 수 : ", rate_count) # 순서대로 나오는지 페이지와 비교하는 문구
    else:
        print("     <평점 수 없는 상품 제외합니다>")
        continue
#-------평점, 평점 수 존재하는 것만 걸러짐-----
    
    if float(rate) >= 4.5 and int(rate_count) >= 500:
        print(name, price, rate, rate_count)