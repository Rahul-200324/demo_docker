from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Student API!"

@app.route("/student")
def student():
    student_data = {
        "name": "Rahul",
        "course": "B.E Electrical and Electronics",
        "skills": ["Python", "Java", "SQL", "Docker"],
        "status": "Learning DevOps"
    }

    return jsonify(student_data)

@app.route("/health")
def health():
    return jsonify({
        "status": "Karnataka"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)