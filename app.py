from flask import Flask, jsonify, request


app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice Johnson", "course": "Computer Science"},
    {"id": 2, "name": "Bob Smith", "course": "Data Science"},
]


@app.get("/")
def home():
    return jsonify({"message": "Student Management API is running"})


@app.get("/students")
def get_students():
    return jsonify(students)


@app.post("/students")
def add_student():
    data = request.get_json(silent=True)

    if not data or not data.get("name") or not data.get("course"):
        return jsonify({"error": "name and course are required"}), 400

    student = {
        "id": max((student["id"] for student in students), default=0) + 1,
        "name": data["name"],
        "course": data["course"],
    }
    students.append(student)
    return jsonify(student), 201


if __name__ == "__main__":
    app.run(debug=True)