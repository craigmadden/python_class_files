def student_info(students):
    for student in students:
        print student
        print students[student]["homework"]
        print students[student]["quizzes"]
        print students[student]["tests"]
        print ''

# Better solution
def student_info2(students):
    for student in students:
        print student
        current_student = students[student]
        for item in current_student:
            print item, current_student[item]
            # prints out the key name "homework", "quizes", etc and then the value

def average(list_nums):
    return sum(list_nums) / float(len(list_nums))


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    homework = homework * .10
    quizzes = quizzes * .30
    tests = tests * .60
    return homework + quizzes + tests

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(students[student]))
    return average(results)

def main():
    students =  {
        "Lloyd": {
        "homework": [90.0,97.0,75.0,92.0],
        "quizzes": [88.0,40.0,94.0],
        "tests": [75.0,90.0]
        },
        "Alice": {
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes": [82.0, 83.0, 91.0],
        "tests": [89.0, 97.0]
        },
        "Tyler": {
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "tests": [100.0, 100.0]
        }
    }
    student_info2(students)
    class_avg = get_class_average(students)
    print "%.2f" % class_avg
    print get_letter_grade(class_avg)

if __name__ == '__main__':
    main()