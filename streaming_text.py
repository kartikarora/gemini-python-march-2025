from google import genai
from credentials import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=["Write a poem about a magic backpack."]
)
for chunk in response:
    print(chunk.text, end="")
