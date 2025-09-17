import gradio as gr

with gr.Blocks() as demo:
    with gr.Row(equal_height=True):
        btn1 = gr.Button("Button 1")
        btn2 = gr.Button("Button 2")

demo.launch()
