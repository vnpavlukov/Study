import os.path
from solution import File

path_to_file = 'some_filename'
print(os.path.exists(path_to_file))

file_obj = File(path_to_file)
print(os.path.exists(path_to_file))

file_obj.read()