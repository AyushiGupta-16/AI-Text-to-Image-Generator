from diffusers import StableDiffusionPipeline
import torch
import os
from datetime import datetime
import re

# Load the model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cpu")  # Use "cuda" if you have a GPU

# Take input from the user
prompt = input("Enter your image prompt: ")

# Generate an image
image = pipe(prompt).images[0]

# Clean prompt to create a safe filename (e.g., remove special characters)
safe_prompt = re.sub(r'[^a-zA-Z0-9_ ]', '', prompt).replace(' ', '_')[:30]  # Limit length
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{safe_prompt}_{timestamp}.png"

# Create directory if it doesn't exist
os.makedirs("generated_images", exist_ok=True)
output_path = os.path.join("generated_images", filename)

# Save the image
image.save(output_path)
print(f"Image generated and saved as {output_path}")

