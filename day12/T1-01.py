# numpy : 배열 기반(위치(인덱스)), 공학 수치 계산
# pandas : 테이블 기반(라벨(인덱스)), 전처리/필터링(+numpy)
    # 1차원 : series
    # 2차원 : dataframe


import pandas as pd

print(pd.__version__)

# series
x = [10,20,30,40] # 리스트
z = pd.Series(x)
print(z)
#0    10   #  0 ~ 3 : 각 요소들의 인덱스 
#1    20   # 10 ~ 40 : 각 요소들의 값
#2    30
#3    40
#dtype: int64 # 데이터 타입

# 각 요소들의 라벨 포함하기
y = ['a', 'b', 'c', 'd']
z = pd.Series(x, index=y) # index에 라벨(목록) 대입
print(z)
# a    10   # a ~ d : 각 요소들의 인덱스(라벨)
# b    20
# c    30
# d    40
# dtype: int64


# 딕셔너리 으로 생성
dic = { 'apple': 1, 'banana':2 , 'cherry':'결측'}
z = pd.Series(dic)
print(z)
# apple      1
# banana     2
# cherry    결측
# dtype: object

# 주요 속성 확인
print(z.dtype) # object
print(z.index) # Index(['apple', 'banana', 'cherry'], dtype='str')
print(z.values) # 값 반환 [1 2 '결측']
print(z.head()) # .head(n) 상위 n개만 출력(확인용) 기본값 5
print(z.tail()) # .tail(n) 하위 n개만 출력(확인용) 기본값 5
print(z.iloc[0]) # .iloc[인덱스 번호], 라벨이 아닌 위치로 조회

# 인덱싱
print(z.iloc[0]) # iloc[인덱스 번호]
print(z.loc['apple']) # loc[라벨명] 라벨명으로 조회
print(z.loc['apple':'banana']) # loc[시작라벨 : 끝라벨] 라밸명으로 슬라이싱

# 데이터 수정
z['apple'] = 10 # [라벨명] = 새로운값
print(z)
print(z['apple']) # 라벨명으로 호출 가능

# 데이터 추가
z['berry'] = 40 # [새로운라벨명] = 새로운값
print(z)

# 판다스 합치기
x = pd.Series([10,20,30], index=['a','b','c'])
y = pd.Series([40,50], index=['d','e'])
z = pd.concat([x,y])
print(z)

# 라벨 이름 변경
z = z.rename({'a':'apple'}) # .rename({'기존' : '새로운'})
print(z)

# 필터링
print(z[z>30]) # 30초과 필터링

x = z[ (z <25) | (z > 35)]
print(x)
x = z[ (z > 25) & ( z < 35)]
print(x)

z[z>30] = z[z>30] +10  # 30초과 한 요소값에 더한 후에 30 초과한 요소에만 대입
print(z)


# 통계
print(z.sum()) # 합계
print(z.mean()) # 평균
print(z.max()) # 최댓값
print(z.min()) # 최솟값
print(z.median()) # 중앙값
print(z.var()) # 분산
print(z.std()) # 표준편차
print(z.count()) # 요소개수
print(z.value_counts()) # 각 요소별 중복 개수
print(z.value_counts(normalize=True)) # 각 요소가 전체에서 차지 하는 비율(0~1)


# 정렬
x = z.sort_index() # 인덱스(라벨) 기준의 정렬
print(x)
x = z.sort_values() # 값 기준의 정렬
print(x)
x = z.sort_index(ascending=False) # 내림차순
print(x)
x = z.sort_values(ascending=False)
print(x)

# 그룹  .groupby(level=0).집계함수() 그룹이후에 집계
# .groupby(level=0).agg(['집계함수명', '집계함수명'])
z = pd.Series([10,20,30,10,20,30]
              , index=['a','b','a','b','a','b'])
x = z.groupby(level=0).sum() # 인덱스(라벨) 별 총합계
print(x)

x = z.groupby(level=0).mean() # 인덱스(라벨) 별 평균
print(x)

x = z.groupby(level=0).agg(['sum','mean','count']) # 여러개 집계 함수 agg로 묶어서 표현 가능
print(x)