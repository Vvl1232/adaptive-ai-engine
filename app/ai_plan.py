import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")

def generate_study_plan(weak_topics):

    topics = ", ".join(weak_topics)

    prompt = f"""
A student completed an adaptive test.

Weak topics: {topics}

Create a simple 3-step study plan to improve these topics.
"""

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text

        return "Study plan generated but no text returned."

    except Exception as e:
        # Prevent server crash
        return f"AI generation failed: {str(e)}"