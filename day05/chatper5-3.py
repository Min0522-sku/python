
# 튜플 : ( ) 소괄호 이용하여 여러 자료들을 감싼 자료형 , 단*) 수정이 안된다

# 튜플 선언
tuple_test = ( 10, 20, 30)
print(tuple_test)

# 요소 호출, 인덱스 사용
print(tuple_test[0])

# 주의할점 : 수정 안된다.
# tuple_test[0] = 40 # TypeError: 'tuple' object does not support item assignment

# 요소가 1개인 경우에는 , 쉼표 넣어준다
tuple_test2 = (272,)


[a, b] = [10, 20] # 오른쪽에 있는 리스트의 자료들을 왼쪽 변수에 대입
(c, d) = (10, 20)
print("a :", a) # 10
print("b :", b) # 20
print("c :", c) # 10
print("d :", d) # 20

# 튜플은 소괄호 생략해도 된다.
tuple_test3 = 10, 20, 30, 40
a, b, c = 10, 20, 30

# 튜플 이용한 스왑(교체)
a, b = 10, 20 # a = 10, b = 20
a, b = b, a # a = 20, b = 10


# 함수 리턴 값
def test():
    return 10, 20 # 튜플, 리스트, 딕셔너리 다 가능 (10, 20)  [10, 20]  { 'a':10, 'b':20 }



