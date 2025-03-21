from google import genai
from google.genai import types

from credentials import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Write a poem about a magic backpack."],
    config=types.GenerateContentConfig(
        temperature=0.7,
        top_p=0.8,
        top_k=40,
        max_output_tokens=256,
    )
)
print(response.text)
