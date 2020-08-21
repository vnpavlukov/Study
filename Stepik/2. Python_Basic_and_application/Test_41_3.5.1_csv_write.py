import csv

students = [
    ['Vova', 'Pavl', 70, 80, 90, 'Good job Vova'],
    ['Egor', 'Komarov', 99, 98, 100, 'You are the best']
]

with open("Test_41_3.5.1_example.csv", "a") as f:
    new_text = csv.writer(f)
    new_text.writerows(students)

    # for student in students:
    #     new_text.writerow(student)