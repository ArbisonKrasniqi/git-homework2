from .storage import load_data, save_data
from .models import Course, Enrollment, Student

def add_student(name):
    data = load_data()
    #Mundemi edhe me nje lloj te timestamp
    #Incremental Id is not wrong
    new_id = len(data["students"]) + 1
    student = Student(new_id, name)
    data["students"].append(student.to_dict())
    save_data(data)
    return new_id

def add_course(code, title):
    data = load_data()
    course = Course(code, title)
    data["courses"].append(course.to_dict())
    save_data(data)
    return

def enroll(student_id, course_code):
    data = load_data()
    enrollment = Enrollment(student_id, course_code)
    data["enrollments"].append(enrollment.to_dict())
    save_data(data)
    return

def add_grade(student_id, course_code, grade):
    data = load_data()
    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            #Prej dict, krijo nje objet te Enrollment
            enrollment_obj = Enrollment(e["student_id"], e["course_code"], e["grades"])
            #Perdor metodat e dict per te mos anashkaluar validimet per shtimin e notes
            enrollment_obj.add_grade(grade)
            #Rivendos dict me notat e reja
            e["grades"] = enrollment_obj.grades
            save_data(data)
            return
    raise ValueError(f"Student with student_id: {student_id} enrolled in course: {course_code} does not exist!")
    
def list_students(sort_by="name"):
    data = load_data()
    students = [Student(s["id"], s["name"]) for s in data["students"]]
    return sorted(students, key=lambda s: getattr(s, sort_by))

def list_courses(sort_by="code"):
    data = load_data()
    courses = [Course(c["code"], c["title"]) for c in data["courses"]]
    return sorted(courses, key=lambda c: getattr(c, sort_by))

def list_enrollments():
    data = load_data()
    enrollments = [Enrollment(e["student_id"], e["course_code"], e["grades"]) for e in data["enrollments"]]
    return sorted(enrollments, key=lambda e: e.course_code)

def compute_average(student_id, course_code):
    data = load_data()
    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            if not e["grades"]:
                return 0.0
            return sum(e["grades"]) / len(e["grades"])
    raise ValueError(f"No enrollment found for student {student_id} in the course {course_code}")

def compute_gpa(student_id): #Simple mean of course averages
    data = load_data()
    enrollments = [e for e in data["enrollments"] if e["student_id"] == student_id]

    if not enrollments:
            raise ValueError(f"No enrollments found for student {student_id}.")
    
    averages = [compute_average(student_id, e["course_code"]) for e in enrollments]
    return sum(averages) / len(averages)
