from flask import Flask, render_template, request
from analyzer import analyze_email_thread

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        thread_input = request.form.get("thread_input", "")
        sender_role_input = request.form.get("sender_role_input", "Associate")
        recipient_role_input = request.form.get("recipient_role_input", "Manager")
        relationship_input = request.form.get("relationship_input", "peer")
        tone_level = request.form.get("tone_level", "5")
        sender_name_input = request.form.get("sender_name_input", "John Doe")
        if not thread_input.strip():
            error = "Please enter an email thread."
        else:
            try:
                result = analyze_email_thread(
                    thread_input, sender_role_input, recipient_role_input, relationship_input, tone_level, sender_name_input,
                )
            except Exception as e:
                error = str(e)

    return render_template("index.html", result=result, error=error)
