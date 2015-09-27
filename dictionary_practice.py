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

for student in students:
    for item in students[student]:
        # item in this case contains the VALUE not the key
        print item
