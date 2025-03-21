from google import genai

import PIL.Image
from credentials import GOOGLE_API_KEY

image_path_1 = "images/dog.jpg"
image_path_2 = "images/cat.jpg"
image_path_3 = "images/crocodile.jpg"

image_1 = PIL.Image.open(image_path_1)
image_2 = PIL.Image.open(image_path_2)
image_3 = PIL.Image.open(image_path_3)

client = genai.Client(api_key=GOOGLE_API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents=["What do these images have in common?", image_1, image_2, image_3])

print(response.text)
