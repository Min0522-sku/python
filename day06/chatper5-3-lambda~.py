# 콜백 함수 : 함수의 매개변수로 함수를 사용하는 함수
# 콜백 함수 예시
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello) # 함수 자체
# call_10_times(print_hello()) # 함수실행 예외 발생

# map(), filter()
# map(함수, 리스트) : 리스트의 요소를 *하나씩* 함수 매개변수에 대입하여 *새로운리스트* 반환
# filter(함수, 리스트) : 리스트의 요소를 *하나씩* 함수매개변수에 대입하여 참(True) 인경우 *새로운리스트* 반환

def power(item):
    return item * item
def under_3(item):
    return item < 3
list_input_a = [1,2,3,4,5]

# map()
print("map(power, list_input_a) :" , map(power, list_input_a))
print("map(power, list_input_a) :" , list(map(power, list_input_a)))
# filter()
print("filter(under_3, list_input_a) :", filter(under_3, list_input_a))
print("filter(under_3, list_input_a) :", list(filter(under_3, list_input_a)))

# p 336
# 제너레이터 : 함수 내부에 yield 키워드를 사용하며 next() 함수를 외부에서 호출하여 yield 키워드 까지 실행한다

def test():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")
test() # 함수 호출시 실행 안됨
output = test()  # 함수 반환값을 변수에 저장
print("D") 
a = next(output) # 함수 반환 값이 저장된 변수를 next에 대입
print(a) # yield 까지 실행되고 yield 반환값이 반환
print("E")
b = next(output)
print(b)
print("F")
# c = next(output) # 다음 yield 존재하지 않기 때문에 예외 발생
# print(c)

# 람다 : 함수 선언 간단하게 하는 문법
# lambda 매개변수 : 반환값

# JS 선언적 함수 콜백
#function 함수명(){} , const 함수명  = () => { }
#<button onClick = {함수명}>
# JS 람다(화살표) 콜백
#<button onClick = { () => {}} >

# 방법1 : 재사용 가능하다
power = lambda x : x * x
output_a = map(power, list_input_a)
# 방법2 : 재사용 안된다.
output_a = map(lambda x : x * x, list_input_a)


# 파일처리
# open(파일경로, 읽기모드)
# 읽기모드 : w 새로쓰기 a 이어쓰기 r 읽기모드
# open 함수 이용하여 지정한 경로의 파일 쓰기
file = open('./day06/basic.txt', 'w') # 현재 .py 파일 폴더내 basic.txt 파일 생성
# .write(출력할내용) 함수 이용한 내보내기 
file.write("안녕하세요")
# .close() 함수 이용한 안전하게 스트림 닫기
file.close()
# with 키워드 이용한 .close() 자동 닫기
with open('./day06/basic2.txt', 'w') as file :
    file.write('안녕 파이썬 프로그래밍2..!')

# 스트림이란? 데이터가 흐르는 길, 바이트 단위, 프로그래밍 언어가 외부 자료와 연결(파일, JDBC, 네트워크 등)

# .read() 함수 이용한 파일 읽어오기
with open('./day06/basic.txt', 'r') as file:
    contents = file.read()
print(contents)