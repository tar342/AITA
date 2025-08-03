import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_email_thread(thread, user_role, coworker_role, relationship):
    prompt = f"""
You are an impartial HR consultant analyzing workplace communication in a U.S.-based corporate setting.

Evaluate the email thread below and return a JSON with:
- summary
- user_tone
- coworker_tone
- verdict
- confidence
- flagged_phrases
- suggestion

Assume:
- User role: {user_role}
- Coworker role: {coworker_role}
- Relationship: {relationship}

Thread:
{thread}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return json.loads(response.choices[0].message.content)
