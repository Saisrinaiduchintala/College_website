from pymongo import MongoClient
from pymongo.server_api import ServerApi


import os
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGODB_URI")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["College"]  


subjects = [

    # Semester I
    {
        "subject_code": "M110A",
        "subject_name": "Matrices and Calculus",
        "subject_type": "Theory",
        "credits": 4
    },
    {
        "subject_code": "M110D",
        "subject_name": "Engineering Chemistry",
        "subject_type": "Theory",
        "credits": 4
    },
    {
        "subject_code": "M110C",
        "subject_name": "English for Skill Enhancement",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M115A",
        "subject_name": "Elements of Computer Science and Engineering",
        "subject_type": "Theory",
        "credits": 1
    },
    {
        "subject_code": "M115B",
        "subject_name": "Programming for Problem Solving",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M1103",
        "subject_name": "English Language and Communication Skills Lab",
        "subject_type": "Lab",
        "credits": 1
    },
    {
        "subject_code": "M1102",
        "subject_name": "Chemistry Laboratory",
        "subject_type": "Lab",
        "credits": 1
    },
    {
        "subject_code": "M1151",
        "subject_name": "Programming for Problem Solving Lab",
        "subject_type": "Lab",
        "credits": 1
    },
    {
        "subject_code": "M1132",
        "subject_name": "Computer Aided Engineering Graphics",
        "subject_type": "Theory",
        "credits": 2.5
    },
    {
        "subject_code": "M11AC2",
        "subject_name": "Human Values and Professional Ethics",
        "subject_type": "Theory",
        "credits": 0
    },

    # Semester II
    {
        "subject_code": "M120A",
        "subject_name": "Differential Equations and Vector Calculus",
        "subject_type": "Theory",
        "credits": 4
    },
    {
        "subject_code": "M120B",
        "subject_name": "Applied Physics",
        "subject_type": "Theory",
        "credits": 4
    },
    {
        "subject_code": "M122A",
        "subject_name": "Basic Electrical Engineering",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M125A",
        "subject_name": "Data Structure",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M1252",
        "subject_name": "Data Structure Lab",
        "subject_type": "Lab",
        "credits": 1
    },
    {
        "subject_code": "M1201",
        "subject_name": "Physics Laboratory",
        "subject_type": "Lab",
        "credits": 1
    },
    {
        "subject_code": "M1221",
        "subject_name": "Basic Electrical Engineering Lab",
        "subject_type": "Lab",
        "credits": 1
    },
    {
        "subject_code": "M1233",
        "subject_name": "Engineering & IT Workshop",
        "subject_type": "Lab",
        "credits": 2.5
    },
    {
        "subject_code": "M12AC1",
        "subject_name": "Linguaskill for Professionals-B1",
        "subject_type": "Theory",
        "credits": 0
    },

    # Semester III
    {
        "subject_code": "M210A",
        "subject_name": "Probability and Statistics",
        "subject_type": "Theory",
        "credits": 4
    },
    {
        "subject_code": "M214E",
        "subject_name": "Digital Logic Design",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M215C",
        "subject_name": "Design and Analysis of Algorithms",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M215B",
        "subject_name": "Python Programming",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M216D",
        "subject_name": "Database Management Systems",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M2151",
        "subject_name": "Python Programming Lab",
        "subject_type": "Lab",
        "credits": 1.5
    },
    {
        "subject_code": "M2162",
        "subject_name": "Database Management Systems Lab",
        "subject_type": "Lab",
        "credits": 1.5
    },
    {
        "subject_code": "M21MC1",
        "subject_name": "Environmental Science",
        "subject_type": "Theory",
        "credits": 0
    },

    # Semester IV
    {
        "subject_code": "M225B",
        "subject_name": "Computer Organization and Architecture",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M225A",
        "subject_name": "Mathematical Foundations of Computer Science",
        "subject_type": "Theory",
        "credits": 4
    },
    {
        "subject_code": "M226A",
        "subject_name": "Object Oriented Programming through Java",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M225F",
        "subject_name": "Operating Systems",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M225E",
        "subject_name": "Computer Networks",
        "subject_type": "Theory",
        "credits": 3
    },
    {
        "subject_code": "M2261",
        "subject_name": "Object Oriented Programming through Java Lab",
        "subject_type": "Lab",
        "credits": 1.5
    },
    {
        "subject_code": "M2252",
        "subject_name": "Operating Systems Lab",
        "subject_type": "Lab",
        "credits": 1.5
    },
    {
        "subject_code": "M2253",
        "subject_name": "Node JS/ React JS/ Django",
        "subject_type": "Lab",
        "credits": 1
    },
    {
        "subject_code": "M22MC2",
        "subject_name": "Gender Sensitization",
        "subject_type": "Theory",
        "credits": 0
    },
    {
        "subject_code": "M22AC1",
        "subject_name": "Linguaskill for Professionals –B2",
        "subject_type": "Theory",
        "credits": 0
    }
]

print(subjects)

db.Subject.delete_many({})
db.Subject.insert_many(subjects)

print("All subjects inserted successfully!")

semesters = [
    {
        "semester_number": 1,
        "academic_year": "2024-2025",
        "sgpa": 8.24,
        "cgpa": None,
        "total_credits": 20.5,
        "credits_secured": 20.5
    },
    {
        "semester_number": 2,
        "academic_year": "2025-2026",
        "sgpa": 8.08,
        "cgpa": None,
        "total_credits": 19.5,
        "credits_secured": 19.5
    },
    {
        "semester_number": 3,
        "academic_year": "2025-2026",
        "sgpa": 7.60,
        "cgpa": None,
        "total_credits": 19.0,
        "credits_secured": 19.0
    },
    {
        "semester_number": 4,
        "academic_year": "2025-2026",
        "sgpa": 7.95,
        "cgpa": 7.97,
        "total_credits": 20.0,
        "credits_secured": 20.0
    }
]

db.Semester.delete_many({})
db.Semester.insert_many(semesters)

print("Semesters inserted successfully!")

semester_subjects = [
    # Semester I
    {"semester_number": 1, "subject_code": "M110A"},
    {"semester_number": 1, "subject_code": "M110D"},
    {"semester_number": 1, "subject_code": "M110C"},
    {"semester_number": 1, "subject_code": "M115A"},
    {"semester_number": 1, "subject_code": "M115B"},
    {"semester_number": 1, "subject_code": "M1103"},
    {"semester_number": 1, "subject_code": "M1102"},
    {"semester_number": 1, "subject_code": "M1151"},
    {"semester_number": 1, "subject_code": "M1132"},
    {"semester_number": 1, "subject_code": "M11AC2"},

    # Semester II
    {"semester_number": 2, "subject_code": "M120A"},
    {"semester_number": 2, "subject_code": "M120B"},
    {"semester_number": 2, "subject_code": "M122A"},
    {"semester_number": 2, "subject_code": "M125A"},
    {"semester_number": 2, "subject_code": "M1252"},
    {"semester_number": 2, "subject_code": "M1201"},
    {"semester_number": 2, "subject_code": "M1221"},
    {"semester_number": 2, "subject_code": "M1233"},
    {"semester_number": 2, "subject_code": "M12AC1"},

    # Semester III
    {"semester_number": 3, "subject_code": "M210A"},
    {"semester_number": 3, "subject_code": "M214E"},
    {"semester_number": 3, "subject_code": "M215C"},
    {"semester_number": 3, "subject_code": "M215B"},
    {"semester_number": 3, "subject_code": "M216D"},
    {"semester_number": 3, "subject_code": "M2151"},
    {"semester_number": 3, "subject_code": "M2162"},
    {"semester_number": 3, "subject_code": "M21MC1"},

    # Semester IV
    {"semester_number": 4, "subject_code": "M225B"},
    {"semester_number": 4, "subject_code": "M225A"},
    {"semester_number": 4, "subject_code": "M226A"},
    {"semester_number": 4, "subject_code": "M225F"},
    {"semester_number": 4, "subject_code": "M225E"},
    {"semester_number": 4, "subject_code": "M2261"},
    {"semester_number": 4, "subject_code": "M2252"},
    {"semester_number": 4, "subject_code": "M2253"},
    {"semester_number": 4, "subject_code": "M22MC2"},
    {"semester_number": 4, "subject_code": "M22AC1"}
]

db.Semester_Subject.delete_many({})
db.Semester_Subject.insert_many(semester_subjects)

print("Semester-Subject links inserted successfully!")

student = {
    "student_id": "24671A05R2",
    "student_name": "Chinthala Rama Naga Sai Sriakshmi",
    "roll_number": "24671A05R2",
    "branch": "CSE",
    "admission_year": 2024
}

db.Student.delete_many({})
db.Student.insert_one(student)

print("Student inserted successfully!")

exams = [
    # Semester I
    {"semester_number": 1, "subject_code": "M110A", "exam_type": "Theory", "exam_name": "Sem1_M110A_Exam", "exam_date": "2025-01", "max_marks": 100},
    {"semester_number": 1, "subject_code": "M110D", "exam_type": "Theory", "exam_name": "Sem1_M110D_Exam", "exam_date": "2025-01", "max_marks": 100},
    {"semester_number": 1, "subject_code": "M110C", "exam_type": "Theory", "exam_name": "Sem1_M110C_Exam", "exam_date": "2025-01", "max_marks": 100},
    {"semester_number": 1, "subject_code": "M115A", "exam_type": "Theory", "exam_name": "Sem1_M115A_Exam", "exam_date": "2025-01", "max_marks": 100},
    {"semester_number": 1, "subject_code": "M115B", "exam_type": "Theory", "exam_name": "Sem1_M115B_Exam", "exam_date": "2025-01", "max_marks": 100},
    {"semester_number": 1, "subject_code": "M1102", "exam_type": "Lab", "exam_name": "Sem1_M1102_Exam", "exam_date": "2025-01", "max_marks": 100},
    {"semester_number": 1, "subject_code": "M1103", "exam_type": "Lab", "exam_name": "Sem1_M1103_Exam", "exam_date": "2025-01", "max_marks": 100},
    {"semester_number": 1, "subject_code": "M1151", "exam_type": "Lab", "exam_name": "Sem1_M1151_Exam", "exam_date": "2025-01", "max_marks": 100},
    {"semester_number": 1, "subject_code": "M1132", "exam_type": "Theory", "exam_name": "Sem1_M1132_Exam", "exam_date": "2025-01", "max_marks": 100},

    # Semester II
    {"semester_number": 2, "subject_code": "M120A", "exam_type": "Theory", "exam_name": "Sem2_M120A_Exam", "exam_date": "2026-01", "max_marks": 100},
    {"semester_number": 2, "subject_code": "M120B", "exam_type": "Theory", "exam_name": "Sem2_M120B_Exam", "exam_date": "2026-01", "max_marks": 100},
    {"semester_number": 2, "subject_code": "M122A", "exam_type": "Theory", "exam_name": "Sem2_M122A_Exam", "exam_date": "2026-01", "max_marks": 100},
    {"semester_number": 2, "subject_code": "M125A", "exam_type": "Theory", "exam_name": "Sem2_M125A_Exam", "exam_date": "2026-01", "max_marks": 100},
    {"semester_number": 2, "subject_code": "M1251", "exam_type": "Lab", "exam_name": "Sem2_M1251_Exam", "exam_date": "2026-01", "max_marks": 100},
    {"semester_number": 2, "subject_code": "M1201", "exam_type": "Lab", "exam_name": "Sem2_M1201_Exam", "exam_date": "2026-01", "max_marks": 100},
    {"semester_number": 2, "subject_code": "M1221", "exam_type": "Lab", "exam_name": "Sem2_M1221_Exam", "exam_date": "2026-01", "max_marks": 100},
    {"semester_number": 2, "subject_code": "M1233", "exam_type": "Lab", "exam_name": "Sem2_M1233_Exam", "exam_date": "2026-01", "max_marks": 100},

    # Semester III
    {"semester_number": 3, "subject_code": "M210A", "exam_type": "Theory", "exam_name": "Sem3_M210A_Exam", "exam_date": "2025-12", "max_marks": 100},
    {"semester_number": 3, "subject_code": "M214E", "exam_type": "Theory", "exam_name": "Sem3_M214E_Exam", "exam_date": "2025-12", "max_marks": 100},
    {"semester_number": 3, "subject_code": "M215C", "exam_type": "Theory", "exam_name": "Sem3_M215C_Exam", "exam_date": "2025-12", "max_marks": 100},
    {"semester_number": 3, "subject_code": "M215B", "exam_type": "Theory", "exam_name": "Sem3_M215B_Exam", "exam_date": "2025-12", "max_marks": 100},
    {"semester_number": 3, "subject_code": "M216D", "exam_type": "Theory", "exam_name": "Sem3_M216D_Exam", "exam_date": "2025-12", "max_marks": 100},
    {"semester_number": 3, "subject_code": "M2151", "exam_type": "Lab", "exam_name": "Sem3_M2151_Exam", "exam_date": "2025-12", "max_marks": 100},
    {"semester_number": 3, "subject_code": "M2162", "exam_type": "Lab", "exam_name": "Sem3_M2162_Exam", "exam_date": "2025-12", "max_marks": 100},
    {"semester_number": 3, "subject_code": "M21MC1", "exam_type": "Theory", "exam_name": "Sem3_M21MC1_Exam", "exam_date": "2025-12", "max_marks": 100},

    # Semester IV
    {"semester_number": 4, "subject_code": "M225B", "exam_type": "Theory", "exam_name": "Sem4_M225B_Exam", "exam_date": "2026-05", "max_marks": 100},
    {"semester_number": 4, "subject_code": "M225A", "exam_type": "Theory", "exam_name": "Sem4_M225A_Exam", "exam_date": "2026-05", "max_marks": 100},
    {"semester_number": 4, "subject_code": "M226A", "exam_type": "Theory", "exam_name": "Sem4_M226A_Exam", "exam_date": "2026-05", "max_marks": 100},
    {"semester_number": 4, "subject_code": "M225F", "exam_type": "Theory", "exam_name": "Sem4_M225F_Exam", "exam_date": "2026-05", "max_marks": 100},
    {"semester_number": 4, "subject_code": "M225E", "exam_type": "Theory", "exam_name": "Sem4_M225E_Exam", "exam_date": "2026-05", "max_marks": 100},
    {"semester_number": 4, "subject_code": "M2261", "exam_type": "Lab", "exam_name": "Sem4_M2261_Exam", "exam_date": "2026-05", "max_marks": 100},
    {"semester_number": 4, "subject_code": "M2252", "exam_type": "Lab", "exam_name": "Sem4_M2252_Exam", "exam_date": "2026-05", "max_marks": 100},
    {"semester_number": 4, "subject_code": "M2253", "exam_type": "Lab", "exam_name": "Sem4_M2253_Exam", "exam_date": "2026-05", "max_marks": 100},
    {"semester_number": 4, "subject_code": "M22MC2", "exam_type": "Theory", "exam_name": "Sem4_M22MC2_Exam", "exam_date": "2026-05", "max_marks": 100}
]

db.Exam.delete_many({})
db.Exam.insert_many(exams)

print("Exams inserted successfully!")

results = [

    # =========================
    # SEMESTER 1
    # =========================

    # M110A - Matrices and Calculus
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M110A",
        "exam_name": "Sem1_Matrices_and_Calculus_Exam",
        "marks_obtained": 40,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M110A",
        "exam_name": "Sem1_Matrices_and_Calculus_Exam",
        "marks_obtained": 44,
        "grade": "A+",
        "remarks": "External"
    },

    # M110D - Engineering Chemistry
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M110D",
        "exam_name": "Sem1_Engineering_Chemistry_Exam",
        "marks_obtained": 33,
        "grade": "B+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M110D",
        "exam_name": "Sem1_Engineering_Chemistry_Exam",
        "marks_obtained": 35,
        "grade": "B+",
        "remarks": "External"
    },

    # M110C - English for Skill Enhancement
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M110C",
        "exam_name": "Sem1_English_for_Skill_Enhancement_Exam",
        "marks_obtained": 32,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M110C",
        "exam_name": "Sem1_English_for_Skill_Enhancement_Exam",
        "marks_obtained": 44,
        "grade": "A",
        "remarks": "External"
    },

    # M115A - Elements of Computer Science and Engineering
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M115A",
        "exam_name": "Sem1_Elements_of_Computer_Science_and_Engineering_Exam",
        "marks_obtained": 42,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M115A",
        "exam_name": "Sem1_Elements_of_Computer_Science_and_Engineering_Exam",
        "marks_obtained": 0,
        "grade": "A+",
        "remarks": "External"
    },

    # M115B - Programming for Problem Solving
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M115B",
        "exam_name": "Sem1_Programming_for_Problem_Solving_Exam",
        "marks_obtained": 31,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M115B",
        "exam_name": "Sem1_Programming_for_Problem_Solving_Exam",
        "marks_obtained": 39,
        "grade": "A",
        "remarks": "External"
    },

    # M1102 - Chemistry Laboratory
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M1102",
        "exam_name": "Sem1_Chemistry_Laboratory_Exam",
        "marks_obtained": 39,
        "grade": "O",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M1102",
        "exam_name": "Sem1_Chemistry_Laboratory_Exam",
        "marks_obtained": 58,
        "grade": "O",
        "remarks": "External"
    },

    # M1103 - English Language and Communication Skills Lab
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M1103",
        "exam_name": "Sem1_English_Language_and_Communication_Skills_Lab_Exam",
        "marks_obtained": 37,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M1103",
        "exam_name": "Sem1_English_Language_and_Communication_Skills_Lab_Exam",
        "marks_obtained": 50,
        "grade": "A+",
        "remarks": "External"
    },

    # M1151 - Programming for Problem Solving Lab
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M1151",
        "exam_name": "Sem1_Programming_for_Problem_Solving_Lab_Exam",
        "marks_obtained": 37,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M1151",
        "exam_name": "Sem1_Programming_for_Problem_Solving_Lab_Exam",
        "marks_obtained": 48,
        "grade": "A+",
        "remarks": "External"
    },

    # M1132 - Computer Aided Engineering Graphics
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M1132",
        "exam_name": "Sem1_Computer_Aided_Engineering_Graphics_Exam",
        "marks_obtained": 35,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 1,
        "subject_code": "M1132",
        "exam_name": "Sem1_Computer_Aided_Engineering_Graphics_Exam",
        "marks_obtained": 41,
        "grade": "A",
        "remarks": "External"
    },


    # =========================
    # SEMESTER 2
    # =========================

    # M120A - Differential Equations and Vector Calculus
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M120A",
        "exam_name": "Sem2_Differential_Equations_and_Vector_Calculus_Exam",
        "marks_obtained": 26,
        "grade": "B+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M120A",
        "exam_name": "Sem2_Differential_Equations_and_Vector_Calculus_Exam",
        "marks_obtained": 34,
        "grade": "B+",
        "remarks": "External"
    },

    # M120B - Applied Physics
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M120B",
        "exam_name": "Sem2_Applied_Physics_Exam",
        "marks_obtained": 29,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M120B",
        "exam_name": "Sem2_Applied_Physics_Exam",
        "marks_obtained": 47,
        "grade": "A",
        "remarks": "External"
    },

    # M122A - Basic Electrical Engineering
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M122A",
        "exam_name": "Sem2_Basic_Electrical_Engineering_Exam",
        "marks_obtained": 36,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M122A",
        "exam_name": "Sem2_Basic_Electrical_Engineering_Exam",
        "marks_obtained": 43,
        "grade": "A",
        "remarks": "External"
    },

    # M125A - Data Structure
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M125A",
        "exam_name": "Sem2_Data_Structure_Exam",
        "marks_obtained": 33,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M125A",
        "exam_name": "Sem2_Data_Structure_Exam",
        "marks_obtained": 46,
        "grade": "A",
        "remarks": "External"
    },

    # M1252 - Data Structures Lab
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M1252",
        "exam_name": "Sem2_Data_Structure_Lab_Exam",
        "marks_obtained": 32,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M1252",
        "exam_name": "Sem2_Data_Structure_Lab_Exam",
        "marks_obtained": 47,
        "grade": "A",
        "remarks": "External"
    },

    # M1201 - Physics Laboratory
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M1201",
        "exam_name": "Sem2_Physics_Laboratory_Exam",
        "marks_obtained": 37,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M1201",
        "exam_name": "Sem2_Physics_Laboratory_Exam",
        "marks_obtained": 52,
        "grade": "A+",
        "remarks": "External"
    },

    # M1221 - Basic Electrical Engineering Lab
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M1221",
        "exam_name": "Sem2_Basic_Electrical_Engineering_Lab_Exam",
        "marks_obtained": 37,
        "grade": "O",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M1221",
        "exam_name": "Sem2_Basic_Electrical_Engineering_Lab_Exam",
        "marks_obtained": 59,
        "grade": "O",
        "remarks": "External"
    },

    # M1233 - Engineering & IT Workshop
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M1233",
        "exam_name": "Sem2_Engineering_and_IT_Workshop_Exam",
        "marks_obtained": 34,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 2,
        "subject_code": "M1233",
        "exam_name": "Sem2_Engineering_and_IT_Workshop_Exam",
        "marks_obtained": 52,
        "grade": "A+",
        "remarks": "External"
    },


    # =========================
    # SEMESTER 3
    # =========================

    # M210A - Probability and Statistics
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M210A",
        "exam_name": "Sem3_Probability_and_Statistics_Exam",
        "marks_obtained": 27,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M210A",
        "exam_name": "Sem3_Probability_and_Statistics_Exam",
        "marks_obtained": 43,
        "grade": "A",
        "remarks": "External"
    },

    # M214E - Digital Logic Design
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M214E",
        "exam_name": "Sem3_Digital_Logic_Design_Exam",
        "marks_obtained": 34,
        "grade": "B",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M214E",
        "exam_name": "Sem3_Digital_Logic_Design_Exam",
        "marks_obtained": 24,
        "grade": "B",
        "remarks": "External"
    },

    # M215C - Design and Analysis of Algorithms
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M215C",
        "exam_name": "Sem3_Design_and_Analysis_of_Algorithms_Exam",
        "marks_obtained": 30,
        "grade": "B+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M215C",
        "exam_name": "Sem3_Design_and_Analysis_of_Algorithms_Exam",
        "marks_obtained": 30,
        "grade": "B+",
        "remarks": "External"
    },

    # M215B - Python Programming
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M215B",
        "exam_name": "Sem3_Python_Programming_Exam",
        "marks_obtained": 29,
        "grade": "B+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M215B",
        "exam_name": "Sem3_Python_Programming_Exam",
        "marks_obtained": 40,
        "grade": "B+",
        "remarks": "External"
    },

    # M216D - Database Management Systems
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M216D",
        "exam_name": "Sem3_Database_Management_Systems_Exam",
        "marks_obtained": 33,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M216D",
        "exam_name": "Sem3_Database_Management_Systems_Exam",
        "marks_obtained": 51,
        "grade": "A+",
        "remarks": "External"
    },

    # M2151 - Python Programming Lab
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M2151",
        "exam_name": "Sem3_Python_Programming_Lab_Exam",
        "marks_obtained": 34,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M2151",
        "exam_name": "Sem3_Python_Programming_Lab_Exam",
        "marks_obtained": 54,
        "grade": "A+",
        "remarks": "External"
    },

    # M2162 - Database Management Systems Lab
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M2162",
        "exam_name": "Sem3_Database_Management_Systems_Lab_Exam",
        "marks_obtained": 26,
        "grade": "B+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M2162",
        "exam_name": "Sem3_Database_Management_Systems_Lab_Exam",
        "marks_obtained": 40,
        "grade": "B+",
        "remarks": "External"
    },

    # M21MC1 - Environmental Science
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M21MC1",
        "exam_name": "Sem3_Environmental_Science_Exam",
        "marks_obtained": 75,
        "grade": "SA",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 3,
        "subject_code": "M21MC1",
        "exam_name": "Sem3_Environmental_Science_Exam",
        "marks_obtained": 0,
        "grade": "SA",
        "remarks": "External"
    },


    # =========================
    # SEMESTER 4
    # =========================

    # M225B - Computer Organization and Architecture
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M225B",
        "exam_name": "Sem4_Computer_Organization_and_Architecture_Exam",
        "marks_obtained": 32,
        "grade": "B+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M225B",
        "exam_name": "Sem4_Computer_Organization_and_Architecture_Exam",
        "marks_obtained": 36,
        "grade": "B+",
        "remarks": "External"
    },

    # M225A - Mathematical Foundations of Computer Science
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M225A",
        "exam_name": "Sem4_Mathematical_Foundations_of_Computer_Science_Exam",
        "marks_obtained": 29,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M225A",
        "exam_name": "Sem4_Mathematical_Foundations_of_Computer_Science_Exam",
        "marks_obtained": 44,
        "grade": "A",
        "remarks": "External"
    },

    # M226A - Object Oriented Programming through Java
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M226A",
        "exam_name": "Sem4_Object_Oriented_Programming_through_Java_Exam",
        "marks_obtained": 32,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M226A",
        "exam_name": "Sem4_Object_Oriented_Programming_through_Java_Exam",
        "marks_obtained": 41,
        "grade": "A",
        "remarks": "External"
    },

    # M225F - Operating Systems
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M225F",
        "exam_name": "Sem4_Operating_Systems_Exam",
        "marks_obtained": 27,
        "grade": "B+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M225F",
        "exam_name": "Sem4_Operating_Systems_Exam",
        "marks_obtained": 37,
        "grade": "B+",
        "remarks": "External"
    },

    # M225E - Computer Networks
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M225E",
        "exam_name": "Sem4_Computer_Networks_Exam",
        "marks_obtained": 31,
        "grade": "A",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M225E",
        "exam_name": "Sem4_Computer_Networks_Exam",
        "marks_obtained": 44,
        "grade": "A",
        "remarks": "External"
    },

    # M2261 - Object Oriented Programming through Java Lab
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M2261",
        "exam_name": "Sem4_Object_Oriented_Programming_through_Java_Lab_Exam",
        "marks_obtained": 34,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M2261",
        "exam_name": "Sem4_Object_Oriented_Programming_through_Java_Lab_Exam",
        "marks_obtained": 52,
        "grade": "A+",
        "remarks": "External"
    },

    # M2252 - Operating Systems Lab
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M2252",
        "exam_name": "Sem4_Operating_Systems_Lab_Exam",
        "marks_obtained": 34,
        "grade": "A+",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M2252",
        "exam_name": "Sem4_Operating_Systems_Lab_Exam",
        "marks_obtained": 47,
        "grade": "A+",
        "remarks": "External"
    },

    # M2253 - Node JS / React JS / Django
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M2253",
        "exam_name": "Sem4_Node_JS_React_JS_Django_Exam",
        "marks_obtained": 36,
        "grade": "O",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M2253",
        "exam_name": "Sem4_Node_JS_React_JS_Django_Exam",
        "marks_obtained": 56,
        "grade": "O",
        "remarks": "External"
    },

    # M22MC2 - Gender Sensitization
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M22MC2",
        "exam_name": "Sem4_Gender_Sensitization_Exam",
        "marks_obtained": 74,
        "grade": "SA",
        "remarks": "Internal"
    },
    {
        "student_id": "24671A05R2",
        "semester_number": 4,
        "subject_code": "M22MC2",
        "exam_name": "Sem4_Gender_Sensitization_Exam",
        "marks_obtained": 0,
        "grade": "SA",
        "remarks": "External"
    }
]

db.Result.delete_many({})
db.Result.insert_many(results)

print("Results inserted successfully!")
print("Total result records:", len(results))