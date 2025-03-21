from google import genai
from google.genai import types
from energy_savings import calculate_total_energy_savings
from credentials import GOOGLE_API_KEY
import json

config = types.GenerateContentConfig(tools=[calculate_total_energy_savings])

client = genai.Client(api_key=GOOGLE_API_KEY)

chat = client.chats.create(model="gemini-2.0-flash", config=config)

response = chat.send_message(
    'There is s a building which uses about 10000 kWh of energy. The energy price is roughly $0.12 per kWh. '
    'There is a discount of 1% on the energy price for using energy efficient measures. '
    'What would be the total energy savings in this case? Please explain your answer'
)
print(response.text)

for content in chat.get_history():
    part = content.parts[0].dict()
    print(f"From: {content.role} -> {json.dumps(part, indent=2)}")
