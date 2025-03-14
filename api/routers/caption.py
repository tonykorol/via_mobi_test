from fastapi import APIRouter, File, UploadFile, Depends
from starlette.status import HTTP_200_OK

from api.schemas.caption import GetCaptionResponse
from api.services.caption import CaptionService

router = APIRouter(prefix='/caption')

@router.post(
    path='/',
    status_code=HTTP_200_OK,
    response_model=GetCaptionResponse
)
async def get_caption(
        model: str,
        file: UploadFile = File(...),
        service: CaptionService = Depends(CaptionService),
):
    caption = await service.get_caption(file=file, model=model)
    return GetCaptionResponse(caption=caption)
