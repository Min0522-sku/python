
# 라우터 : 특정 도메인(주소) 묶어주는 역할
from fastapi import APIRouter

# APIRouter(prefic='/공통도메인')
# vs @RequestMapping("공통도메인")
router = APIRouter(prefix="/api")

# 서비스 불러오기
# vs private final 
from service import item_service
# REST API 정의
# GET
@router.get("/item")
async def item(id:int):
    return item_service.item(id)

# GET
@router.get("/items")
async def items():
    return item_service.items()

# POST {"id":4, "name":"제로 콜라", "price":2500}
@router.post("/save")
async def save(item:dict):
    return item_service.save(item)

# PUT {"id":1, "name":"펩시 콜라", "price":2500}
@router.put("/update")
async def update(item:dict):
    return item_service.update(item)

# DELETE
@router.delete("/delete")
async def delete(id:int):
    return item_service.delete(id)

