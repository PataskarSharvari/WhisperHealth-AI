from dotenv import load_dotenv
load_dotenv()

import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
print("GROQ_API_KEY loaded:", bool(GROQ_API_KEY))  # <-- DO THIS RIGHT HERE

import base64
from groq import Groq

def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

query = "Is there something wrong with my face?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)  # <- Explicitly pass key
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    print("Raw response:")
    print(chat_completion.model_dump_json(indent=2))

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    image_path = "acne.jpg"
    encoded = encode_image(image_path)
    result = analyze_image_with_query(query, model, encoded)
    print("AI says:")
    print(result)
