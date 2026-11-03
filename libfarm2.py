def move_dir(dir,spaces):
    for _ in range(spaces):
        move(dir)

def go_home():
    go_to(0,0)
        
def go_to(x,y):
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


def drill_layers(layers):
    def runner():
        for _ in range(layers):
            dig()
    ws = get_world_size()
    max_bots = max_drones()
    if ws < max_bots:
        max_bots = ws
    zone_size = (ws**2 / max_bots) ** 0.5 // 1
    go_to(zone_size-1,zone_size-1)
    for _ in range(max_bots-1):
        spawn_drone(runner)
        if get_pos_x() + zone_size > ws:
            move_dir(North,zone_size)
            go_to(zone_size,get_pos_y())
        else:
            move_dir(East,zone_size)
    runner()

