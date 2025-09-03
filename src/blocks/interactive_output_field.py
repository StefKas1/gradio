import gradio as gr


def greet(name):
    return "Hello " + name + "!"


with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    # Since Textbox output acts only as an output, Gradio determines that it should not be
    # made interactive. You can override the default behavior and directly configure
    # the interactivity of a Component with the boolean interactive keyword argument,
    # e.g. gr.Textbox(interactive=True).
    output = gr.Textbox(label="Output", interactive=True)
    greet_btn = gr.Button("Greet")
    greet_btn.click(
        fn=greet, inputs=name, outputs=output, api_name="greet"
    )  # Event listener

demo.launch()
