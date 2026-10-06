from flask import Flask, render_template, request, jsonify

app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../frontend",
    static_url_path="/static"
)

def get_response(message):
    message = message.lower()

    if "exam" in message:
        return "Exam details will be updated soon."

    elif "fee" in message:
        return "Please contact the college office for fee details."

    elif "attendance" in message:
        return "You can check your attendance through the student portal."

    elif "timetable" in message:
        return "Please check the latest department timetable."

    elif "hello" in message or "hi" in message:
        return "Hello! 👋 How can I help you?"

    else:
        return "Sorry, I don't have information about that yet."

@app.routea("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    response = get_response(message)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)


