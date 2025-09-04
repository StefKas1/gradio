import gradio as gr

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")

    @greet_btn.click(
        inputs=name, outputs=output
    )  # Attach event listeners using decorators
    def greet(name):
        return "Hello " + name + "!"


demo.launch()
