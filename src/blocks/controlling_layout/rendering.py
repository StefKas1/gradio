import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown("Row 1")
            textbox = gr.Textbox()
        with gr.Column():
            gr.Markdown("Row 2")
            textbox.unrender()
        with gr.Column():
            gr.Markdown("Row 3")
            textbox.render()

demo.launch()
