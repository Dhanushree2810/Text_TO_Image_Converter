import base64
import io
from huggingface_hub import InferenceClient

MODELS = [
    "black-forest-labs/FLUX.1-schnell",
    "stabilityai/stable-diffusion-2-1",
    "runwayml/stable-diffusion-v1-5",
]

def generate(token, prompt, neg_prompt):
    # token= is the correct parameter name
    client = InferenceClient(token=token)
    last_error = "Unknown error"

    for model in MODELS:
        print(f"  Trying: {model}")
        try:
            image = client.text_to_image(
                prompt=prompt,
                model=model,
                negative_prompt=neg_prompt or "blurry, low quality",
                width=512,
                height=512,
            )
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            img_b64 = base64.b64encode(buf.getvalue()).decode()
            print(f"  ✅ Success: {model}")
            return img_b64, model

        except Exception as e:
            last_error = str(e)
            print(f"  ❌ {model}: {last_error[:80]}")
            continue

    return None, f"All models failed. Error: {last_error[:150]}"