

# 타입확인, type(자료)

print(type(52)) # integer
print(type(52.273)) # float , 부동 소수점

# 지수 표현 : 지수 승 표현 방법,  자료e지수승
0.52273e2  # 52.273
0.52273e-2 # 0.0052273

# 연산자
print(5+7) # 12
print(5-7) # -2
print(5*7) # 35
print(5/7) # 0.714~~
print(10//3) # 3 , 몫
print(10%2) # 1 , 나머지
print(2**3) # 8 , 제곱 연산자

print("안녕"+"하세요"*3) # 안녕하세요하세요하세요


# 변수 : 하나의 자료를 저장하는 (메모리) 공간

pi = 3.141592 # 같다라는 뜻이 아닌 우변의 값을 좌변에 넣는다 저장한다

print(pi) # 변수 참조, 변수가 갖는 자료 반환
print(pi+pi)
#print(pi+"입니다") # 오류
print(pi, "입니다")

#타입의 유연성 * 동적타입, 단점 : 타입 식별이 어렵다.
# 자바 or c언어, int pi = 3

#복합 대입 연산자
number = 100
number += 10
print(number) # 110
number -= 10
print(number) # 100
number *= 10 # 1000
number /= 10 # 100
number %= 3 # 1
number **= 3 # 1


# 사용자 입력, input(),   주의할점 : 콘솔에 입력하는 구조로 무조건 *문자열*로 변환됨
String = input("입력 : ")
print("입력한값: "+String)
print(type(String)) # str

# 문자열을 숫자로 변환하기, 사용처 : input, HTTP 문자열통신(API, JSON 등)
string_a = input("입력 A>") # str
int_a = int(string_a) # int
string_b = type(int(input("입력 B>"))) # int

string_c = type(float(input("입력 C> "))) # 다른것들도 가능

# 타입 변환 해야 되는 이유 : 자료 사용할 때 서로 다른 타입간의 예외가 발생할 수 있어서

# 숫자를 문자열로 변환하기
pi = 3.141592
print(type(str(pi))) # str



