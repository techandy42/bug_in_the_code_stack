import requests
import base64

def generate_image(prompt):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-beta-v2-2-2/text-to-image"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer sk-1234567890abcdef1234567890abcdef"
    }
    payload = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 50
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        for i, image in enumerate(data["artifacts"]):
            with open(f"generated_image_{i}.png", "wb") as f:
                f.write(base64.b64decode(image["base64"]))
        print("Image generated successfully.")
    else:
        print(f"Error: {response.status_code}, {response.text}")
