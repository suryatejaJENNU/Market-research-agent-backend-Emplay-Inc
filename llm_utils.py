import os
from dotenv import load_dotenv
import google.generativeai as genai

# just loading env things, need keys from here only
load_dotenv()

# printing just to check whether keys coming or not
print("DEBUG (llm_utils): GOOGLE_API_KEY =", os.getenv("GOOGLE_API_KEY"))
print("DEBUG (llm_utils): GEMINI_API_KEY =", os.getenv("GEMINI_API_KEY"))

# using whatever key available, first google then gemini
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

# if no key then nothing will work so throwing error
if not api_key:
    raise Exception("Gemini API key missing!")



genai.configure(api_key=api_key)

# using this flash model, seems faster so using this only
model = genai.GenerativeModel("models/gemini-2.5-flash")


# function to get keywords from input, model will generate it
def expand_keywords(text, n=5):
    # telling model what to do basically
    prompt = f"Generate {n} relevant keywords for: {text}. Only return the keywords."
    result = model.generate_content(prompt)
    kw = result.text.strip().split("\n")
    # cleaning little, returning top n
    return [k.strip() for k in kw if k.strip()][:n]


# for checking sentiments of headlines. simple prompt only.
def analyze_sentiment(text_list):
    if not text_list:
        return "No sentiment data available."

    prompt = f"Analyze sentiment for:\n{text_list}\nProvide short positive/negative/neutral summary."
    result = model.generate_content(prompt)
    return result.text.strip()


# this one for full detailed report, model will write everything
def generate_summary(data):
    prompt = f"Generate a detailed market research summary for this data:\n{data}"
    result = model.generate_content(prompt)
    return result.text.strip()
