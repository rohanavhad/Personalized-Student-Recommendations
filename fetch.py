import pandas as pd
import requests

# API Endpoint (Replace with actual API)
API_URL = "https://www.jsonkeeper.com/b/LLQT"

# Fetch data
response = requests.get(API_URL)
data = response.json()

# Convert JSON to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("api_data.csv", index=False)

print("CSV file saved successfully!")
