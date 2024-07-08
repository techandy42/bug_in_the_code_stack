import os
import google.generativeai as genai

def ask_question_gemini(question):
    os.environ["GOOGLE_API_KEY"] = "sk-1234567890abcdef1234567890abcdef"
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(question)
    answer = response.text.strip()
    return answer
