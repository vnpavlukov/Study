import pickle

shop_list_file = 'Test_4_shop_list.data'

shop_list = ['apple', 'mango', 'carrot']

f = open(shop_list_file, 'wb')  # режим бинарной записи
pickle.dump(shop_list, f) # add shop_list in file
f.close()

del shop_list

# read from file

f = open(shop_list_file, 'rb')
stored_list = pickle.load(f)
print(stored_list)
