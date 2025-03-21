from google import genai
import time
from credentials import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)
print("Uploading file...")
video_file = client.files.upload(file="video/video.mp4")

while video_file.state.name == "PROCESSING":
    print('.', end='')
    time.sleep(1)
    video_file = client.files.get(name=video_file.name)

if video_file.state.name == "FAILED":
    print("Upload failed")
    exit(1)

print('Upload complete')

response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents=[
        video_file,
        "Summarize this video. Then create a quiz with answer key based on the information in the video."])

print(response.text)
