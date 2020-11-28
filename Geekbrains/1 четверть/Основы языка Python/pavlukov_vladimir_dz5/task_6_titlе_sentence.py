"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

file_name_task_6 = 'task_6.txt'

with open(file_name_task_6, 'r', encoding="utf8") as f:
    objects_and_loads = dict()
    for line in f:
        split_line = line.split()
        school_object = split_line[0][:-1]

        work_load = 0
        for word in split_line:
            new_load = ''
            for letter in word:
                try:
                    _ = int(letter)
                    new_load += letter
                except:
                    continue
            if new_load:
                work_load += int(new_load)
        objects_and_loads[school_object] = work_load

print(objects_and_loads)