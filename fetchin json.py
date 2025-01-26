import requests
import json

# Step 1: Define the API URL (Replace with your actual API link)
api_url = "https://api.jsonserve.com/XgAgFJ"  # Replace with your actual API link

# Step 2: Fetch JSON data from API
response = requests.get(api_url)

# Step 3: Convert response to JSON format
if response.status_code == 200:
    data = response.json()  # Convert API response to dictionary
else:
    print("❌ Error fetching data:", response.status_code)
    exit()

# Step 4: Save JSON data to a file
json_filename = " APIEndpoint.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"✅ JSON file created successfully: {json_filename}")
