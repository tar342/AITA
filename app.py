from flask import Flask, render_template, request
from analyzer import analyze_email_thread

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        thread = request.form.get("thread", "")
        user_role = request.form.get("user_role", "Associate")
        coworker_role = request.form.get("coworker_role", "Manager")
        relationship = request.form.get("relationship", "peer")
        tone_level = request.form.get("tone_level", "5")  # NEW

        if not thread.strip():
            error = "Please enter an email thread."
        else:
            try:
                result = analyze_email_thread(
                    thread, user_role, coworker_role, relationship, tone_level
                )
            except Exception as e:
                error = str(e)

    return render_template("index.html", result=result, error=error)
