# git-homework2
Python CLI gradebook app

## Setup

Clone the repository and make sure you have Python 3 installed. No external dependencies are needed

## Seed sample data
```bash
python scripts/seed.py
```

## CLI Commands
```bash
python main.py add-student --name "John"
python main.py add-course --code CS101 --title "Intro to CS"
python main.py enroll --student-id 1 --course CS101
python main.py add-grade --student-id 1 --course CS101 --grade 95
python main.py list students
python main.py list courses
python main.py list enrollments
python main.py avg --student-id 1 --course CS101
python main.py gpa --student-id 1
```

## Run tests
```bash
python -m unittest tests/test_service.py -v
```

## Description
The data is stored in a JSON file (`data/gradebook.json`) instead of a database.
Student IDs are auto-incremental 
Grades are stored as a list letting a student to have more than one grade
Logs are written in `logs/app.log`