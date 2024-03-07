from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os

#Todo - Add .env

app = FastAPI()

load_dotenv()
openai_key = os.getenv('openai_key')

@app.get("/")
async def root():

    client = OpenAI(api_key=openai_key)

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                "type": "image_url",
                "image_url": {
                    "url": "https://files.worldwildlife.org/wwfcmsprod/images/Tiger_resting_Bandhavgarh_National_Park_India/hero_full/77ic6i4qdj_Medium_WW226365.jpg",
                },
                },
            ],
            }
        ],
        max_tokens=300,
    )

    print(response.choices[0])

    return {'message' : response.choices[0].message.content}
