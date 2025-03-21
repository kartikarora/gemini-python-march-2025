from google import genai

import PIL.Image
import requests
from credentials import GOOGLE_API_KEY

image_url = "https://goo.gle/instrument-img"

downloaded_image = requests.get(image_url)

client = genai.Client(api_key=GOOGLE_API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents=["What instrument is this?", downloaded_image])

print(response.text)
