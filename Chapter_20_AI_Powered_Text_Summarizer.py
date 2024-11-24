from transformers import pipeline

# Initialize a summarization pipeline
summarizer = summarizer = pipeline("summarization")
pipeline("summarization")

# Define the long text you want to summarize
text = """
Your long text goes here...
"""

# Generate the summary
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
print(summary[0]['summary_text'])