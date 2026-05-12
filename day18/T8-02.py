
# import 가져오기
import  uvicorn 
from fastapi import FastAPI 
# fastApi 객체 생성
app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("T8-02:app", host="127.0.0.1", port=8000, reload=True)

# REST 정의하기
# REST : 자원 주고 받는 상태 구조 # REST API : HTTP로 REST 구현
# 자동으로 JSON 타입으로 응답한다. vs @ResponseBody(@RestController)
# @GetMapping("/URL") vs @app.get("/URL")

@app.get("/")
async def index():
    return "안녕 파이썬웹"

# 쿼리 파라미터
@app.get("/user") # http://localhost:8000/user?name=%EC%9C%A0%EC%9E%AC%EC%84%9D&age=40
async def find_user(name, age:int): # URL?변수명=값&변수명=값 # 기본타입 str # 지정타입은 변수명:타입
    return {'name':name, 'age':age}

# 경로 파라미터
@app.get("/item/{name}/{age}") # http://localhost:8000/item/%EC%9C%A0%EC%9E%AC%EC%84%9D/40
async def find_item(name:str, age:int):
    return {'name':name, 'age':age, 'msg':'경로파라미터예시'}

# 본문(body)
@app.post("/product")
async def find_product(product:dict): # 변수명:dict # 딕셔너리 타입으로 받기
    product['msg'] = 'body'
    return product
