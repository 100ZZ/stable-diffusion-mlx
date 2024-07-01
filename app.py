import gradio as gr
import subprocess

def generate_image(prompt, model, n_images):
    command = [
        "python", "txt2image.py", prompt,
        "--n_images", str(n_images),
        "--model", model
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return "Error", result.stderr
    return "out.png", result.stdout

with gr.Blocks() as demo:
    gr.processing_utils.ANALYTICS_ENABLED = False
    gr.Markdown("# Stable Diffusion Image Generator")
    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(label="Enter your prompt")
            model = gr.Dropdown(label="Select model", choices=["sd", "sdxl"], value="sdxl")
            n_images = gr.Slider(label="Number of images", minimum=1, maximum=10, value=1, step=1)
            btn = gr.Button("Generate Image")
        with gr.Column():
            output_image = gr.Image(label="Generated Image")
            output_text = gr.Textbox(label="Output Message")

    btn.click(generate_image, inputs=[prompt, model, n_images], outputs=[output_image, output_text])

demo.launch()