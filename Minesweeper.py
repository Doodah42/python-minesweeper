'''
Created on 11-Jul-2020

@author: Christopher
'''
import random as rnd


def surrounding_cell_list(cell):
    global horz, vert
    x = cell[1]
    y = cell[0]
    xlim = horz - 1
    ylim = vert - 1
    if y == 0 and x == 0: # TL
        return [[y, x], [y, x + 1], [y + 1, x + 1], [y + 1, x]]
    elif y == 0 and x == xlim: # TR
        return [[y, x], [y + 1, x], [y + 1, x - 1], [y, x - 1]]
    elif y == 0 and 0 < x < xlim: # T not corners
        return [[y, x], [y, x + 1], [y + 1, x + 1], [y + 1, x], [y + 1, x - 1], [y, x - 1]]
    elif x == 0 and y == ylim: # BL
        return [[y, x], [y, x + 1], [y - 1, x], [y - 1, x + 1]]
    elif x == 0 and 0 < y < ylim: # L not corners
        return [[y, x], [y, x + 1], [y + 1, x + 1], [y + 1, x], [y - 1, x], [y - 1, x + 1]]
    elif x == xlim and y == ylim: # BR
        return [[y, x], [y, x - 1], [y - 1, x - 1], [y - 1, x]]
    elif y == ylim and 0 < x < xlim: # B not corners
        return [[y, x], [y, x + 1], [y, x - 1], [y - 1, x - 1], [y - 1, x], [y - 1, x + 1]]
    elif x == xlim and 0 < y < ylim: # R not corners
        return [[y, x], [y + 1, x], [y + 1, x - 1], [y, x - 1], [y - 1, x - 1], [y - 1, x]]
    else: # middle
        return [[y, x], [y, x + 1], [y + 1, x + 1], [y + 1, x], [y + 1, x - 1], [y, x - 1], [y - 1, x - 1], [y - 1, x], [y - 1, x + 1]]


def get_number_of_bombs(theCell, theList):
#     global grid_list
    temp_list = []
    surrounds = surrounding_cell_list(theCell)
    for _, p in enumerate(surrounds):
        temp_list.append(theList[p[0]][p[1]][0])
    return temp_list.count(9)


def new_grid(horizontal_cells, vertical_cells, bombs):
    # populate my_list with the specified number bombs
    # add zeros to the rest based on total_cells
    main_list = []
    my_list = []
    total_cells = horizontal_cells * vertical_cells
    my_list.extend([9] * bombs)
    my_list.extend([0] * (total_cells - bombs))
    
    # shuffle my_list so bombs are randomly placed in the list
    rnd.shuffle(my_list)
    
    # create grid_list to hold my_list in vert rows by horz columns
    for grp in range(0, len(my_list), horizontal_cells):
        main_list.append(my_list[grp:grp + horizontal_cells])
    
    # replace each entry with a list so the number of surrounding bombs
    # can be stored alongside the state of the cell
    for g, p in enumerate(main_list):
        for h, q in enumerate(p):
            main_list[g][h] = [q, 0, 0, 0]
    
    # store number of bombs surrounding each cell
    for i, p in enumerate(main_list):
        for j, q in enumerate(p):
            main_list[i][j][1] = get_number_of_bombs([i, j], main_list)

    return main_list

horz = 5
vert = 7
number_of_bombs = 5
# when grid_list is populated the integers represent:
# [i0, i1, i2, i3, i4]
# i0 - 9 is a bomb, 0 is no bomb
# i1 - number of bombs surrounding and including the cell
# i2 - 1 cell is revealed, 0 is not revealed
# i3 - 1 is show number of bombs, 0 show nothing
grid_list = []

x = "y"
while x == "y":
    grid_list = new_grid(horz, vert, number_of_bombs)
    for g in grid_list:
        print(g)
    x = input("New grid? ")
