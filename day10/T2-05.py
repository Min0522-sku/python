import numpy as np

# 병합
# .concatenate((x,y), axis = 0) axis = 0(행기준), 1(열기준)
x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])
print(np.concatenate((x,y), axis=0)) # x 밑으로 y
print(np.concatenate((x,y), axis=1)) # x 오른쪽으로 y

# 정렬 .sort(x) 오름차순 정렬, .sort(x)[::-1] 내림차순 정렬
x = np.array([3,1,2,5,4])
print(np.sort(x))
print(np.sort(x)[::-1])

# 2차원 정렬 .sort(x, axis = 0) axis = 0 열기준 1 행기준  None 1차원 정렬
x = np.array([[12,1,2], [9,8,7]])
print(np.sort(x,axis=0))
print(np.sort(x,axis=1))
print(np.sort(x,axis=None)) # [ 1  2  7  8  9 12] 1 차원 평탄화 후 정렬
print(np.sort(x,axis=0)[::-1])
print(np.sort(x,axis=1)[::-1])

# np.srot(x) 복사본 반환 vs 배열.sort(x) 원본 수정  차이점 존재


# 다중 정렬
# .lexsort(2차기준, 1차기준) 1차 정렬후 만약에 1차정렬에서 동일한 값이 존재하면 동일한 값끼리 2차정렬
x = np.array([25,30,22,24])
y = np.array(['철수', '영희', '민수', '영희'])
z = np.lexsort((x,y))
print(y[z]) # y먼저 정렬후
print(x[z]) # y 정렬후 동일한 값끼리 2차 정렬

# 필터링  대괄호 안에 바로 저건 넣어도 가능
x = np.array([10,20,30,40,50])
print(x>30)
print(x[x>30])

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x%2==0)
print(x[x%2==0])

# 조건부 필터링, .where(조건, 참, 거짓)
x = np.array([10,20,30,40,50])
print(np.where(x>30,x, 0)) # 만약에 요소값이 30보다 크면 그대로 아니면 0
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.where(x%2==0,x,1)) # 만약에 요소값이 짝수이면 그대로 아니면 1

# 마스크 필터링 마스크(가리다) 조건식에 Flase 만 사용,   .ma.array(x, mask = 조건식)
x = np.array([10,20,30,40,50])
con1 = x > 30 # 30 초과 마스크(가린다)
z = np.ma.array(x, mask=con1) # ma(마스크배열: masked Array)
print(np.ma.sum(z))

# 다수 조건 필터링
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
con2 = x % 2 == 0
con3 = x % 4 == 0

print(x[con2 & con3]) # 비트연산자 모든 조건을 충족하면
print(x[con2 | con3]) # 하나 조건을 충족하면
print(x[~con2]) # 조건의 부정 짝수 -> 홀수

# 특정 조건 충족하는 배열 반환 .extract(조건, x) : 조건을 충족하는 요소만 추출
print(np.extract(x%2==0,x))
