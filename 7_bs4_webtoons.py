#모든 웹툰 정보를 가져옴
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title 인 모든 "a" element 를 반환
for cartoon in cartoons: #모든 웹툰의 제목을 가져오는 반복문
    print(cartoon.get_text())

