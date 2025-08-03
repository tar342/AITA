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

## Setup

Create and activate a virtual environment:

```sh
conda create -n aita-env python=3.11

conda activate aita-env
```

Install packages:

```sh
# pip install pytest

pip install -r requirements.txt
```

# Usage

export FLASK_APP=app.py          # On Windows: set FLASK_APP=app.py
export FLASK_ENV=development     # On Windows: set 
flask run
