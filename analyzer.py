import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_email_thread(thread_input, sender_name_input, sender_role_input, recipient_role_input, relationship_input, tone_level):
    # Map slider value to tone description
    tone_map = {
        "1": "very soft and diplomatic",
        "2": "soft and gentle",
        "3": "gentle but direct",
        "4": "calm and constructive",
        "5": "neutral and professional",
        "6": "confident and respectful",
        "7": "assertive but respectful",
        "8": "direct and clear",
        "9": "firm and blunt",
        "10": "very direct and unfiltered"
    }

    tone_description = tone_map.get(tone_level, "neutral and professional")

    prompt = f"""
You are an impartial HR consultant analyzing workplace communication in a U.S.-based corporate setting.

Evaluate the email thread below and return a JSON with:
- summary: A brief neutral summary of what happened.
- sender_tone: Label the Sender's tone (e.g., aggressive, passive-aggressive, professional, neutral, frustrated). Use the Sender name to determine who the sender is.
- recipient_tone: Label the Recipient’s tone. 
- verdict: Who is at fault? (Sender, Recipient, or Both. Use the Sender name to dermine who the Sender is)
- confidence: On a scale of 1-10, how confident are you in your verdict?
- flagged_phrases: Any phrases from the sender that may be unprofessional or inflammatory.
- suggestion: Rewrite the emails in a more {tone_description} tone.

Assume:
- Sender role: {sender_role_input}
- Sender name: {sender_name_input}
- Recipient role: {recipient_role_input}
- Relationship of Reciepient to Sender: {relationship_input}

Thread:
{thread_input}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return json.loads(response.choices[0].message.content)
