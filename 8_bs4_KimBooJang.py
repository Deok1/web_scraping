import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=783053&weekday=tue" # 김부장
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#cartoons = soup.find_all("td", attrs={"class":"title"})
#title = cartoons[0].a.get_text() #김부장의 첫 번째 제목 가져옴
#link = cartoons[0].a["href"]
#print(title)
#print("https://comic.naver.com" + link) #김부장으로 바로 가는 주소

# 만화 제목 + 링크 가져오기
#for cartoon in cartoons:
#    title = cartoons.a.get_text()
#    link = "https://comic.naver.com" + cartoon.a["href"]
#    print(title, link)

# 평점 평균 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons)) # 전체 평점의 합 / 웹툰의 갯수
