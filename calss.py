from json import load


def rotbe(student_name, student_socore):

    if student_socore <= 100 and student_socore >= 90:
        grade = "A"
        data = [student_name, grade]

    elif student_socore <= 89 and student_socore >= 80:
        grade = "B"
        data = [student_name, grade]
    elif student_socore <= 79 and student_socore >= 70:
        grade = "C"
        data = [student_name, grade]
    elif student_socore <= 69 and student_socore >= 60:
        grade = "D"
        data = [student_name, grade]
    elif student_socore <= 59 and student_socore >= 0:
        grade = "F"
        data = [student_name, grade]
    else:
        print("Score Error!")

    print(data)


json_file = open('test.json')
data = load(json_file)
for p in data['people']:
    name = p['name']
    socore = p['socore']
    rotbe(name, socore)
