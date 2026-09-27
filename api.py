from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from fastapi.responses import StreamingResponse
import gridfs
import io
from pydantic import BaseModel

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

uri = os.getenv("MONGODB_URI")

client = MongoClient(
    uri,
    server_api=ServerApi("1")
)

db = client["College"]

fs = gridfs.GridFS(db)

class Student(BaseModel):
    student_id: str
    student_name: str
    roll_number: str
    branch: str
    admission_year: int


@app.get("/")
def home():
    return {"message": "College Academic API is running!"}


@app.get("/student")
def get_student():
    return db.Student.find_one({}, {"_id": 0})


@app.get("/semesters")
def get_semesters():
    return list(db.Semester.find({}, {"_id": 0}))


@app.get("/subjects")
def get_subjects():
    return list(db.Subject.find({}, {"_id": 0}))

@app.get("/subjects/{semester_number}")
def get_subjects_by_semester(semester_number: int):

    links = db.Semester_Subject.find(
        {"semester_number": semester_number},
        {"_id": 0}
    )

    subjects = []

    for link in links:
        subject = db.Subject.find_one(
            {"subject_code": link["subject_code"]},
            {"_id": 0}
        )

        if subject:
            subjects.append(subject)

    return subjects

@app.get("/syllabus")
def get_syllabus():

    file = fs.find_one({
        "filename": "CSE-R24 (1)(1).pdf"
    })

    if file is None:
        return {"error": "Syllabus PDF not found"}

    pdf_data = file.read()

    return StreamingResponse(
        io.BytesIO(pdf_data),
        media_type="application/pdf",
        headers={
            "Content-Disposition": "inline; filename=CSE-R24.pdf"
        }
    )

@app.get("/results")
def get_results():
    return list(db.Result.find({}, {"_id": 0}))

@app.get("/results/{semester_number}")
def get_results_by_semester(semester_number: int):
    return list(
        db.Result.find(
            {"semester_number": semester_number},
            {"_id": 0}
        )
    )

@app.get("/student/{student_id}/results")
def get_student_results(student_id: str):
    return list(
        db.Result.find(
            {"student_id": student_id},
            {"_id": 0}
        )
    )

@app.get("/results/{semester_number}/{subject_code}")
def get_subject_result(semester_number: int, subject_code: str):
    return list(
        db.Result.find(
            {
                "semester_number": semester_number,
                "subject_code": subject_code
            },
            {"_id": 0}
        )
    )

@app.get("/semesters/{semester_number}")
def get_semester(semester_number: int):
    return db.Semester.find_one(
        {"semester_number": semester_number},
        {"_id": 0}
    )

@app.get("/subjects/code/{subject_code}")
def get_subject_by_code(subject_code: str):
    return db.Subject.find_one(
        {"subject_code": subject_code},
        {"_id": 0}
    )

@app.get("/student/{student_id}/semesters")
def get_student_semesters(student_id: str):
    student = db.Student.find_one(
        {"student_id": student_id},
        {"_id": 0}
    )

    if student is None:
        return {"error": "Student not found"}

    semesters = list(
        db.Semester.find({}, {"_id": 0}).sort("semester_number", 1)
    )

    return {
        "student": student,
        "semesters": semesters
    }

@app.get("/student/{student_id}/results/{semester_number}")
def get_student_semester_results(student_id: str, semester_number: int):
    return list(
        db.Result.find(
            {
                "student_id": student_id,
                "semester_number": semester_number
            },
            {"_id": 0}
        )
    )

@app.post("/students")
def create_student(student: Student):
    db.Student.insert_one(student.model_dump())

    return {
        "message": "Student added successfully",
        "student": student.model_dump()
    }

@app.put("/students/{student_id}")
def update_student(student_id: str, student: Student):
    result = db.Student.update_one(
        {"student_id": student_id},
        {"$set": student.model_dump()}
    )

    if result.matched_count == 0:
        return {"error": "Student not found"}

    return {
        "message": "Student updated successfully",
        "student": student.model_dump()
    }

@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    result = db.Student.delete_one(
        {"student_id": student_id}
    )

    if result.deleted_count == 0:
        return {"error": "Student not found"}

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }