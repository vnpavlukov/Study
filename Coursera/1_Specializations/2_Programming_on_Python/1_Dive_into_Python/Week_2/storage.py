import argparse
import json
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()
key, val = args.key, args.val


def write_file(what, f_name):
    with open(f_name, 'w') as f:
        json.dump(what, f)


if val:
    if os.path.exists(storage_path):
        with open(storage_path) as file:
            my_dict = json.load(file)
            if key in my_dict:
                my_dict[key].append(val)
            else:
                my_dict[key] = [val]
        write_file(my_dict, storage_path)
    else:
        my_dict = {key: [val]}
        write_file(my_dict, storage_path)

else:
    if os.path.exists(storage_path):
        with open(storage_path) as file:
            my_dict = json.load(file)
            print(', '.join(my_dict[key]) if key in my_dict else None)
    else:
        print(None)

# python storage.py --key key_name --val value_1
# python storage.py --key key_name --val value_2
# python storage.py --key key_name
