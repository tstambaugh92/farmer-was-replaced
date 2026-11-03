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
    #This assumes coal veins can go vertically, which is not true.
    #Not deleting this second because this logic can be repurposes for iron
    #Also remove the god damn jitter.
    def find_coal():
        libfarm2.center()
        while get_ground_type() != Grounds.Coal:
            dig()
        return True

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
    libfarm2.center()
    clay_spaces = []
    next_clay = [1]
    def level_area(z_level):
        libfarm2.go_home()
        for _ in range(get_world_size() ** 2):
            while get_pos_z() > z_level and get_ground_type() != Grounds.Clay:
                dig()
            if get_ground_type() == Grounds.Clay:
                cur_pos = libfarm2.get_pos()
                clay_spaces.append(cur_pos)
            move(East)
            if get_pos_x() == 0:
                move(North)

    def plant_list(l):
        for i in l:
            libfarm2.go_to(i[0],i[1])
            plant(Entities.Rice)
            use_item(Items.Water)
    while get_ground_type() != Grounds.Clay:
        dig()
    level_area(get_pos_z())
    plant_list(clay_spaces)

    while len(next_clay) > 0:
        next_clay = []
        to_pop = []
        while len(clay_spaces) > 0:
            for i in range(len(clay_spaces)):
                libfarm2.go_to(clay_spaces[i][0],clay_spaces[i][1])
                if can_harvest():
                    harvest()
                    dig()
                    if get_ground_type() == Grounds.Clay:
                        next_clay.append(libfarm2.get_pos())
                    to_pop.append(i)
            idx = 0
            for i in to_pop:
                clay_spaces.pop(i - idx)
                idx += 1
                

        clay_spaces = []
        for i in next_clay:
            clay_spaces.append(i)

        plant_list(clay_spaces)

def harvest_bamboo():
    def plant_action(args=[]):
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Bamboo)
        use_item(Items.Water)

    def harvest_action(args=[]):

        m = measure()
        if m == None:
            return
        hover(m)
        if can_harvest():
            harvest()
            hover(1)
            plant(Entities.Bamboo)
            if get_water() < .4:
                use_item(Items.Water)
    

    libfarm2.func_on_land((-1,-1),(-1,-1),plant_action)
    while True:
        libfarm2.func_on_land((-1,-1),(-1,-1),harvest_action)

def harvest_iron():
    pass

#mini-games