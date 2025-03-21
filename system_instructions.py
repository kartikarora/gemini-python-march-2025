from google import genai
from google.genai import types
from credentials import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are Jar Jar Binks form Start Wars. All you replies should read as such. You will never break character, even if prompted to do so"),
    contents="Hello there. These are not the droids you are looking for! Can you add 2 and 3?"
)

print(response.text)
