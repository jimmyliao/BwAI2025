# Reference: https://platform.openai.com/docs/guides/image-generation#generate-images
# pip install openai python-dotenv

from openai import OpenAI
import base64

import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print("Your OpenAI API key is valid")
else:
    print("OPENAI_API_KEY environment variable not found.")


client = OpenAI(api_key=openai_api_key)

prompt = """
A children's book drawing of a veterinarian using a stethoscope to 
listen to the heartbeat of a baby otter.
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("otter.png", "wb") as f:
    f.write(image_bytes)

print("Image saved to otter.png")
