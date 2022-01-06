import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status() # 문제가 생기면 프로그램 바로 종료하는 문장

soup = BeautifulSoup(res.text, "lxml")
#   가져온 html문서를 lxml을 통해 BeautifulSoup 객체로 만듦
#   soup이 모든 정보를 가지고 있음
#print(soup.title)
#print(soup.title.get_text()) #   soup.*** : ***로 바로 접근할 수 있게 해주는 함수
#print(soup.title.get_text()) #   title에서 글자만 가지고 옮
#print(soup.a) #   객체에서 처음 발견되는 a element 출력
#print(soup.a.attrs) #   a element 의 속성 정보를 출력
#print(soup.a.attrs["href"]) #   a element 의 href 속성 '값' 정보를 출력

#print(soup.find("a", attrs = {"class":"Nbton_upload"})) # class="Nbtn_upload" 인 a element 를 찾아줌
#print(soup.find(attrs = {"class":"Nbton_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줌
#print(soup.find("li", attrs={"class":"rank01"}))

#rank1 = soup.find("li", attrs={"class":"rank01"}) #1위 웹툰 찾아줌
#print(rank1.a.get_text()) # rank1 제목 보여줌
#rank2 = rank1.next_sibling.next_sibling # 다음순위(2위) 엘리먼트로 넘어감, 공백이 있을 시 두번 사용
#renk2 = rank1.find_next_sibling() #next_sibling을 여러번 쓸때 간소화
#rank3 = rank2.find_next_sibling() # 다음순위(3위) 엘리먼트로 넘어감
#print(rank3.a.get_text()) # rank3 제목 보여줌
#rank2 = rank3.previous_sibling.previous_sibling # 이전순위(1위) 엘리먼트로 넘어감
#renk2 = rank3.find_previous_sibling # previous_sibling 여러번 쓸때 간소화
#print(rank2.a.get_text()) # rank2 제목 보여줌
#print(rank1.parent) # rank1 "li"의 부모 엘리먼트를 보여줌(1위부터 다 보여줌)

#print(rank1.find_next_siblings("li")) # rank1 기준으로 모든 형제들을 가져옴(s가 붙음)

#webtoon = soup.rind("a", text="nadocoding") # 모든 정보에서 element 이름이 a이고 text가 nadocoding인 것을 찾아줌
#print(webtoon)