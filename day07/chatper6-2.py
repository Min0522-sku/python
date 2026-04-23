
# 예외 객체 : Exception 클래스
# try ~ except 예외 클래스명 as 변수명 ~ except 예외 클래스명 as 변수명 
# 모든 예외 잡기 : *마지막 except 에 Exception 클래스 사용

num_list = [52,273,32,72,100]
try:
    number_input_a = int(input("정수입력 >")) # int() 에서 예외 발생 경우
    print(num_list[number_input_a]) # [] 에서 예외 발생 경우'
    raise NotImplementedError # 강제 예외 발생
    예외.발생() # 예상치 못한 예외는 Exception
except ValueError as e :
    print("정수만 입력하세요")
except IndexError as e:
    print("인덱스 벗어남")
except Exception as e:
    print(e)