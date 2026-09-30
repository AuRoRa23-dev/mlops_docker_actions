import unittest

from app import app, students


class StudentApiTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        students.clear()
        students.extend(
            [
                {"id": 1, "name": "Alice Johnson", "course": "Computer Science"},
                {"id": 2, "name": "Bob Smith", "course": "Data Science"},
            ]
        )

    def test_get_students(self):
        response = self.client.get("/students")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 2)

    def test_add_student(self):
        response = self.client.post(
            "/students",
            json={"name": "Chris Lee", "course": "Cybersecurity"},
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {
            "id": 3,
            "name": "Chris Lee",
            "course": "Cybersecurity",
        })

    def test_add_student_requires_name_and_course(self):
        response = self.client.post("/students", json={"name": "Chris Lee"})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "name and course are required")


if __name__ == "__main__":
    unittest.main()