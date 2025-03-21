from google import genai

import PIL.Image
from credentials import GOOGLE_API_KEY

image = PIL.Image.open('images/space.jpg')

client = genai.Client(api_key=GOOGLE_API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["What is this image?", image])

print(response.text)
