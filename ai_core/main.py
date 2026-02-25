from llm_client import send_chat # Import the send_chat function from the llm_client module

if __name__ == "__main__":

    simple_prompt = "Hey, What's up?" # Define a simple prompt to ask the AI assistant
    complex_prompt = "Ready to shoot the breeze on which LLM API is better—Gemini or OpenAI?" # Define a more complex prompt to ask the AI assistant

    print("--------SIMPLE PROMPT--------")
    response1 = send_chat(simple_prompt) # Send the simple prompt to the AI assistant and store the response
    print(response1.choices[0].message.content) # Print the content of the response from the AI assistant

    print("\n--------COMPLEX PROMPT--------")
    response2 = send_chat(complex_prompt) # Send the complex prompt to the AI assistant and store the response
    print(response2.choices[0].message.content) # Print the content of the response from the AI assistant
    