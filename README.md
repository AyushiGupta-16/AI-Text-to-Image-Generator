# AI Based Text-to-Image Generator
A Python project that generates images from text prompts using Stable Diffusion.

This project demonstrates how AI can convert natural language descriptions into realistic images.

---

## ✨  Demo Results

**Prompt:** A futuristic city at sunset  
![City](generated_images/City.png)

**Prompt:** Dragon flying over mountains  
![Dragon](generated_images/Dragon.png)

**Prompt:** Modern glass house in forest  
![House](generated_images/House.png)

**Prompt:** Cat surfing on pizza  
![Cat](generated_images/Cat.png)

**Prompt:** Panda driving a car  
![Panda](generated_images/Panda.png)

---

## ⚙️ How It Works
1. User enters a text prompt via command line
2. Stable Diffusion v1.5 generates the image
3. Image is automatically saved with timestamp
4. Works on CPU and Apple Silicon (MPS)

---

## 📁 Project Structure
app.py → Main script
generated_images/ → Output images
README.md → Documentation

## 💼 Real World Use Cases
• Social media content generation  
• Blog & marketing visuals  
• Concept art creation  
• Creative prototyping  

---

## ▶️ How to Run
pip install diffusers transformers accelerate torch pillow
python app.py

---

## 👩‍💻 Author
Ayushi Gupta – Python & AI Developer
