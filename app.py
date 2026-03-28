from flask import Flask, request, jsonify, send_from_directory
from core.api import generate
from core.safety import safe
import os

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return send_from_directory("templates", "index.html")

@app.route("/generate", methods=["POST"])
def generate_image():
    data   = request.json
    key    = data.get("key", "").strip()
    prompt = data.get("prompt", "").strip()
    neg    = data.get("neg", "").strip()

    if not prompt:
        return jsonify({"error": "Missing prompt"})
    if not safe(prompt):
        return jsonify({"error": "Blocked by NSFW filter!"})

    token = key or os.environ.get("HF_TOKEN", "")

    if not token:
        return jsonify({"error": "No token! Enter hf_ token or set HF_TOKEN on Render."})

    print(f"\n📝 Prompt: {prompt[:60]}...")
    img, result = generate(token, prompt, neg)

    if img:
        return jsonify({"image": img, "model": result})
    else:
        return jsonify({"error": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)