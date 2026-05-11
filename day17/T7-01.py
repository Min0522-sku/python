# 웹 크롤링 : 웹페이지에 존재하는 데이터들을 수집 하는 기술
# 기초지식 : HTML/CSS(식별자) 필요
# 파이썬 크롤링 라이브러리 : request, BeautifulSoup 정적 / Selenium, Playwright 동적(JS/대기) 

# 크롤링(로봇) 허용 여부 확인 : 도메인/robots.txt
# 적절한 크롤링으로 윤리적 사용

# HTML/CSS 식별자(마크업, # id, . class, 자손선택자 띄어쓰기, 자식선택자 >) 찾기
# 브라우저 개발자도구[F12] -> 왼쪽상단에 마우스 아이콘(컨트롤+쉬프트+c) -> 크롤링 요소 선택 -> 확인

# 파이썬 크롤링
# 네이버 검색어 -> 안양날씨 -> 현재 날씨 크롤링
# 1. 주소 : https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%95%88%EC%96%91%EB%82%A0%EC%94%A8
# 퀘리스트링(주소상에 변수) : URL?벼눗명=값&변수명&값
# 2. 크롤링 선택자 : txt_temp

import requests
from bs4 import BeautifulSoup

# 특정한 URL 요청 requests.get(url)
respones = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=안양날씨")
print(respones)

# 요청(200)된 url에서 HTML 형식으로 파싱하기 BeautifulSoup(respones.text, "html.parser")
soup = BeautifulSoup(respones.text, "html.parser")

# 가져온 HTML에서 특정한 요소(식별자)만 가져오기 soup.select_one('식별자')
txt_temp = soup.select_one('.txt_temp')
print(txt_temp)

# 가져온 요소에서 텍스트만 추출, <마크업> *텍스트* </마크업>,  요소변수.get_text()
print(txt_temp.get_text()) # 18.2
