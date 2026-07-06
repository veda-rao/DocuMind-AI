import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_llm():
    """
    Return Gemini model.
    """
    return genai.GenerativeModel(
        model_name="gemini-2.5-flash"
    )


def generate_response(prompt: str) -> str:
    """
    Generate response from Gemini.
    """

    model = get_llm()

    response = model.generate_content(prompt)

    return response.text