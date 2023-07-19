import gradio as gr
from PIL import Image
import numpy as np
import sys
sys.path.append("./Scripts/")
from Scripts import mask  # maskモジュールをインポート
from Scripts import tagger  # taggerモジュールをインポート
from Scripts import Kakikomi
import os
from datetime import datetime

def image_generation(init_image: Image, max_size: str,prompt: str, strength:str):
    max_size = int(max_size)
    strength = float(strength)

    mode = "MaskOFF"
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"output_image_{timestamp}.png"
    output_image = Kakikomi.main(init_image, mask_image, mode , max_size=max_size,prompt=prompt, strength=strength)
    output_image.save(os.path.join(output_folder, output_filename))
    return output_image

def image_generation_Mask(init_image: Image, mask_image: Image, max_size: str, prompt: str, strength:str):
    max_size = int(max_size)
    strength = float(strength)

    if mask_image == None:
        mode = "MaskOFF"
    else:
        mode = "MaskON"
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"output_image_{timestamp}.png"
    output_image = Kakikomi.main(init_image, mask_image, mode, max_size=max_size, prompt=prompt, strength=strength)
    output_image.save(os.path.join(output_folder, output_filename))
    return output_image


def mask_generation(image: Image):
    result = mask.main(image)
    return result

# モデルをグローバル変数として保持します
model = None
def prompt_generation(image: Image):
    global model
    if model is None:
        model = tagger.modelLoad()
    tags = tagger.main(image, model)
    return tags


with gr.Blocks() as ui:
    with gr.Tab("KakikomiImage"):
        with gr.Row():
            with gr.Column():
                input_image = gr.Image(type="pil",label="PreImage")
                with gr.Row():
                    max_size = gr.Textbox(label="Enter max_size",value = "960")
                    strength = gr.Slider(minimum=0, maximum=1, value=0.4, step=0.1, label="strength", interactive=True )

            with gr.Column():
                prompt = gr.Textbox(label="prompt",lines = 5)
                prompt_btn = gr.Button("PromptGenerate")
                prompt_btn.click(fn=prompt_generation, inputs=input_image, outputs=prompt)
                mask_image = None
                output=gr.Image(elem_id="output_image")
                inputs=[input_image,max_size,prompt,strength]
                image_btn = gr.Button("ImageGenerate")
                image_btn.click(fn=image_generation, inputs=inputs, outputs=output)

    with gr.Tab("Inpaint"):
        with gr.Row():
            with gr.Column():
                input_image = gr.Image(type="pil",label="PreImage")
                mask_image = gr.Image(type="pil",label="MaskImage")
                mask_btn = gr.Button("MaskGenerate")
                mask_btn.click(fn=mask_generation, inputs=input_image, outputs=mask_image)
                with gr.Row():
                    max_size = gr.Textbox(label="Enter max_size",value = "960")
                    strength = gr.Slider(minimum=0, maximum=1, value=0.4, step=0.1, label="strength", interactive=True )


            with gr.Column():
                prompt = gr.Textbox(label="prompt",lines = 5)
                prompt_btn = gr.Button("PromptGenerate")
                prompt_btn.click(fn=prompt_generation, inputs=input_image, outputs=prompt)
                output=gr.Image(elem_id="output_image")
                inputs=[input_image,mask_image,max_size,prompt,strength]
                image_btn = gr.Button("ImageGenerate")
                image_btn.click(fn=image_generation_Mask, inputs=inputs, outputs=output)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "share":
            ui.launch(share=True,enable_queue=True)
        else:
            ui.launch(share=False,enable_queue=True)

    else:
        ui.launch(share=False,enable_queue=True)
