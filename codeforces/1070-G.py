from collections import OrderedDict

cell_count, hero_count = map(int,input().split())
hero_tokens = []
initial_hero_position = set()
for _ in range(hero_count):
    cell, hp = map(int,input().split())
    hero_tokens.append((cell-1,hp))
    initial_hero_position.add(cell-1)

cells_original = [*map(int, input().split())]
# hero_tokens = OrderedDict(hero_tokens)

hero_index = {}
def get_hero_index(cell_no):
    global hero_index
    if cell_no in hero_index:
        return hero_index[cell_no]

    for i, hero_token in enumerate(hero_tokens):
        if hero_token[0] == cell_no:
            hero_index[cell_no] = i
            return i
    return -1

def get_next_hero_in_left(cur_pos, hero_order):
    for i in range(cur_pos -1, -1, -1):
        hero_index = get_hero_index(i)
        if hero_index < 0:
            continue
        if i in initial_hero_position and hero_index not in hero_order:
            return i
    return -1


def get_next_hero_in_right(cur_pos, hero_order):
    for i in range(cur_pos + 1, cell_count):
        hero_index = get_hero_index(i)
        if hero_index < 0:
            continue
        if i in initial_hero_position and hero_index not in hero_order:
            return i
    return -1


def move_hero_left(rally_cell, starting_cell, cells):
    if starting_cell < 0 or starting_cell >= cell_count:
        return False
    hp = hero_tokens[get_hero_index(starting_cell)][1]
    for i in range(starting_cell, rally_cell - 1, -1):
        hp += cells[i]
        cells[i] = 0
        if hp < 0:
            return False
    return True


def move_hero_right(rally_cell, starting_cell, cells):
    if starting_cell < 0 or starting_cell >= cell_count:
        return False
    hp = hero_tokens[get_hero_index(starting_cell)][1]
    for i in range(starting_cell, rally_cell + 1):
        hp += cells[i]
        cells[i] = 0
        if hp < 0:
            return False
    return True


def solve(rally_point, cells, hero_order):
    ok = False
    left = get_next_hero_in_left(rally_point, hero_order)
    right = get_next_hero_in_right(rally_point, hero_order)

    if left == -1 and right == -1:
        return True

    cells_copy = cells[:]
    hero_order_copy = hero_order[:]
    hero_move_success = move_hero_right(rally_point, left, cells_copy)
    
    if hero_move_success:
        hero_order_copy.append(get_hero_index(left))
        ok |= solve(rally_point, cells_copy, hero_order_copy) 
    if ok:
        hero_order = hero_order_copy[:]
        return True

    cells_copy = cells[:]
    hero_order_copy = hero_order[:]
    hero_move_success = move_hero_left(rally_point, right, cells_copy)
    if hero_move_success:
        hero_order_copy.append(get_hero_index(right))
        ok |= solve(rally_point, cells_copy, hero_order_copy) 
    if ok:
        hero_order = hero_order_copy[:]
        return True
    return ok


for i in range(cell_count):
    hero_order = []
    for hero_token in hero_tokens:
        if i == hero_token[0]:
            hero_order.append(get_hero_index(i))
            break
    cells = cells_original[:]
    ok = solve(i, cells, hero_order)
    if ok:
        print(i)
        print(hero_order)
        exit()
print(-1)