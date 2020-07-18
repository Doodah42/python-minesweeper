'''
Created on 18-Jul-2020

@author: Christopher

  64    32    16    08    04    02    01
   B     H     S     c     c     c     c
   
  B - 1 = bomb, 0 = no bomb
  H - 1 = marked/unhidden, 0 = unmarked/hidden
  S - 1 = show number of surrounding bombs, 0 = don't show
  c - 4 bits for number of surrounding bombs
  
  1100000 - 96 - bomb & cell marked
  1000000 - 64 - bomb & cell unmarked
  0100000 - 32 - unhidden
  0011000 - 24 - 8 surrounding bombs, show number, hidden
  0010111 - 23 - 7        "                "         "
  0010110 - 22 - 6        "                "         "
  0010101 - 21 - 5        "                "         "
  0010100 - 20 - 4        "                "         "
  0010011 - 19 - 3        "                "         "
  0010010 - 18 - 2        "                "         "
  0010001 - 17 - 1        "                "         "
  0010000 - 16 - 0 surrounding bombs, show blank cell, hidden
  0001000 -  8 - 8 surrounding bombs, don't show number, hidden
  0000111 -  7 - 7        "                 "              "
  0000110 -  6 - 6        "                 "              "
  0000101 -  5 - 5        "                 "              "
  0000100 -  4 - 4        "                 "              "
  0000011 -  3 - 3        "                 "              "
  0000010 -  2 - 2        "                 "              "
  0000001 -  1 - 1        "                 "              "
  0000000 -  0 - 0        "                 "              "
'''
import random as rnd


def surrounding_bombs(the_list, cell_num, cols, rows, tot_cells):
    # determine col and row number
    col_number = cell_num % cols
    row_number = cell_num // cols
    
    # construct a list of cell positions (cp)
    # 0 - tl, 1 - t, 2 - tr
    # 3 - l ,      , 4 - r
    # 5 - br, 6 - b, 7 - br
    cp = [cell_num - cols - 1, cell_num - cols, cell_num - cols + 1,
          cell_num - 1, cell_num + 1,
          cell_num + cols - 1, cell_num + cols, cell_num + cols + 1]
    
    # store list of surrounding cells based on current cell position
    if 0 < col_number < cols - 1 and 0 < row_number < rows - 1:
        # middle of grid
        temp_list = cp.copy()
    
    elif row_number == 0 and cell_num != 0 and cell_num != cols - 1:
        # T row, not corners
        temp_list = [cp[3], cp[4], cp[5], cp[6], cp[7]]
    
    elif col_number == 0 and cell_num != 0 and \
         cell_num != tot_cells - cols:
        # L col, not corners
        temp_list = [cp[1], cp[1], cp[4], cp[6], cp[7]]

    elif col_number == cols - 1 and cell_num != cols - 1 and \
         cell_num != tot_cells - 1:
        # R col, not corners
        temp_list = [cp[0], cp[1], cp[3], cp[5], cp[6]]
    
    elif row_number == rows - 1 and cell_num != tot_cells - cols and \
         cell_num != tot_cells - 1:
        # B row, not corners
        temp_list = [cp[0], cp[1], cp[2], cp[3], cp[4]]
    
    elif cell_num == 0:
        # TL
        temp_list = [cp[4], cp[6], cp[7]]

    elif cell_num == cols - 1:
        # TR
        temp_list = [cp[3], cp[5], cp[6]]

    elif cell_num == tot_cells - cols:
        # BL
        temp_list = [cp[1], cp[2], cp[4]]

    elif cell_num == tot_cells - 1:
        # BR
        temp_list = [cp[0], cp[1], cp[3]]
    
    # count how many bombs are surrounding current cell position
    cnt = 0
    for x in temp_list:
        if the_list[x] == 64:
            cnt += 1

    # return number of bombs
    return cnt


def new_mine(cols, rows, bombs):
    some_list = []
    total_cells = cols * rows
    some_list.extend([64] * num_bombs)
    some_list.extend([0] * (total_cells - bombs))
    
    rnd.shuffle(some_list)

    for i, p in enumerate(some_list):
        if p != 64:
            some_list[i] = \
                  surrounding_bombs(some_list, i, cols, rows, total_cells)
    
    return some_list
    
num_cols = 5
num_rows = 4
num_bombs = 5

x = "y"
while x == "y":
    
    # create new mine
    my_list = new_mine(num_cols, num_rows, num_bombs)
    
    # group my_list into rows and columns and print to visualize
    for grp in range(0, len(my_list), num_cols):
            print(my_list[grp:grp + num_cols])
 
    print("-" * 20)
    x = input("New mine? ")






