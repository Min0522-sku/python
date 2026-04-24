
# 모듈 호출하기
# 표준 모듈 : 파이썬 내장 라이브러리
# 외부 모듈 : 설치형 라이브러리
# import 모듈명

import math 
print(math.sin(1)) # 호출한 모듈에서 .sin() 함수 호출,   . (접근연산자)
print(math.cos(1))
print(math.tan(1))
print(math.floor(2.5))
print(math.ceil(2.5))

from math import sin, cos, tan, floor, ceil

import math as m
print(m.sin(1))

# random 모듈
import random

print(random.random()) # 0.0 <= x < 1.0 사이의 (실수) 난수 생성
print(random.uniform(10,20)) # .uniform(시작값, 끝값) , 실수
print(random.randrange(1, 10)) # .randrange(시작값, 끝값) , 정수
print(random.choice([10,20,30,40])) # .choice([리스트]), 리스트내 랜덤 요소 1개 반환
a = [1,2,3,4,5]
print(random.shuffle(a)) # .shuffle([리스트]), 리스트내 요소들을 랜덤으로 섞는다. 원본이 수정됨
print(random.sample([1,2,3,4,5], k=3)) # .sample([리스트], k=개수), 리스트내 k개 랜덤 요소 반환
# k= ? : 키워드 매개변수, k라는 이름 갖는 매개변수에 대입

