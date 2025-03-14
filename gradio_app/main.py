import gradio as gr
from gradio_app.utils import send_request


def gradio_interface():
    with gr.Blocks() as app:
        gr.Markdown("# Image Captioning App")

        with gr.Row():
            image_input = gr.Image()
            model_dropdown = gr.Dropdown(
                choices=["BLIP-Base", "BLIP-Large"],
                label="Выберите модель",
                value="BLIP-Base"
            )

        btn = gr.Button("Сгенерировать описание", variant="primary")
        output_text = gr.Textbox(label="Описание изображения")

        btn.click(send_request, inputs=[image_input, model_dropdown], outputs=output_text)

    return app


if __name__ == "__main__":
    gradio_interface().launch()
