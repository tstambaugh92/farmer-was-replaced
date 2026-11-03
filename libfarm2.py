def move_dir(dir,spaces):
    for _ in range(spaces):
        move(dir)

def go_home():
    go_to((0,0))
        
def go_to(cords):
    if len(cords) < 2:
        return
    else:
        x = cords[0]
        y = cords[1]
    if (x > get_world_size() - 1 or
        y > get_world_size() - 1 or
        x < 0 or y < 0):
            go_home()
            return
    cur_x = get_pos_x()
    cur_y = get_pos_y()
    if x == cur_x and y == cur_y:
        return
    size = get_world_size()
    half_size = size / 2
    
    NS = North
    add_ns = 1
    EW = East
    add_ew = 1
    if cur_x > x:
        if cur_x - x > half_size:
            pass #east
        else:
            EW = West
            add_ew = -1
    else:
        if x - cur_x > half_size:
            EW = West
            add_ew = -1
        else:
            pass #east
    if cur_y > y:
        if cur_y - y > half_size:
            pass #north
        else:
            NS = South
            add_ns = -1
    else:
        if y - cur_y > half_size:
            NS = South
            add_ns = -1
        else:
            pass #north
    while cur_x != x:
        move(EW)
        cur_x += add_ew
        if cur_x < 0:
            cur_x = size - 1
        elif cur_x >= size:
            cur_x = 0
    while cur_y != y:
        move(NS)
        cur_y += add_ns
        if cur_y < 0:
            cur_y = size -1
        elif cur_y >= size:
            cur_y = 0

def get_pos():
    return (get_pos_x(),get_pos_y(),get_pos_z())

def get_pos_xy():
    return (get_pos_x(),get_pos_y())

def center():
    s = get_world_size() // 2
    while get_pos_x() != s:
        move(East)
    while get_pos_y() != s:
        move(North)

def get_world_size_tup():
    return (get_world_size(),get_world_size())

def func_on_land(start=(-1,-1),end=(-1,-1),action=print,args = []):
    ws = get_world_size()
    if start == (-1,-1) or end == (-1,-1):
        start = (0,0)
        end = (ws-1,ws-1)

    def take_action(args):
        for _ in range(rows):
            args[0](args[1])
            move(North)

    go_to(start)
    cols = end[1] - start[1] + 1
    rows = end[0] - start[0] + 1

    for _ in range(cols-1):
        spawn_drone(take_action,[action,args])
        move(East)
    take_action([action,args])




