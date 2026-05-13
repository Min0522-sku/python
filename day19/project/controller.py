
# 라우터 : 특정 도메인(주소) 묶어주는 역할
from fastapi import APIRouter

# APIRouter(prefic='/공통도메인')
# vs @RequestMapping("공통도메인")
router = APIRouter(prefix="/stats")

# 서비스 불러오기
# vs private final 
from service import stats_service
# REST API 정의
# GET
@router.get("/get")
async def all():
    return stats_service.all()

