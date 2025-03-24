 # Add more as needed
import google.generativeai as genai
import os

# Fetch Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Basic inappropriate content filter
INAPPROPRIATE_WORDS = ["shit", "death", "crap"]  # Add more as needed

def filter_content(text):
    """Check for inappropriate words in user input."""
    for word in INAPPROPRIATE_WORDS:
        if word in text.lower():
            return True
    return False

def get_llm_response(query):
    """Fetch response from Gemini API."""
    if filter_content(query):
        return "Your input contains inappropriate content. Please rephrase."

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-pro")  
        response = model.generate_content(query)
        return response.text if response.text else "No response received."
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    response = get_llm_response(user_query)
    print("AI Response:", response)
