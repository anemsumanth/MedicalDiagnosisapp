from cmd import PROMPT
from http import client
import os
from urllib import response
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))


def get_diagnosis(symptoms: list[str]) -> str:
    prompt = f"Patient has symptoms: {','.join(symptoms)}. suggest possible medical diagnoses suggest me possible cure for the same"

    response=client.chat.completions.create(
        model="gpt-4",
        messages=[
            
            {"role":"system", "content": "you are helpful medical assistant"},
            {"role":"user", "content": prompt},
            
            ]
        )
    return response.choices[0].message.content.strip()