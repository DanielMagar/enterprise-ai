import os
from dotenv import load_dotenv
from openai import OpenAI
from google import genai

load_dotenv()

# ===============================
# CONFIGURATION
# ===============================
PROVIDER = os.getenv("LLM_PROVIDER", "openai")  # "openai" or "gemini"

OPENAI_MODEL = "gpt-5.2"
GEMINI_MODEL = "gemini-2.5-flash"

# ===============================
# INTERNAL UNIFIED SCHEMA
# ===============================
# We define ONE conversation format internally
# This format never changes across providers

"""
conversation = [
    {"role": "system", "text": "..."},
    {"role": "user", "text": "..."},
    {"role": "assistant", "text": "..."},
]
"""

# ===============================
# ADAPTERS
# ===============================

def _to_openai_messages(conversation):  # OpenAI expects "content" instead of "text"
    return [
        {"role": msg["role"], "content": msg["text"]}
        for msg in conversation
    ]


def _to_gemini_contents(conversation): # Gemini expects "parts" with "text", and "model" instead of "assistant"
    gemini_messages = []

    for msg in conversation:
        role = msg["role"]

        # Gemini uses "model" instead of "assistant"
        if role == "assistant":
            role = "model"

        gemini_messages.append({
            "role": role,
            "parts": [{"text": msg["text"]}]
        })

    return gemini_messages


# ===============================
# MAIN SEND FUNCTION (Unified)
# ===============================

def send_chat(conversation: list) -> str: # This is the main function that the rest of the codebase will call. It takes in a conversation in our internal unified format, and then routes it to the correct provider adapter based on configuration.

    if PROVIDER == "openai":

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=_to_openai_messages(conversation)
        )

        return response.choices[0].message.content

    elif PROVIDER == "gemini":

        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=_to_gemini_contents(conversation)
        )

        return response.text

    else:
        raise ValueError("Unsupported provider")