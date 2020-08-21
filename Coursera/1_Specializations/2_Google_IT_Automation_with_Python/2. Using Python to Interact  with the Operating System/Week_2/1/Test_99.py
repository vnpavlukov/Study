import os

cwd = os.getcwd()
os.chdir('test')
cwd = os.getcwd()
print(cwd)