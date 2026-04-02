class Student:
    #student_id gjenerohet ne service kismet
    def __init__(self, id, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not len(name.strip()) > 3:
            raise ValueError("Name should be longer than 3 characters")
        self.student_id = id
        self.name = name.strip()
        pass

    def __str__(self):
        return f"Student(id={self.id}, name={self.name})"

class Course:
    def __init__(self, code, title):
        if not isinstance(code, str) or not code.strip():
            raise ValueError("Code must be non empty")
        if not len(code.strip()) > 2:
            raise ValueError("Code should be longer than 2 characters")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must not be empty")
        if not len(title.strip()) > 3:
            raise ValueError("Code should be longer than 3 characters")
        self.code = code
        self.title = title

    def __str__(self):
        return f"Course(code={self.code}, title={self.title})"

class Enrollment:
    def __init__(self, student_id, course_code, grades=None):
        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number")
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be a number between 0 and 100")
        self.grades.append(grade)

    def __str__(self):
        return(f"Enrollment(student_id={self.student_id}, course_code={self.course_code}, grades={self.grades})")
