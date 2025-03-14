import io

import numpy as np
from httpx import AsyncClient

from gradio_app.config import settings


def convert_to_bytes(image: np.ndarray) -> io.BytesIO:
    from PIL import Image
    pil_image = Image.fromarray(image)

    byte_io = io.BytesIO()
    pil_image.save(byte_io, format="PNG")
    byte_io.seek(0)
    return byte_io

async def send_request(image, model_name):
    if image is None:
        return "Ошибка: загрузите изображение."

    image_bytes = convert_to_bytes(image)
    files = {"file": ("image.png", image_bytes, "image/png")}
    params = {"model": model_name}

    async with AsyncClient() as client:
        # try:
        response = await client.post(settings.API_URL, files=files, params=params)
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get("caption", "Ошибка при обработке")
        # except Exception as e:
        #     return f"Ошибка запроса: {str(e)}"
