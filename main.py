from argparse import ArgumentParser
import logging
import os

from gradebook.service import (
    add_student, add_course, enroll, add_grade, list_students, list_courses, list_enrollments, compute_average, compute_gpa
)
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

def string_to_number(value):
    try:
        grade = float(value)
    except ValueError:
        raise ValueError(f"{value} is not a real number")
    return grade

def main():
    # Argument Parser lexon te gjithe python programin
    parser = ArgumentParser(description="Gradebook Command Line Interface")
    #Subparsers definon komandat per main parser, shembull: (add-student, add-course, gpa)
    subparsers = parser.add_subparsers(dest="command")

    p_add_student = subparsers.add_parser("add-student")
    p_add_student.add_argument("--name", required=True)

    # add-course
    p_add_course = subparsers.add_parser("add-course")
    p_add_course.add_argument("--code", required=True)
    p_add_course.add_argument("--title", required=True)

    # enroll
    p_enroll = subparsers.add_parser("enroll")
    p_enroll.add_argument("--student-id", required=True, type=int)
    p_enroll.add_argument("--course", required=True)

    # add-grade
    p_add_grade = subparsers.add_parser("add-grade")
    p_add_grade.add_argument("--student-id", required=True, type=int)
    p_add_grade.add_argument("--course", required=True)
    p_add_grade.add_argument("--grade", required=True)

    # list
    p_list = subparsers.add_parser("list")
    p_list.add_argument("type", choices=["students", "courses", "enrollments"])
    p_list.add_argument("--sort", choices=["name", "code", "student_id"], default=None)
    
    # avg
    p_avg = subparsers.add_parser("avg")
    p_avg.add_argument("--student-id", required=True, type=int)
    p_avg.add_argument("--course", required=True)

    # gpa
    p_gpa = subparsers.add_parser("gpa")
    p_gpa.add_argument("--student-id", required=True, type=int)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            student_id = add_student(args.name)
            print(f"Student \"{args.name}\" added with id {student_id}.")

        elif args.command == "add-course":
            add_course(args.code, args.title)
            print(f"Course \"{args.title}\" ({args.code}) added.")

        elif args.command == "enroll":
            enroll(args.student_id, args.course)
            print(f"Student {args.student_id} enrolled in {args.course}.")

        elif args.command == "add-grade":
            grade = string_to_number(args.grade)
            add_grade(args.student_id, args.course, grade)
            print(f"Grade {grade} added for student {args.student_id} in {args.course}.")

        elif args.command == "list":
            if args.type == "students":
                sort_by = args.sort if args.sort else "name"
                for s in list_students(sort_by):
                    print(s)
            elif args.type == "courses":
                sort_by = args.sort if args.sort else "code"
                for c in list_courses(sort_by):
                    print(c)
            elif args.type == "enrollments":
                for e in list_enrollments():
                    print(e)

        elif args.command == "avg":
            avg = compute_average(args.student_id, args.course)
            print(f"Average for student {args.student_id} in {args.course}: {avg}")

        elif args.command =="gpa":
            gpa = compute_gpa(args.student_id)
            print(f"GPA for student {args.student_id}: {gpa}")

        else:
            parser.print_help()
    except ValueError as e:
        logging.error(str(e))
        print(f"Error: {e}")

if __name__ == "__main__":
    main()