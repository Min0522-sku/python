
# 라우터 : 특정 도메인(주소) 묶어주는 역할
from fastapi import APIRouter

# APIRouter(prefic='/공통도메인')
# vs @RequestMapping("공통도메인")
router = APIRouter(prefix="/api")

from service import productService
# REST API 정의
# GET
@router.get("/products")
async def products():
    return productService.products()

# http://127.0.0.1:8000/api/spring
@router.get("/spring")
async def getSpring():
    return await productService.getSpring()