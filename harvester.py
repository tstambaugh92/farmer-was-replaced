import libfarm2

#Pre-mining farming

##Mining
def harvest_stone(offset=0):
    def runner(x,y):
        for _ in range(offset):
            if (x == 1):
                move(East)
            else:
                move(West)
            if(y == 1):
                move(North)
            else:
                move(South)

        while True:
            dig()

    libfarm2.go_home()
    spawn_drone(runner,1,1)
    move(West)
    spawn_drone(runner,-1,1)
    move(South)
    spawn_drone(runner,-1,-1)
    move(East)
    runner(1,-1)


def harvest_coal():
    def find_coal():
        libfarm2.go_home()
        max_checks = get_world_size() ** 2
        checks = 0
        while checks <= max_checks:
            if get_ground_type() == Grounds.Coal:
                return True
            checks += 1
            move(East)
            if get_pos_x() == 0:
                move(North)
        return False

    def map_vein(vein):
        if libfarm2.get_pos() in vein:
            return
        vein.append(libfarm2.get_pos())
        if(get_pos_x() > 0):
            move(West)
            while get_pos_z() > vein[0][2]-1 and get_ground_type() != Grounds.Coal:
                dig()
            if get_ground_type() == Grounds.Coal:
                map_vein(vein)
            move(East)
        if(get_pos_x() < get_world_size() - 1):
            move(East)
            while get_pos_z() > vein[0][2]-1 and get_ground_type() != Grounds.Coal:
                dig()
            if get_ground_type() == Grounds.Coal:
                map_vein(vein)
            move(West)
        if(get_pos_y() > 0):
            move(South)
            while get_pos_z() > vein[0][2]-1 and get_ground_type() != Grounds.Coal:
                dig()
            if get_ground_type() == Grounds.Coal:
                map_vein(vein)
            move(North)
        if(get_pos_y() < get_world_size() - 1):
            move(North)
            while get_pos_z() > vein[0][2]-1 and get_ground_type() != Grounds.Coal:
                dig()
            if get_ground_type() == Grounds.Coal:
                map_vein(vein)
            move(South)

    def sort_vein(vein):
        #orders by Z value
        tmp = []
        for i in vein:
            if len(tmp) == 0:
                tmp.append(i)
            else:
                idx = 0
                for j in tmp:
                    if i[2] > j[2]:
                        tmp.insert(idx,i)
                        break
                    idx += 1
                tmp.append(i)
        vein = tmp

    libfarm2.drill_layers(5)
    while True:
        while find_coal() == False:
            libfarm2.drill_layers(5)
        vein = []
        map_vein(vein)

        next = []
        for i in vein:
            libfarm2.go_to(i[0],i[1])
            dig()
            if get_ground_type() == Grounds.Coal:
                next.append(libfarm2.get_pos())

        while len(next) > 0:
            sort_vein(next)
            vein = []
            for i in next:
                vein.append.next()
            next = []
            for i in vein:
                libfarm2.go_to(i[0],i[1])
                dig()
                if get_ground_type() == Grounds.Coal:
                    next.append(libfarm2.get_pos())

def harvest_rice():
    pass

def harvest_bamboo():
    pass

#mini-games