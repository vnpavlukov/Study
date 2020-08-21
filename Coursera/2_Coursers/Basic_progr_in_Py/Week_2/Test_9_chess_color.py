cell_1_x = int(input())
cell_1_y = int(input())
cell_2_x = int(input())
cell_2_y = int(input())


def cell_color(x, y):
    if (x + y) % 2 == 0:
        return "black"
    else:
        return "white"


def check_cells():
    if cell_color(cell_1_x, cell_1_y) == cell_color(cell_2_x, cell_2_y):
        print("YES")
    else:
        print("NO")


check_cells()
