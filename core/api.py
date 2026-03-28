import requests
import base64

API_URL = "https://router.huggingface.co/models/runwayml/stable-diffusion-v1-5"

def generate(token, prompt, neg_prompt):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "inputs": prompt
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            return None, response.text

        image_bytes = response.content
        img_b64 = base64.b64encode(image_bytes).decode()

        return img_b64, "stable-diffusion-v1-5"

    except Exception as e:
        return None, str(e)