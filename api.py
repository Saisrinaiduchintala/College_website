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

class SubjectCreate(BaseModel):
    subject_code: str
    subject_name: str
    subject_type: str
    credits: float

class SemesterCreate(BaseModel):
    semester_number: int
    semester_name: str

class SemesterSubjectCreate(BaseModel):
    semester_number: int
    subject_code: str

class ExamCreate(BaseModel):
    semester_number: int
    subject_code: str
    exam_type: str
    exam_name: str
    exam_date: str
    max_marks: int

class ResultCreate(BaseModel):
    student_id: str
    semester_number: int
    subject_code: str
    exam_name: str
    marks_obtained: float
    grade: str
    remarks: str

class SyllabusCreate(BaseModel):
    semester: int
    subject_code: str
    subject_name: str
    modules: list

class SubjectUpdate(BaseModel):
    subject_name: str
    subject_type: str
    credits: float

class SemesterUpdate(BaseModel):
    semester_name: str

class SemesterSubjectUpdate(BaseModel):
    subject_code: str

class ExamUpdate(BaseModel):
    exam_type: str
    exam_name: str
    exam_date: str
    max_marks: int

class ResultUpdate(BaseModel):
    marks_obtained: float
    grade: str
    remarks: str

class SyllabusUpdate(BaseModel):
    subject_name: str
    modules: list

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

@app.get("/syllabus")
def get_syllabus():
    syllabus = list(db["syllabus"].find({}, {"_id": 0}))
    return syllabus

@app.get("/syllabus/{semester}")
def get_semester_syllabus(semester: int):
    syllabus = list(
        db["syllabus"].find(
            {"semester": semester},
            {"_id": 0}
        )
    )

    if not syllabus:
        return {"message": "Semester not found"}

    return syllabus

@app.get("/syllabus/{semester}/{subject_code}")
def get_subject_syllabus(semester: int, subject_code: str):

    syllabus = db["syllabus"].find_one(
        {
            "semester": semester,
            "subject_code": subject_code
        },
        {"_id": 0}
    )

    if not syllabus:
        return {"message": "Subject not found"}

    return syllabus

@app.post("/subjects")
def create_subject(subject: SubjectCreate):
    existing_subject = db.Subject.find_one(
        {"subject_code": subject.subject_code}
    )

    if existing_subject:
        return {"message": "Subject already exists"}

    result = db.Subject.insert_one(subject.model_dump())

    return {
        "message": "Subject created successfully",
        "id": str(result.inserted_id)
    }

@app.post("/semesters")
def create_semester(semester: SemesterCreate):
    existing_semester = db.Semesters.find_one(
        {"semester_number": semester.semester_number}
    )

    if existing_semester:
        return {"message": "Semester already exists"}

    result = db.Semesters.insert_one(semester.model_dump())

    return {
        "message": "Semester created successfully",
        "id": str(result.inserted_id)
    }

@app.post("/semester-subjects")
def create_semester_subject(link: SemesterSubjectCreate):

    existing_link = db.Semester_Subjects.find_one(
        {
            "semester_number": link.semester_number,
            "subject_code": link.subject_code
        }
    )

    if existing_link:
        return {"message": "Semester-subject link already exists"}

    result = db.Semester_Subjects.insert_one(link.model_dump())

    return {
        "message": "Semester-subject link created successfully",
        "id": str(result.inserted_id)
    }

@app.post("/exams")
def create_exam(exam: ExamCreate):

    existing_exam = db.Exam.find_one(
        {
            "semester_number": exam.semester_number,
            "subject_code": exam.subject_code,
            "exam_name": exam.exam_name
        }
    )

    if existing_exam:
        return {"message": "Exam already exists"}

    result = db.Exam.insert_one(exam.model_dump())

    return {
        "message": "Exam created successfully",
        "id": str(result.inserted_id)
    }

@app.post("/results")
def create_result(result: ResultCreate):

    existing_result = db.Result.find_one(
        {
            "student_id": result.student_id,
            "semester_number": result.semester_number,
            "subject_code": result.subject_code,
            "exam_name": result.exam_name
        }
    )

    if existing_result:
        return {"message": "Result already exists"}

    result_id = db.Result.insert_one(result.model_dump())

    return {
        "message": "Result created successfully",
        "id": str(result_id.inserted_id)
    }

@app.post("/syllabus")
def create_syllabus(syllabus: SyllabusCreate):

    existing_syllabus = db.syllabus.find_one(
        {
            "semester": syllabus.semester,
            "subject_code": syllabus.subject_code
        }
    )

    if existing_syllabus:
        return {"message": "Syllabus already exists"}

    result = db.syllabus.insert_one(syllabus.model_dump())

    return {
        "message": "Syllabus created successfully",
        "id": str(result.inserted_id)
    }

@app.put("/subjects/{subject_code}")
def update_subject(subject_code: str, subject: SubjectUpdate):

    existing_subject = db.Subject.find_one(
        {"subject_code": subject_code}
    )

    if not existing_subject:
        return {"message": "Subject not found"}

    db.Subject.update_one(
        {"subject_code": subject_code},
        {
            "$set": {
                "subject_name": subject.subject_name,
                "subject_type": subject.subject_type,
                "credits": subject.credits
            }
        }
    )

    return {
        "message": "Subject updated successfully"
    }

@app.put("/semesters/{semester_number}")
def update_semester(
    semester_number: int,
    semester: SemesterUpdate
):
    existing_semester = db.Semesters.find_one(
        {"semester_number": semester_number}
    )

    if not existing_semester:
        return {"message": "Semester not found"}

    db.Semesters.update_one(
        {"semester_number": semester_number},
        {
            "$set": {
                "semester_name": semester.semester_name
            }
        }
    )

    return {
        "message": "Semester updated successfully"
    }

@app.put("/semester-subjects/{semester_number}/{subject_code}")
def update_semester_subject(
    semester_number: int,
    subject_code: str,
    link: SemesterSubjectUpdate
):
    existing_link = db.Semester_Subjects.find_one(
        {
            "semester_number": semester_number,
            "subject_code": subject_code
        }
    )

    if not existing_link:
        return {"message": "Semester-subject link not found"}

    db.Semester_Subjects.update_one(
        {
            "semester_number": semester_number,
            "subject_code": subject_code
        },
        {
            "$set": {
                "subject_code": link.subject_code
            }
        }
    )

    return {
        "message": "Semester-subject link updated successfully"
    }

@app.put("/exams/{exam_name}")
def update_exam(
    exam_name: str,
    exam: ExamUpdate
):
    existing_exam = db.Exam.find_one(
        {"exam_name": exam_name}
    )

    if not existing_exam:
        return {"message": "Exam not found"}

    db.Exam.update_one(
        {"exam_name": exam_name},
        {
            "$set": {
                "exam_type": exam.exam_type,
                "exam_name": exam.exam_name,
                "exam_date": exam.exam_date,
                "max_marks": exam.max_marks
            }
        }
    )

    return {
        "message": "Exam updated successfully"
    }

@app.put("/results/{student_id}/{semester_number}/{subject_code}/{exam_name}")
def update_result(
    student_id: str,
    semester_number: int,
    subject_code: str,
    exam_name: str,
    result: ResultUpdate
):
    existing_result = db.Result.find_one(
        {
            "student_id": student_id,
            "semester_number": semester_number,
            "subject_code": subject_code,
            "exam_name": exam_name
        }
    )

    if not existing_result:
        return {"message": "Result not found"}

    db.Result.update_one(
        {
            "student_id": student_id,
            "semester_number": semester_number,
            "subject_code": subject_code,
            "exam_name": exam_name
        },
        {
            "$set": {
                "marks_obtained": result.marks_obtained,
                "grade": result.grade,
                "remarks": result.remarks
            }
        }
    )

    return {
        "message": "Result updated successfully"
    }

@app.put("/syllabus/{semester}/{subject_code}")
def update_syllabus(
    semester: int,
    subject_code: str,
    syllabus: SyllabusUpdate
):
    existing_syllabus = db.syllabus.find_one(
        {
            "semester": semester,
            "subject_code": subject_code
        }
    )

    if not existing_syllabus:
        return {"message": "Syllabus not found"}

    db.syllabus.update_one(
        {
            "semester": semester,
            "subject_code": subject_code
        },
        {
            "$set": {
                "subject_name": syllabus.subject_name,
                "modules": syllabus.modules
            }
        }
    )

    return {
        "message": "Syllabus updated successfully"
    }

@app.delete("/subjects/{subject_code}")
def delete_subject(subject_code: str):

    result = db.Subject.delete_one(
        {"subject_code": subject_code}
    )

    if result.deleted_count == 0:
        return {"message": "Subject not found"}

    return {
        "message": "Subject deleted successfully"
    }

@app.delete("/semesters/{semester_number}")
def delete_semester(semester_number: int):

    result = db.Semesters.delete_one(
        {"semester_number": semester_number}
    )

    if result.deleted_count == 0:
        return {"message": "Semester not found"}

    return {
        "message": "Semester deleted successfully"
    }

@app.delete("/semester-subjects/{semester_number}/{subject_code}")
def delete_semester_subject(
    semester_number: int,
    subject_code: str
):

    result = db.Semester_Subjects.delete_one(
        {
            "semester_number": semester_number,
            "subject_code": subject_code
        }
    )

    if result.deleted_count == 0:
        return {"message": "Semester-subject link not found"}

    return {
        "message": "Semester-subject link deleted successfully"
    }

@app.delete("/exams/{exam_name}")
def delete_exam(exam_name: str):

    result = db.Exam.delete_one(
        {"exam_name": exam_name}
    )

    if result.deleted_count == 0:
        return {"message": "Exam not found"}

    return {
        "message": "Exam deleted successfully"
    }

@app.delete(
    "/results/{student_id}/{semester_number}/{subject_code}/{exam_name}"
)
def delete_result(
    student_id: str,
    semester_number: int,
    subject_code: str,
    exam_name: str
):

    result = db.Result.delete_one(
        {
            "student_id": student_id,
            "semester_number": semester_number,
            "subject_code": subject_code,
            "exam_name": exam_name
        }
    )

    if result.deleted_count == 0:
        return {"message": "Result not found"}

    return {
        "message": "Result deleted successfully"
    }

@app.delete("/syllabus/{semester}/{subject_code}")
def delete_syllabus(
    semester: int,
    subject_code: str
):

    result = db.syllabus.delete_one(
        {
            "semester": semester,
            "subject_code": subject_code
        }
    )

    if result.deleted_count == 0:
        return {"message": "Syllabus not found"}

    return {
        "message": "Syllabus deleted successfully"
    }
