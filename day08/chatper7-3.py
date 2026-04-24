
# 모듈 만들기 : .py 파일 만들기와 같다
# xxxx.py 파일 생성
# 다른 .py 파일내에서 import 하여 모듈 호출

import test_module as test
radius = test.number_input()
print(test.get_circle_area(radius))
print(test.get_circumference(radius))

# 프로그램의 진입점 : __name__=="__main__"
print(__name__) # __main__

# 같은 모듈의 이름을 가지더라도 패키지 혹은 폴더가 다르면 다른 파일, 클래스 이다 


# 인터넷의 이미지 저장하기
from urllib import request
target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output) # 바이너리 데이터로 반환된다. 앞에 'b' 가 붙어있음

file = open('./day08/output.png', 'wb') # 바이너리 파일 저장시 'wb' 사용
file.write(output)
file.close()