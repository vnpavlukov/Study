import csv

with open("Test_40_3.5.1_example.csv") as f:
    text_in_file = csv.reader(f)
    for row in text_in_file:
        print(row)