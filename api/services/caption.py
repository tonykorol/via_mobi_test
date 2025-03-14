from io import BytesIO

from fastapi import File
from PIL import Image

from api.utils.caption_generator import CaptionGenerator
from api.utils.generator_models import models


class CaptionService:

    async def get_caption(self, file: File, model: str):
        """
        Чтение файла и получение описания изображения

        :param model:
        :param file:
        :return:
        """
        model, processor = self.choice_model(model)
        image = await self.read_file(file)
        cg = CaptionGenerator(model, processor)
        return await cg.generate_caption(image)

    @staticmethod
    async def read_file(file: File) -> Image:
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        return image

    @staticmethod
    def choice_model(model):
        match model:
            case 'BLIP-Base':
                return models['BLIP-Base']['model'], models['BLIP-Base']['processor']
            case 'BLIP-Large':
                return models['BLIP-Large']['model'], models['BLIP-Large']['processor']

