from llm_client import send_chat

# Example conversation format:
if __name__ == "__main__":

    # conversation = [
    #     {"role": "system", "text": "You are an enterprise AI assistant."},
    #     {"role": "user", "text": "Hey, what's up?"}
    # ]
    conversation = [
    {"role": "system", "text": "You are a strict financial risk analyst. Respond concisely."},
    {"role": "user", "text": "Analyze Tesla stock."}
]

    print("------ RESPONSE ------")
    print(send_chat(conversation))