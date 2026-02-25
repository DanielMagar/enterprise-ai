from llm_client import send_chat

# Example conversation format:
if __name__ == "__main__":

    # conversation = [
    #     {"role": "system", "text": "You are an enterprise AI assistant."},
    #     {"role": "user", "text": "Hey, what's up?"}
    # ]
#     conversation = [
#     {"role": "system", "text": "You are a strict financial risk analyst. Respond concisely."},
#     {"role": "user", "text": "Analyze Tesla stock."}
# ]

    conversation = [
        {
            "role": "system",
            "text": "You are a senior AI strategy consultant advising enterprise leadership. Provide structured, concise, business-focused insights with clear risks and ROI implications."
        },
        {
            "role": "user",
            "text": (
                "We are evaluating whether to adopt OpenAI or Gemini for our enterprise AI roadmap. "
                "Provide a comparison focusing on cost, scalability, vendor lock-in, compliance, "
                "and long-term strategic risk. End with a clear recommendation."
            )
        }
    ]
    print("------ RESPONSE ------")
    print(send_chat(conversation))