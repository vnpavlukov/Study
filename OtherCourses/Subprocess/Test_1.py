import subprocess

p = subprocess.call('dir', shell=True)

print(p)