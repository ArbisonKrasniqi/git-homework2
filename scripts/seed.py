# scripts/seed.py

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gradebook.service import add_student, add_course, enroll, add_grade

# Add students
s1 = add_student("Alice")
s2 = add_student("Bob")
s3 = add_student("Charlie")

# Add courses
add_course("CS101", "Intro to CS")
add_course("CS102", "Data Structures")

# Enroll students
enroll(s1, "CS101")
enroll(s1, "CS102")
enroll(s2, "CS101")
enroll(s3, "CS102")

# Add grades
add_grade(s1, "CS101", 90)
add_grade(s1, "CS101", 85)
add_grade(s1, "CS102", 78)
add_grade(s2, "CS101", 70)
add_grade(s2, "CS101", 65)
add_grade(s3, "CS102", 88)

print("Seed data created successfully!")