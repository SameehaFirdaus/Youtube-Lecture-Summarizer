import os
import openai

def summarize_text(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Summarize the following text: {text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
