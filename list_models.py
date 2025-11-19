import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# just checking what all models are available, nothing fancy
print("AVAILABLE MODELS:")
models = genai.list_models()

# printing model names one by one (just to see what's there)
for m in models:
    print(" -", m.name)
