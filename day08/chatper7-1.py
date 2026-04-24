# ㅔ 410
# OS 모듈
import os
print(os.name) # nt : 윈도우 뜻
print(os.getcwd()) # 현재 최상위 폴더
print(os.listdir()) # 현재 최상위 폴더의 내부 요소

os.mkdir('hello') # 폴더 생성
os.rmdir('hello') # 폴더 삭제

with open('./day08/original.txt', 'w') as file:
    file.write('hello')

os.rename('./day08/original.txt', './day08/new.txt') # 파일명 변경
os.remove('./day08/new.txt') # 파일 삭제

def read_folder(path):
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
        else:
            print("파일: ",item)
read_folder("./")

# datetime 모듈
import datetime

print(datetime.datetime.now())
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
# 형식 : Y 년 m 월 d일 H시 M분 S초
now.strftime('%Y-%m-%d %H:%M:%S') # 형식 만들기

#시간 계산
now.replace(year=(now.year+1), month=(now.month+1))

# time 모듈
import time
time.sleep(3) # 3초간 일시정지 # 스레드 일시정지, 스레드란? 코드가 실행되는 흐름단위

# urllib 모듈
from urllib import request
target = request.urlopen("https://google.com")
output = target.read()
print(output)

