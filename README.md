# Am I the Asshole? (Corporate Edition)

This is a Flask-based web app that uses OpenAI's GPT API to analyze workplace email threads and determine who's in the wrong — the user, their coworker, or both — based on tone, power dynamics, and professional norms.

---

## Features

- Paste email threads into the app.
- Define your role, the coworker’s role, and relationship.
- GPT-4 analyzes the thread and returns:
  - Summary of situation
  - Tone assessment
  - Verdict (User, Coworker, Both)
  - Confidence scores
  - Problematic phrases
  - Suggested rewrite

---

## Setup Instructions (Terminal)

### 1. Clone or Download the Repo

If you downloaded the ZIP, unzip it and navigate to the project folder:

```bash
unzip aita-corp.zip
cd aita-corp
