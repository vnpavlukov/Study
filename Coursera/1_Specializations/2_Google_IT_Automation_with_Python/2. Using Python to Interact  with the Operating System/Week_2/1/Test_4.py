import os
import datetime


def file_date(filename):
    open(filename, 'w').close()
    mod_date_time = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    return mod_date_time.strftime("%Y-%m-%d")


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
