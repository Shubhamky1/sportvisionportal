# gemini_utils.py
import google.generativeai as genai
import os

# Load your API key
genai.configure(api_key="AIzaSyAkY_eYS0oR_elnEuVAL17jbrBBJuVfJRU")

def ask_gemini(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text
