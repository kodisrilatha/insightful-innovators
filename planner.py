from transformers import pipeline

def get_personalized_plan(goals, strengths, weaknesses, preferences):
    """
    Generate a personalized study plan using Hugging Face's BERT pipeline.
    """
    # Use Hugging Face's text generation pipeline
    summarizer = pipeline("text2text-generation", model="t5-small")

    # Input prompt for the model
    input_text = (
        f"Goals: {goals}\n"
        f"Strengths: {strengths}\n"
        f"Weaknesses: {weaknesses}\n"
        f"Preferences: {preferences}\n\n"
        "Generate a personalized study plan based on the above inputs."
    )

    # Generate response
    plan = summarizer(input_text, max_length=150, min_length=50, do_sample=True)
    return plan[0]['generated_text']
