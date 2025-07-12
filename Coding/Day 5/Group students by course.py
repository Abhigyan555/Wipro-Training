
data = [("Math", "Bobby"), ("Science", "Bablu"),
        ("Math", "Pinkie"), ("Math", "Ram"), ("Science", "Chintu")]


course_students = {}


for item in data:
    course = item[0]
    student = item[1]

    
    if course not in course_students:
        course_students[course] = []

    course_students[course].append(student)

print(course_students)
