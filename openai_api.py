import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ad_copy(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert ad copywriter."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.8
    )
    return response.choices[0].message["content"]
