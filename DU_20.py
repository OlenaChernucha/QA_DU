import json

students = [
    {"name": "Alice", "course": 1, "group": "A", "grades": {"math": 85, "physics": 92}},
    {"name": "Bob", "course": 2, "group": "B", "grades": {"math": 65, "physics": 75}},
    {"name": "Charlie", "course": 1, "group": "A", "grades": {"math": 95, "physics": 90}},
    {"name": "David", "course": 2, "group": "A", "grades": {"math": 78, "physics": 85}},
    {"name": "Eve", "course": 1, "group": "B", "grades": {"math": 58, "physics": 72}},
    {"name": "Frank", "course": 2, "group": "B", "grades": {"math": 88, "physics": 90}},
    {"name": "Grace", "course": 1, "group": "A", "grades": {"math": 92, "physics": 85}},
    {"name": "Hannah", "course": 2, "group": "A", "grades": {"math": 72, "physics": 80}},
    {"name": "Ivan", "course": 1, "group": "B", "grades": {"math": 68, "physics": 72}},
    {"name": "Judy", "course": 2, "group": "B", "grades": {"math": 90, "physics": 95}}
]

students_2 = [student for student in students if student['course'] == 2]

math_grades = [student['grades']['math'] for student in students_2]
average_math_grade = sum(math_grades) / len(math_grades)

top_math_students = [student for student in students_2 if student['grades']['physics'] > average_math_grade]
top_math_students.sort(key=lambda x: x['grades']['physics'], reverse=True)

for student in top_math_students:
    print(f"Name: {student['name']}, Math Grade: {student['grades']['math']}, Physics Grade: {student['grades']['physics']}")

