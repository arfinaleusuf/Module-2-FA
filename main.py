from fastapi import FastAPI, Path
import json

app = FastAPI()

@app.get("/")
def hello():
    return "Student Management System API"

def load_data():
    with open('student.json','r') as f:
        data = json.load(f)
    return data

@app.get("/about")
def about():
    return "a fully functional API to manage our student records"

@app.get("/view")
def view_students():
    data = load_data()
    return data

@app.get("/view/{student_id}")
def view_students_by_id(student_id: str = Path(...,description="Student id of the student", example="S001")):
    data = load_data()

    if student_id in data:
        return data[student_id]
    else:
        return "Student Not Found"