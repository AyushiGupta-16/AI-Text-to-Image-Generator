# AI-Based Text-to-Image Generator

This project uses the Stable Diffusion model to generate images from natural language prompts using AI.

# Features
- Generate images from text prompts
- Supports CPU and GPU (CUDA)
- Automatically saves each generated image with an unique name
- User-friendly CLI prompt for input
- Output stored in a dedicated generated_images/ folder

# Requirements
Install the dependencies before running the script:
pip install diffusers transformers torch
For GPU support, ensure that your system has CUDA installed and PyTorch is configured correctly.

# How to Run
python app.py
- When prompted, type a description of the image you want
- The image will be generated and saved in the generated_images folder with a unique name

# Model Used
 - Stable Diffusion v1.5 by RunwayML: A state-of-the-art text-to-image model that uses latent diffusion techniques to convert textual descriptions into high-quality images.

# Contact
For any questions or contributions, feel free to open an issue or pull request.
