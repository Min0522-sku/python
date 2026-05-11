import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
# 주소 : https://www.yes24.com/product/category/bestseller?categoryNumber=001
#url = 'https://www.yes24.com/product/category/bestseller?categoryNumber=001'

# 주소의 매개변수 분석, ?categoryNumber=001&pageNumber=2&pageSize=24&sex=M&age=20&goodsStatGb=03
# 1~3 페이지 크롤링
book_list = []
for page in range(1,4):
    url = f'https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={page}&pageSize=24&sex=M&age=20&goodsStatGb=03'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    # .select():여러개 .select_one():하나선택
    # 책 여러개 : #yesBestList 여러개 책 정보, li(책하나)
    books = soup.select('#yesBestList > li')
    # 책하나당  가져올 식별자 .gd_name 제목 .yes_b 가격 .info_auth 저자및출판사
    for book in books:
        gd_name = book.select_one('.gd_name').get_text().strip()
        yes_b = book.select_one('.yes_b').get_text().strip()
        info_auth = book.select_one('.info_auth').get_text().strip().replace('\n', '')
        # 리스트에 딕셔너리 포함하기
        book_list.append({'제목':gd_name, '가격':yes_b, '저자정보':info_auth})
    # import time,   time.sleep(초) 지정한 초 만큼 코드(스레드) 대기샅애, ] 여러개 크롤링 할때 서버 과부화 방지
    time.sleep(2)

df = pd.DataFrame(book_list)
print(df)
