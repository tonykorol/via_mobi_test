import io

import torch
from PIL import Image


class CaptionGenerator:
    def __init__(self, model, processor):
        self.model = model
        self.processor = processor

    async def generate_caption(self, file) -> str:
        image = await self.convert_image_to_bytes(file)
        tensor = self.generate_tensor(image)
        output = self.get_caption(tensor)
        return self.decode_caption(output)

    @staticmethod
    async def convert_image_to_bytes(file) -> Image.Image:
        return file.convert("RGB")

    def generate_tensor(self, image) -> torch.Tensor:
        return self.processor(images=image, return_tensors="pt")

    def get_caption(self, tensor) -> torch.Tensor:
        with torch.no_grad():
            return self.model.generate(**tensor)

    def decode_caption(self, output) -> str:
        return self.processor.decode(output[0], skip_special_tokens=True)
