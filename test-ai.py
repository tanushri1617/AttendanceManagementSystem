import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv(".env")
token = os.getenv("HF_TOKEN")

if not token:
    print("ERROR: HF_TOKEN not found in .env file.")
else:
    try:
        client = InferenceClient(api_key=token)
        print("Connecting to Hugging Face AI...")

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant for a student attendance management system."
                },
                {
                    "role": "user",
                    "content": "Reply with exactly: AI connection successful!"
                }
            ],
            max_tokens=50
        )

        print(response.choices[0].message.content)

    except Exception as error:
        print("AI connection failed.")
        print(type(error).__name__, error)