# client.py
import requests
from PIL import Image
import base64
import io

def test_server(prompt):
    url = "http://127.0.0.1:8000/predict"
    payload = {"prompt": prompt}
    response = requests.post(url, json=payload)
    result = response.json()

    image_data = base64.b64decode(result["image_base64"])
    image = Image.open(io.BytesIO(image_data))
    image.save("generated_image.png")
    print("✅ Image saved as 'generated_image.png'.")

if __name__ == "__main__":
    prompt = "a photo of an astronaut riding a horse on mars"
    test_server(prompt)
