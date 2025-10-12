# analyzer.py

from transformers import pipeline

# Let's set up our AI models when the script is first loaded.
# This is more efficient than reloading them every time we need them.

# 1. The Summarizer
# We're using the 'BART' model, which is excellent for summarizing text.
# It reads an article and writes a shorter version, just like a journalist.
print("Loading the summarization model... (This might take a moment)")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print("Summarization model loaded!")

# 2. The Sentiment Analyzer
# This model is trained to classify text as either POSITIVE or NEGATIVE.
# It's great for quickly getting the 'vibe' of the article.
print("Loading the sentiment analysis model...")
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
print("Sentiment analysis model loaded!")


def summarize_text(text):
    """
    Takes a long piece of text (our article) and returns a concise summary.
    """
    if not text or not isinstance(text, str) or len(text.strip()) < 200:
        return "The article content is too short to summarize."

    print("Generating summary...")
    try:
        # We set some limits to make sure the summary is a good length.
        # Not too long, not too short.
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        print("Summary generated successfully.")
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error during summarization: {e}")
        return f"Could not summarize the text due to an error: {e}"

def analyze_sentiment(text):
    """
    Reads a piece of text and determines if the sentiment is positive or negative.
    """
    if not text or not isinstance(text, str) or len(text.strip()) == 0:
        return "No text provided for sentiment analysis."
        
    print("Analyzing sentiment...")
    try:
        result = sentiment_analyzer(text[:512]) # Analyze the first 512 tokens for speed
        sentiment = result[0]['label']
        confidence = result[0]['score']
        print("Sentiment analysis complete.")
        # Let's make the output a bit more fun and human-readable.
        emoji = "😊" if sentiment == "POSITIVE" else "😞"
        return f"Sentiment: {sentiment} {emoji} (Confidence: {confidence:.2f})"
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return f"Could not analyze sentiment due to an error: {e}"

