from google import genai
from google.genai import types
from energy_savings import calculate_total_energy_savings
from credentials import GOOGLE_API_KEY

config = types.GenerateContentConfig(tools=[calculate_total_energy_savings])

client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        'There is s a building which uses about 10000 kWh of energy. The energy price is roughly $0.12 per kWh. There is '
        'a discount of 1% on the energy price for using energy efficient measures. '
        'What would be the total energy savings in this case? Please explain your answer'],
    config=config,
)
print(response.text)
