import numpy as np

# 배열의 주요 속성
x = np.array([[1,2,3],[4,5,6]])
print(x.shape) # .shape 현재 배열의 크기 (튜플)반환,  (행개수, 열개수)

x = np.array([1.0,2.0,3.0])
print(x.dtype) # .dtype 현재 배열내 데이터 타입 반환

x = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(x.size) # .size 헌재 배열내 모든 요소 수

x = np.array([1,2,3])
print(x.ndim) # .ndim 현재 배열의 차원수
x = np.array([[[1],[2], [3],[4]]])
print(x.ndim) # 3

x = np.array([[1,2], [3,4], [7,0]])
print(x.flat) # .flat 다차원 배열을 1차원으로 변환
for element in x.flat:
    print(element)

# 배열의 데이터 타입
# .array(자료, dtype = numpy.타입명)
x = np.array([1,2,3], dtype=np.int32)
print(x.dtype)
# 필요에 따라 적절하게 bit 선택
x = np.array([1.0,2.0,3.0], dtype=np.float64)
print(x.dtype) # 더큰 bit 일수록 더욱 오차를 최소화하여 정밀해질 수 있음

x = np.array([True, False, True], dtype=np.bool_)
print(x.dtype) # boll 논리형

x = np.array(['apple', 'banana', 'cherry'], dtype=np.bytes_)
print(x.dtype) # 문자열을 바이트 형태로 저장

x = np.array([1.5,2.3,3.7])
print(x.dtype) # float64
y = x.astype(np.int32) # float 64 -> int32   .astype(numppy.변환할타입명) , 타입변환
print(y) # [1 2 3] , int 정수형으로 바뀌면서 소수점을 표현할 수 없으므로 소수점 잘림

