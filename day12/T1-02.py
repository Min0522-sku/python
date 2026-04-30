import pandas as pd

# pd.DataFrame 2차원 

# 2차원 리스트로 생성
# pd.DataFrame(2차원 리스트, columns = [열이름 목록]) columns 없으면 0 부터 시작
data_list = [ 
    ['ant', 25, 'seoul'],
    ['bee', 30, 'busan'],
    ['cat', 35, 'incheon']
             ]
x = pd.DataFrame(data_list, columns=['name','age','city'])
print(x)

# 딕셔너리로 생성
# pd.DataFrame(딕셔너리) 자동으로 키이름으로 열이름 생성    
# 대부분의 공공 자료는 *딕셔너리*
data_dict = {'name' : ['ant','bee','cat'], 'age' : [25,30,35], 'city':['seoul','busan','incheon']}
y = pd.DataFrame(data_dict)
print(y)

# 넘파이 배열로 생성
import numpy as np
data_np = np.array(data_list)
z = pd.DataFrame(data_np, columns=['name','age','city'], index=['a','b','c']) # index=[행이름] 으로 행이름 설정 가능
print(z)

# 주요속성
print(z.shape) # 행/열 크기
print(z.columns) # 컬럼(열) 목록
print(z.index) # 인덱스(행) 목록
print(z.values) # 값만 2차원으로 반환

# 주요 탐색
print(z.head(2)) # 상위 n개 반환
print(z.tail(2)) # 하위 n개 반환
z.info() # 전처리(데이터 정리) 하기전 결측치 *확인*

# 인덱싱
print(z.iloc[1]) 
print(z.iloc[1,2])

print(z.loc['c'])
print(z.loc['c', 'city'])

# 슬라이싱 [시작인덱스:끝인덱스], [시작라벨명: 끝라벨명]
print(z.iloc[0:2, 0:1]) #[행슬라이싱, 열슬라이싱]
print(z.loc['a':'b', 'name':'age']) #[행슬라이싱, 열슬라이싱]


# 새로운 열 추가 ['새로운열'] =  새로운값,  .assign(새로운열=새로운값)
z['score'] = [100,85,95] # 파괴적 (원본 수정)
print(z)
g = z.assign(score2 = [87, 65, 78]) # 비파괴적 ( 새로운 판다스 반환 )
print(g)
print(z)

# 특정한 값 수정 [기존열] = 수정할값
z['age'] = [31, 52, 40]
print(z)

z.loc['b', 'age'] = 70
print(z)

z.iloc[0,2] = 'ansan'
print(z) 

# 여러개 한번에 수정
# loc[[시작라벨:끝라벨], 수정할컬럼라벨] = [새로운값]
# iloc[[시작인덱스:끝인덱스], 수정할컬럼인덱스] = [새로운값]
z.loc[['a','b'], 'score'] =[10,20]
print(z)

# 필터링
cont1 = z['score'] > 70
print(cont1)
print(z[cont1])

cont2 = z['age'] >35
print(z[cont1 & cont2])
print(z[cont1 | cont2])

# 필터링 조건으로 새로운 열 추가 또는 수정
z.loc[z['score'] > 70, 'passed'] = True
z.loc[z['score']<= 70, 'passed'] = False
print(z)

# 열(컬럼) 이름 수정 
z = z.rename(columns={'city':'도시','age':'나이'})
print(z)

# 집계
print(z.describe()) # 수치 자료들을 집계 요약
print(z['나이'].sum()) # [열이름].집계함수
print(z['score'].mean())
print(z['passed'].value_counts())