import gradio as gr


def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2

example_dir = "example_data/calculator" # Must contain log.csv
demo = gr.Interface(
    calculator,
    [
        gr.Number(label="First number", info="Some info text"),
        gr.Radio(["add", "subtract", "multiply", "divide"]),
        "number",
    ],
    "number",
    examples=example_dir,
    title="Toy Calculator",
    description="Here's a sample toy calculator.",
)

demo.launch()
