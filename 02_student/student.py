from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to University Management System"}

@app.get("/{university}/{student}")
def student_profile(university:str, student:str):
    return {"University": university, "Student": student}

@app.get("/{university}/student/{student}")
def student_profile1(university:str, student:str):
    profile = f"""
                University Name: {university}
                Student Name: {student}
                Current Semester: 8th
                """
    return profile

@app.get("/{university}/student/{student}/course/{course}")
def student_profile2(university:str, student:str, course:str):
    profile = {
                "University Name": university,
                "Student Name": student,
                "Current Semester": "8th",
                "Course": course
               }
    return profile

@app.get("/{university}/student/{student}/course/{course}/grade/{grade}")
def student_profile3(university:str, student:str, course:str, grade:str):
    profile = f"""
                """
    return 
    


