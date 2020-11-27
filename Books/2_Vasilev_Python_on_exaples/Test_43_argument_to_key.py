def show_me(first, second, *other, **by_name):
    print('first:', first)
    print('second:', second)
    print('other:', other)
    print('by_name:', by_name)


print(1)
show_me(10, 20, 30, 40, 50, 60)
print(2)
show_me(10, 20, 30, 40, third=30, fourth=40)
print(3)
show_me(10, 20, third=30, fourth=40)
print(4)
show_me(third=30, fourth=40)
