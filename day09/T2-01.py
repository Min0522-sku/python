
# numpy 이란? 고성능 수치 계산 라이브러리
# numpy 불러오기 : import numpy
import numpy
print(numpy.__version__)

# 넘파이 배열 생성

x = numpy.array([1,2,3,4]) # .array([1차원리스트])  // 일반 리스트랑 다름
print(x)

x = numpy.array([[1,2,3], [4,5,6]]) # .array([[1차원리스트], [1차원리스트]])
print(x)

x = numpy.zeros((2,3)) # .zeros((행,열)) ,  행과 열 만큼의 0으로 초기화
print(x)

x = numpy.ones((2,3)) # .ones((행,열)) ,  행과 열 만큼의 1으로 초기화
print(x)

x = numpy.full((2,3), 10) # .full((행,열), 값) ,  행과 열만큼의 값으로 초기화
print(x)

x = numpy.arange(0,10,2) # .arange(시작, 끝, 단위) , 시작부터 끝 사이의 단위 만큼 증가한 배열
print(x)

x = numpy.linspace(0, 10, 5) # .linspace(시작, 끝, 개수) ,  시작부터 끝 사이의 개수 만큼 균등하게 나눈 배열
print(x)