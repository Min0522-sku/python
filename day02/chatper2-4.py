# 문자열의 format() 함수
string_a = "{}".format(10)
print(string_a, type(string_a))

format_a = "{}만원".format(5000)
print(format_a)
format_b = "{}{}{}".format(1,"문자",True) # {} 개수보다 자료개수가 적으면 오류
print(format_b)

# 특정 칸에 출력하기, {:자릿수d}
output_a = "{:5d}".format(52) # {} 안에서 공백 주의
print(output_a)
output_b = "{:05d}".format(52) # :0자릿수d 나머지 칸을 0으로 채움
print(output_b) # 00052

# 기호 붙여 출력하기, {:+d}
output_c = "{:+d}".format(52)
print(output_c) # +52
output_c = "{:+d}".format(-52)
print(output_c) # -52
output_c = "{: d}".format(52)
print(output_c) #  52
output_c = "{: d}".format(-52)
print(output_c) # -52

# 부동소수점 출력하기
output_d = "{:15f}".format(52.273)
print(output_d) #       52.273
output_d = "{:+015f}".format(52.273) # +기호, 0으로채움, 15자릿수, f 실수
print(output_d) # +0000052.273000
output_e = "{:15.3f}".format(52.2737) # .소수자릿수f, 만약에 잘린 소수점에서 반올림 된다.
print(output_e)

# 의미없는 소수점 제거하기
output_f = "{:g}".format(52.0)
print(output_f)
print(type(output_f))  # str

# 대소문자 바꾸기
a = "Hello Python"
a.upper()
b = "HELLO"
b.lower()

# 공백 제거하기,  .strip() 양쪽공백제거, .lstrip()왼쪽 , .rstrip()오른쪽
c = "          안녕하세요              "
print(c.strip())

# 문자열 찾기 .find() 왼쪽부터, .rfind() 오른쪽부터, in
output_g = "안녕안녕하세요".find("안녕")
print(output_g) # 0번 인덱스에 "안녕" 존재
print("안녕안녕하세요".rfind("안녕")) # 2번 인덱스에 "안녕" 존재

print("안녕" in "안녕하세요") # "안녕하세요" 에 "안녕" 존재 => True

# 문자열 자르기 .split(기준문자)
output_h ="10 20 30 40 50".split(" ")
print(output_h)

# f-문자열 vs .format()
print(f'{10}')
print("{}".format(10))

#도전문제 2
a = int(input("밑변 >"))
b = int(input("높이 >"))
print("빗변 :", (a**2 + b**2)**(1/2))

# 문자열 비교 : 가나다,abc 순으로 앞에 있는것이 작은 값
print("가방" == "가방") # True
print("가방" != "하마") # True
print("가방">"하마") # False 

# 범위 논리
x = 25
print(10 < x < 30)

# 논리 연산자 : and, or, not
print(not True) # False
print(True and True) # True
print(True and False) # False
print(True or False) # True
