import csv
import operator

criminal_2015 = {}
n = 1

with open("Test_42_3.5.2_Crimes.csv") as f:
    text_in_file = csv.reader(f)
    count = 0
    for row in text_in_file:
        if row[2][6:10] == "2015":
            if row[5] not in criminal_2015:
                criminal_2015[row[5]] = n
            else:
                criminal_2015[row[5]] += 1

sort_criminal_2015 = sorted(
    criminal_2015.items(),
    key=operator.itemgetter(1),
    reverse=True)

for a, b in sort_criminal_2015:
    print(a, b)
