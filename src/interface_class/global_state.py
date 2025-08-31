import gradio as gr


"""
In the code, the scores array is shared between all users. 
If multiple users are accessing this demo, their scores 
will all be added to the same list, and the returned top 3 scores 
will be collected from this shared reference.
"""
scores = []


def track_score(score):
    scores.append(score)
    top_scores = sorted(scores, reverse=True)[:3]
    return top_scores


demo = gr.Interface(track_score, gr.Number(label="Score"), gr.JSON(label="Top Scores"))
demo.launch()
