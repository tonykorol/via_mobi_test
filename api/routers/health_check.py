from fastapi import APIRouter
from starlette.status import HTTP_200_OK

router = APIRouter(prefix='/health-check')

@router.get(
    path='/',
    status_code=HTTP_200_OK,
)
async def check_health():
    return {'status': 'OK'}
