# 리스트 : 여려 자료들을 모아 하나의 자료로 구성
# [ , , , , ]

list_a = [273, 32, "문자열", True]
print(list_a[0]) # 273
print(list_a[1:3]) # [32, '문자열']

list_a[1] = "변경값"
print(list_a) # 리스트내 요소값 변경 가능

#뒤에서 부터 요소 선택
print(list_a[-2]) # 문자열

# 리스트 안에 리스트 사용 가능
print(list_a[2][1]) # 자
list_a[1] = ["변경값1", "변경값2"] 
print(list_a[1][1]) # 변경값 2
#존재하지 않는 인덱스 넣을시 오류


#리스트 연산
list_a = [1,2,3]
list_b = [4,5,6]
#연결
print(list_a+list_b) # [1,2,3,4,5,6]
#반복
print(list_b * 3) # [4,5,6,4,5,6,4,5,6]
#길이
print(len(list_a)) # 3

# 리스트에 요소 추가, append(요소) insert(위치, 요소)
list_a.append(4)
print(list_a) # [1,2,3,4]
list_a.insert(0, 10)
print(list_a) # [10,1,2,3,4]

# 리스트에 요소 제거 del, .pop(), remove()
del list_a[1] # 1번 인덱스 요소 삭제
print(list_a) # [10,2,3,4]
list_a.pop() # 인덱스 지정 안할시 맨 마지막 인덱스 삭제
print(list_a) # [10,2,3]
list_a.remove(10) # 해당 자료가 존재하면 삭제
print(list_a) # [2,3]

# 모든 요소 삭제
list_a.clear()
print(list_a) # []

# 리스트 슬라이싱
# [시작인덱스: 끝인덱스 : 단계]
list_b += list_b # [4,5,6,4,5,6]
print(list_b[::-1]) # [6,5,4,6,5,4] 역순 출력
print(list_b[0::2]) # [4,6,5] 0번 인덱스부터 마지막인덱스 까지 2칸씩 이동

# .sort() 오름차순 , .sort(reverse=True)내림차순
list_e = [52, 273, 103, 32, 275, 1, 7]
list_e.sort()
print(list_e)
list_e.sort(reverse=True)
print(list_e)

# in , 내부에 있는지 확인
print(1 in list_e) # True
print(2 in list_e) # False
print(2 not in list_e) # True


# 리스트와 반목문 
# # for 반복자 in 반복할 수 있는것:
        # 코드
array = [273,32,103,57,52]
for element in array:
    print(element)

for i in "안녕하세요":
    print(i)

# 중첩 리스트 # 중첩 반복문 # 2차원 리스트
list_of_list = [
    [1,2,3], # 1행 3열
    [4,5,6,7], # 2행 4열
    [8,9] # 3행 2열
]

for row in list_of_list:
    print(row) # 각행 출력
    for col in row:
        print(col) # 각행의 열 출력

# 전개 연산자  *
list_c = [1,2,3]
print(list_c) # [1, 2, 3] 리스트 자체 출력
print(*list_c) # 1 2 3 리스트 그 자체가 아닌 리스트는 첫번째 인덱스르 참조한다.

print([list_c, list_c]) # 2차원 리스트 구성
print([*list_c, *list_c]) # 1차원 리스트 구성


# 딕셔너리 4-2
# 키를 기반으로 값을 저장하는것  vs JS(JSON) vs JAVA(map,DTO)

#선언
dict_a = {"name" : "어벤저스 엔드게임", "type" : "히어로 무비"}
#호출
print(dict_a)
print(dict_a["name"])
print(dict_a.get("name"))
# 없는키 호출시 오류 발생


# 값 추가    딕셔너리 명['key]=value
dict_a["price"] = 1000
print(dict_a)

dict_a["price"] = 2000 # 존재하는 key 이면 value 수정 key는 중복 없음

# 키, 값 삭제 del 딕셔너리명['key']
del dict_a["price"]
print(dict_a)

# 반복문과 딕셔너리
# for 키가 들어갈 변수명 in 딕셔너리이름:
    # 실행문

for key in dict_a:
    print(key, ':', dict_a[key])
    


# 범위 range
# 숫자 1개만 넣는경우 0 부터 n-1 까지 리스트로 반환
print(list(range(5))) # [0,1,2,3,4]
# 숫자 2개만 넣는경우 n 부터 k-1 까지 리스트로 반환
print(list(range(2,8)))
# 숫자 3개만 넣는경우 n 부터 k-1 까지 j 만큼 증가 하면서 리스트로 반환
print(list(range(2, 8, 2)))

# 반복문과 범위 활용
# for 반복변수 in range() :

for i in range(1, 11, 2) :
    print(i)

for i in range(len(array)) :
    print(array[i])

# 역순 출력
for i in range(4, -1, -1):  # 4부터 0 까지 1씩 감소 
    print(i)
for i in reversed(range(5)):
    print(i)



# while 반복문
#while True: # 무한 반복
#    print(".", end="") # end="" 줄바꿈이 이루어 지지 않음

# 1부터 10까지 출력
i = 1
while i <11 :
    print(i)
    i +=1


list_test = [1, 2, 1, 2]
while 2 in list_test:
    list_test.remove(2)
print(list_test) # [1, 1]

# break 키워드
i = 0
while True:
    print(i)
    i+=1
    msg = input("종료할까요? >")
    if msg in ['Y', 'y']:
        break

# continue 키워드
numbers = [5, 15, 6, 20, 7, 25]
for num in numbers:
    if num < 10:
        continue
    print(num)
