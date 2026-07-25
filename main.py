from fastapi import FastAPI
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