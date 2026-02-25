from openai import OpenAI # Import the OpenAI client library
import os # Import the os module for interacting with the operating system
from dotenv import load_dotenv # Import the load_dotenv function from the dotenv library to load environment variables from a .env file

load_dotenv() # Load environment variables from the .env file

# Create an instance of the OpenAI client
client = OpenAI(     
 api_key = os.getenv("OPENAI_API_KEY") # Retrieve the OpenAI API key from environment variables
)

def send_chat(prompt: str): 

    response = client.chat.completions.create( # Send a chat completion request to the OpenAI API
        model = "gpt-5.2",
        messages = [ # Define the messages for the chat completion, including a system message to set the context and a user message with the prompt
            {
                "role": "system",
                "content": "You are an enterprise AI assistant. You help users with their questions and provide accurate and helpful information."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

    )
    return response
