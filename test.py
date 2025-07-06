# deployed_client.py
import requests
from PIL import Image
import base64
import io

# Replace with your deployed URL
url = "https://8001...........litng.ai/predict" #change the url by your url

# Optional: Replace with your Bearer token if auth is enabled
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ....."  # Only if needed
}

# Provide your prompt
payload = {
    "prompt": "a photo of an astronaut riding a horse on mars"
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Handle response
if response.status_code == 200:
    result = response.json()
    image_data = base64.b64decode(result["image_base64"])
    image = Image.open(io.BytesIO(image_data))
    image.save("generated_image.png")
    print("✅ Image saved as 'generated_image.png'")
else:
    print(f"❌ Request failed with status code {response.status_code}")
    print(response.text)
