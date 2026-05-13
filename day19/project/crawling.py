# 크롤링

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
# 주소 : https://www.yes24.com/product/category/bestseller?categoryNumber=001
#url = 'https://www.yes24.com/product/category/bestseller?categoryNumber=001'

# 주소의 매개변수 분석, ?categoryNumber=001&pageNumber=2&pageSize=24&sex=M&age=20&goodsStatGb=03
# 1~3 페이지 크롤링
# book_list = []
# for page in range(1,10):
#     url = f'https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={page}&pageSize=120'

#     response = requests.get(url)

#     soup = BeautifulSoup(response.text, 'html.parser')
#     # .select():여러개 .select_one():하나선택
#     # 책 여러개 : #yesBestList 여러개 책 정보, li(책하나)
#     books = soup.select('#yesBestList > li')
#     # 책하나당  가져올 식별자 .gd_name 제목 .yes_b 가격 .saleNum 판매지수 .authPub.info_date 출판년월
#     for book in books:
#         gd_name = book.select_one('.gd_name').get_text().strip()
#         # 문자 , 제거 및 정수화
#         yes_b = int(book.select_one('.yes_b').get_text().strip().replace(',', ''))
#         # 불필요한 판매지수 글씨 제거 및 문자 정수화
#         saleNum = int(book.select_one('.saleNum').get_text().replace('판매지수', '').strip().replace(',', '')) 
#         info_date = book.select_one('.authPub.info_date').get_text().strip()
#         # 공백 기준으로 년과 월 나누기
#         info_date = info_date.split()
#         # 년 글씨 제거
#         year = info_date[0].replace('년', '')
#         # 월 글씨 제거
#         month = info_date[1].replace('월', '')
#         # 리스트에 딕셔너리 포함하기
#         book_list.append({'제목':gd_name, '가격':yes_b, '판매지수':saleNum, '출판년':year})
#     # import time,   time.sleep(초) 지정한 초 만큼 코드(스레드) 대기샅애, ] 여러개 크롤링 할때 서버 과부화 방지
#     time.sleep(2)

# df = pd.DataFrame(book_list)
# df.to_csv('day19/project/data/books.csv', index=False, encoding='utf-8-sig')





df= pd.read_csv('day19/project/data/books.csv',encoding='utf-8-sig')

print("평균 가격: ", df['가격'].mean())
print("최고 가격: ", df['가격'].max())
print("최저 가격: ", df['가격'].min())
result = df.groupby('출판년')['출판년'].count().idxmax() 
print("최다 출판년: ",result)


import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('font', family='Malgun Gothic') 
mpl.rcParams['axes.unicode_minus'] = False
import seaborn as sns 

# 시각화

# 가격대 별 히스토그램
plt.hist(df['가격'], color='skyblue', alpha=0.5, bins=40)
plt.title('가격대 별 책 개수')
plt.ylabel('책 개수')
plt.xlabel('가격대')
plt.show()



# 연도별 출판 갯수 막대 그래프
sns.countplot(df, x='출판년')
plt.title('연도별 출판 개수')
plt.ylabel('출판 개수')
plt.show( )