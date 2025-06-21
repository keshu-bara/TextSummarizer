from transformers import pipeline

def summarize_text(text, model_name="facebook/bart-large-cnn", max_len=150, min_len=40):
    """
    Summarize a given text using a pretrained transformer model.

    Parameters:
        text (str): The text to summarize.
        model_name (str): Pretrained model name from Hugging Face.
        max_len (int): Maximum token length of summary.
        min_len (int): Minimum token length of summary.

    Returns:
        str: The summarized text.
    """
    summarizer = pipeline("summarization", model=model_name)
    summary = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=True,         # allows sentence variation
        early_stopping=True     # stops at sentence end
    )
    return summary[0]['summary_text']

if __name__ == "__main__":

    print(summarize_text("""Sure thing, Keshav! Here’s a sample 300-word speech that you can adapt depending on your audience or event. I’ve kept it general-purpose, touching on motivation and personal growth:

    ---

    **Good morning everyone,**

    It’s an absolute honor to stand before you today. I want to speak briefly about something we all strive for, regardless of age, background, or ambition: *growth*.

    Growth isn’t always flashy. It doesn’t always come with applause or medals. Most of the time, it comes quietly—through challenges, setbacks, or the moments when we choose effort over ease. It shows up when we stay late to finish what we started, when we raise our hands even if we’re unsure, or when we stand up after stumbling—again and again.

    Each of us here carries potential far greater than we realize. The only thing standing between where we are and where we want to be is the courage to keep moving forward. Not perfectly. Just forward.

    You may face fear, doubt, or even failure. But don’t let them stop you. Let them teach you. Let them sharpen your instincts and deepen your strength. Remember, diamonds are only formed under pressure.

    Whether you’re chasing a dream, building a better version of yourself, or simply trying to make each day a little brighter—keep going. Celebrate the small wins. Learn from the losses. And above all, believe that you are capable of incredible things.

    So as you leave here today, I hope you carry this truth with you: your story is still unfolding. You are the author. And every choice you make—big or small—is a sentence that shapes your legacy.

    Thank you.

    ---

    Would you like it to be more specific—say, for a school farewell, leadership conference, or personal event? I’d love to help you tailor it!
    """))