import re
p = re.compile("ca.e")
def print_match(m):
    if m:
        print("m.group() :",m.group()) #일치하는 문자열 반환
        print("m.string :",m.string) #입력받은 문자열 반환
        print("m.start() :",m.start()) #일치하는 문자열의 시작 index
        print("m.end() :",m.end()) #일치하는 문자열의 끝 index
        print("m.span() :",m.span()) #일치하는 문자열의 시작|끝 index
    else:
        print("매칭되지 않음")

m = p.match("careless")
print_match(m)
# match : 주어진 문자열의 처음부터 일치하는지 확인


#m = p.search("good care")
#print_match(m)
# search : 주어진 문자열 중에 일치하는게 있는지 확인

#lst = p.findall("good care cafe")
#print(lst)
# findall : 일치하는 모든 것을 리스트 형태로 반환



# 정규식 정리
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열을 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트"형태로 반환

# "원하는 형태" = (정규식)
# . : 하나의 문자
#   ex) ca.e : care, cafe o | caffe x
# ^ : 문자열의 시작
#   ex) ^de : desk, default o | fade x
# $ : 문자열의 끝
#   ex) se$ : case, base o | face x





