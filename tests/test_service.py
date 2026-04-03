from gradebook.service import add_student, add_grade, enroll, add_course, compute_average
from gradebook.storage import save_data
import unittest
from unittest.mock import patch

TEST_PATH = "data/test_gradebook.json"

class TestService(unittest.TestCase):
    def setUp(self):
        self.data = {"students": [], "courses": [], "enrollments": []}

    def test_add_student_success(self):
        with patch("gradebook.service.load_data", return_value=self.data), patch("gradebook.service.save_data"):
            student_id = add_student("Alice")
            self.assertEqual(student_id, 1)

    def test_add_student_empty_fail(self):
        with self.assertRaises(ValueError):
            add_student("")

    def test_add_grade_success(self):
        self.data["students"].append({"id": 1, "name": "Alice"})
        self.data["courses"].append({"code": "CS101", "title": "Intro to CS"})
        self.data["enrollments"].append({"student_id": 1, "course_code": "CS101", "grades": []})
        with patch("gradebook.service.load_data", return_value=self.data), patch("gradebook.service.save_data"):
            add_grade(1, "CS101", 95)
            self.assertEqual(self.data["enrollments"][0]["grades"], [95])

    def test_add_grade_fail(self):
        self.data["students"].append({"id": 1, "name": "Alice"})
        self.data["courses"].append({"code": "CS101", "title": "Intro to CS"})
        self.data["enrollments"].append({"student_id": 1, "course_code": "CS101", "grades": []})
        with patch("gradebook.service.load_data", return_value=self.data), patch("gradebook.service.save_data"):
            with self.assertRaises(ValueError):
                add_grade(1, "CS101", 150)

    def test_compute_average_success(self):
        self.data["enrollments"].append({"student_id": 1, "course_code": "CS101", "grades": [80, 90]})
        with patch("gradebook.service.load_data", return_value=self.data):
            avg = compute_average(1, "CS101")
            self.assertEqual(avg, 85.0)

    def test_compute_average_no_grades(self):
        self.data["enrollments"].append({"student_id": 1, "course_code": "CS101", "grades": []})
        with patch("gradebook.service.load_data", return_value=self.data):
            avg = compute_average(1, "CS101")
            self.assertEqual(avg, 0.0)

if __name__ == "__main__":
    unittest.main()