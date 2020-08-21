import os

dir_with_python_files = []

for current_dir, dirs, files in os.walk("main"):
    # print(current_dir, dirs, files)
    for file in files:
        if file[-3:] == '.py':
            dir_with_python_files.append(current_dir)

one = list(set(dir_with_python_files))


for i in sorted(one):
    print(i)

