# Gradio

## Links

- Documentation: https://www.gradio.app/docs

## Run gradio app modes

**Normal mode**

```bash
python app.py
```

**Hot reload mode**

```bash
gradio app.py
```

**Vibe mode**

```bash
gradio --vibe app.py
```

**Gradio sketch mode - without writing code**

```bash
gradio sketch
```

## Cache examples

In `gr.Interface()` add argument `cache_examples=True`. This will run all of the examples and save the outputs when you call the `launch()` method. This data will be saved in a directory called `gradio_cached_examples` in your working directory by default. You can also set this directory with the `GRADIO_EXAMPLES_CACHE` environment variable, which can be either an absolute path or a relative path to your working directory.

Whenever a user clicks on an example, the output will automatically be populated in the app now, using data from this cached directory instead of actually running the function.

Keep in mind once the cache is generated, it will not be updated automatically in future launches. If the examples or function logic change, delete the cache folder to clear the cache and rebuild it with another `launch()`.

## Sharing app

When you run this code, a public URL will be generated for your demo in a matter of seconds, something like:

```python
demo.launch(share=True)  # Share your demo with just 1 extra parameter
```

## Collection information

- Community-built custom components: https://www.gradio.app/custom-components/gallery
