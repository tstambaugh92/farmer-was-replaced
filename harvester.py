import libfarm

must_till_ls = [
	Entities.Carrot,
	Entities.Pumpkin,
	Entities.Sunflower,
	Entities.Cactus
]

gbl_water_rate = 0.4

#(X,Y) should be the top left corner of the pumpkin to harvest
def harvest_pumpkins(x,y,size,wait_for_growth=False):
	stepsNS = 0
	stepsEW = 0
	measure = []
	for i in range(size):
		measure.append([])
		for j in range(size):
			measure[i].append(0)
	dead_pumpkins = []
	libfarm.go_to(x,y)
	direction = South
	should_harvest = True
	for i in range(size):
		stepsNS = 0
		for j in range(size):
			if get_ground_type() != Grounds.Soil:
				till()
			if not can_harvest():
				should_harvest = False
				if get_entity_type() in [Entities.Dead_Pumpkin,None]:
					plant(Entities.Pumpkin)
					dead_pumpkins.append((get_pos_x(),get_pos_y()))
			if stepsNS < size - 1:
				move(direction)
				stepsNS+=1
		if stepsEW < size - 1:
			move(East)
			stepsEW+=1
		if direction == South:
			direction = North
		else:
			direction = South
	while wait_for_growth:
		i = 0
		if len(dead_pumpkins) < 50: #I should do timing tests to figure out the best num for this
			dead_pumpkins = libfarm.sort_bucket(dead_pumpkins,get_pos_x(),get_pos_y())
		while i < len(dead_pumpkins):
			dead_pumpkin = dead_pumpkins[i]
			libfarm.go_to(dead_pumpkin[0],dead_pumpkin[1])
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
				i += 1
			elif can_harvest():
				dead_pumpkins.pop(i)
			else:
				i += 1
		do_a_flip()
		if len(dead_pumpkins) == 0:
			wait_for_growth = False
			should_harvest = True
	if should_harvest:
		harvest()
		harvest_pumpkins(x,y,size)

def harvest_pumpkin_para(xy,size,fertilize=False,forever=False):
	if max_drones() >= size[1]:
		drone_count = size[1]
	else:
		drone_count = max_drones()

	def harvest_row():
		index = get_pos_x()
		orig_index = index
		libfarm.go_to(xy[0],xy[1] - index)
		while True:
			pumpkin_ids = []
			for i in range(size[0]):
				
				pumpkin_ids.append(measure())
				if len(pumpkin_ids) >= 6:
					if pumpkin_ids[-1] == pumpkin_ids[-6]:
						harvest()
				ent = get_entity_type()
				if ent in [Entities.Dead_Pumpkin,None]:
					plant(Entities.Pumpkin)
				elif ent != Entities.Pumpkin:
					if can_harvest():
						harvest()
					else:
						till()
					if get_ground_type() == Grounds.Grassland:
						till()
				if get_water() < gbl_water_rate:
					use_item(Items.Water)
				move(East)
			index += drone_count
			if index >= size[1]:
				if forever:
					index = orig_index
					# if num_items(Items.Pumpkin) >= 200000000:
					# 	return
				else:
					return
			libfarm.go_to(xy[0],xy[1] - index)

	libfarm.go_to(0,xy[1])
	for _ in range(drone_count - 1):
		spawn_drone(harvest_row)
		move(East)
	harvest_row()
	while num_drones() > 1:
		pass

def harvest_pumpkins_leaderboard():
	cords = [
		(1,30),(1,27),  (8,30),(8,27),  (15,30),(15,27),  (22,30),(22,27),
		(1,23),(1,20),  (8,23),(8,20),  (15,23),(15,20),  (22,23),(22,20),
		(1,16),(1,13),  (8,16),(8,13),  (15,16),(15,13),  (22,16),(22,13),
		(1, 9),(1, 6),  (8, 9),(8, 6),  (15, 9),(15, 6),  (22, 9),(22, 6)
	]
	#this will make 4 6x6 pumpkins, each with 2 drones attending it
	def drone_work(xy):
		#20260104 - This version got me to #40 on the Pumpkins leaderboard
		#			7:33.905
		libfarm.go_to(xy[0],xy[1])
		for i in range(6):
			till()
			plant(Entities.Pumpkin)
			if i < 5:
				move(East)
		move(South)
		for i in range(6):
			till()
			plant(Entities.Pumpkin)
			if i < 5:
				move(West)
		move(South)
		for i in range(6):
			till()
			plant(Entities.Pumpkin)
			if i < 5:
				move(East)

			
		libfarm.go_to_no_wrap(xy[0],xy[1])
		while num_items(Items.Pumpkin) < 200000000:
			dead_pumpkins = []
			libfarm.go_to_no_wrap(xy[0],xy[1])
			for i in range(6):
				if get_entity_type() in [Entities.Dead_Pumpkin,None]:
					plant(Entities.Pumpkin)
					dead_pumpkins.append((xy[0]+i,xy[1]))
				elif not can_harvest():
					dead_pumpkins.append((xy[0]+i,xy[1]))
				if get_water() < 0.75:
					use_item(Items.Water)
				if i < 5:
					move(East)
				else:
					move(South)

			for i in range(6,0,-1):
				if get_entity_type() in [Entities.Dead_Pumpkin,None]:
					plant(Entities.Pumpkin)
					dead_pumpkins.append((xy[0]+i-1,xy[1]-1))
				elif not can_harvest():
					dead_pumpkins.append((xy[0]+i-1,xy[1]-1))
				if get_water() < 0.75:
					use_item(Items.Water)
				if i > 1:
					move(West)
				else:
					move(South)

			for i in range(6):
				if get_entity_type() in [Entities.Dead_Pumpkin,None]:
					plant(Entities.Pumpkin)
					dead_pumpkins.append((xy[0]+i,xy[1]-2))
				elif not can_harvest():
					dead_pumpkins.append((xy[0]+i,xy[1]-2))
				if get_water() < 0.75:
					use_item(Items.Water)
				if i < 5:
					move(East)

			l = len(dead_pumpkins)
			i = 0
			harvested = False
			while l > 0:
				# if i==0 and l > 1  and l < 6:
				# 	dead_pumpkins = libfarm.sort_bucket(dead_pumpkins,get_pos_x(),get_pos_y())
				libfarm.go_to_no_wrap(dead_pumpkins[i][0],dead_pumpkins[i][1])
				ent = get_entity_type()
				if can_harvest():
					dead_pumpkins.pop(i)
				elif ent == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
					if l < 3: #this shaved off like 4 secs. Lot of waste but technically faster
						use_item(Items.Fertilizer)
					i += 1
				elif ent == None:
					#this is a case where the drone was in this loop,
					#a pumpkin finished growing, and the other drone
					#harvested
					harvested = True
					break
				else:
					i += 1
				l = len(dead_pumpkins)
				if l > 0:
					i = i % l

			flip_flop = True
			first = -1
			second = -2
			while not harvested:
				if flip_flop:
					libfarm.go_to(xy[0],xy[1])
					first = measure()
				else:
					libfarm.go_to(xy[0]+5,xy[1])
					second = measure()
				flip_flop = not flip_flop
				if get_entity_type() == None:
					harvested = True
					break
				if first == second:
					harvest()
					harvested = True
		clear()

	while len(cords) > 1:
		cord = cords.pop(0)
		def go_to_work():
			drone_work(cord)
		spawn_drone(go_to_work)
	cord = cords.pop(0)
	drone_work(cord)
		
def harvest_sunflower(x,y,size):
	stepsNS = 0
	stepsEW = 0
	direction = South
	libfarm.go_to(x,y)
	skip = False
	sunflowers = []
	
	for i in range(size):
		stepsNS = 0
		for j in range(size):
			if get_entity_type() != Entities.Sunflower:
				skip = True
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Sunflower)
			elif not can_harvest():
				skip = True
				return
			pet = measure()
			sunflowers.append((get_pos_x(),get_pos_y(),pet))
			if stepsNS < size - 1:
				move(direction)
				stepsNS+=1
		if stepsEW < size - 1:
			move(East)
			stepsEW+=1
		if direction == South:
			direction = North
		else:
			direction = South
	
	if skip:
		return
	
	#sunflowers = libfarm.sun_buckets(sunflowers) this is slow as shit lol

	buckets = []
	for _ in range(16):
		buckets.append([])

	for flower in sunflowers:
		buckets[flower[2]].append(flower)

	for i in range(15,6,-1):
		for flower in buckets[i]:
			libfarm.go_to(flower[0],flower[1])
			harvest() 

	plant_crop(x,y,size,Entities.Sunflower)

	
def harvest_sunflower_para(xy,size):
	if max_drones() >= size[1]:
		drone_count = size[1]
	else:
		drone_count = max_drones()

	for i in range(15,6,-1): #get the 15 flowers, then 14, etc...
		def harvest_row():
			#a drone should be at X,Y to start,
			#where X basically their drone number.
			#if theres 4 drones, the drone at 1,Y will get row 1,1+4,1+4*2, etc
			#until it goes out of bounds on the size
			#Y will be the petal count its trying to get this pass.
			index = get_pos_x()
			flower_power = get_pos_y()
			libfarm.go_to(xy[0],xy[1]-index)
			while True:
				for in_i in range(size[0]):
					if measure() == flower_power:
						while not can_harvest():
							pass
						harvest()
					if get_water() < gbl_water_rate:
						use_item(Items.Water)
					move(East)
				index += drone_count
				if index >= size[1]:
					return
				libfarm.go_to(xy[0],xy[1] - index)
			
		libfarm.go_to(0,i) #this communicates the flower petal cnt
		for j in range(drone_count - 1):
			spawn_drone(harvest_row)
			move(East)
		harvest_row()
		while num_drones() > 1:
			pass
	
	plant_crop_para(xy,size,Entities.Sunflower)



def harvest_plant(x,y,size,cur_plant,tree=False,fertilize=False):
	if cur_plant in must_till_ls:
		must_till = True
	else:
		must_till = False
	to_plant = cur_plant
	stepsNS = 0
	stepsEW = 0
	libfarm.go_to(x,y)
	direction = South
	for i in range(size):
		stepsNS = 0
		for j in range(size):
			if tree:
				to_plant = cur_plant
				if get_pos_y() % 2 == 0:
					if get_pos_x() % 2 == 0:
						to_plant = Entities.Tree
				elif get_pos_x() % 2 != 0:
					to_plant = Entities.Tree
			if must_till and get_ground_type() != Grounds.Soil:
				till()
			elif not must_till and get_ground_type() == Grounds.Soil:
				till()
			if can_harvest():
				harvest()
				plant(to_plant)
				if fertilize:
					use_item(Items.Fertilizer)
			elif get_entity_type() != to_plant:
				plant(to_plant)
				if fertilize:
					use_item(Items.Fertilizer)
			if stepsNS < size - 1:
				move(direction)
				stepsNS+=1
		if stepsEW < size - 1:
			move(East)
			stepsEW+=1
		if direction == South:
			direction = North
		else:
			direction = South

def harvest_plant_rec(xy,size,cur_plant,tree=False,fertilize=False):
	if cur_plant in must_till_ls:
		must_till = True
	else:
		must_till = False
	to_plant = cur_plant
	stepsNS = 0
	stepsEW = 0
	libfarm.go_to(xy[0],xy[1])
	direction = South
	for i in range(size[0]):
		stepsNS = 0
		for j in range(size[1]):
			if tree:
				to_plant = cur_plant
				if get_pos_y() % 2 == 0:
					if get_pos_x() % 2 == 0:
						to_plant = Entities.Tree
				elif get_pos_x() % 2 != 0:
					to_plant = Entities.Tree
			if must_till and get_ground_type() != Grounds.Soil:
				till()
			elif not must_till and get_ground_type() == Grounds.Soil:
				till()
			if can_harvest():
				harvest()
				plant(to_plant)
				if fertilize:
					use_item(Items.Fertilizer)
			elif get_entity_type() != to_plant:
				plant(to_plant)
				if fertilize:
					use_item(Items.Fertilizer)
			if stepsNS < size[1] - 1:
				move(direction)
				stepsNS+=1
		if stepsEW < size[0] - 1:
			move(East)
			stepsEW+=1
		if direction == South:
			direction = North
		else:
			direction = South

def harvest_crop_para(xy,size,crop,trees=False,fertilize=False,forever=False):
	if max_drones() >= size[1]:
		drone_count = size[1]
	else:
		drone_count = max_drones()
	
	def harvest_row():
		index = get_pos_x()
		orig_index = index
		libfarm.go_to(xy[0],xy[1] - index)
		while True:
			for _ in range(size[0]):
				if can_harvest():
					harvest()
					if crop in must_till_ls:
						if get_ground_type() != Grounds.Soil:
							till()
					else:
						if get_ground_type() != Grounds.Grassland:
							till()
					plant(crop)
					if get_water() < gbl_water_rate:
						use_item(Items.Water)
				elif get_entity_type() == None:
					if crop in must_till_ls:
						if get_ground_type() != Grounds.Soil:
							till()
					else:
						if get_ground_type() != Grounds.Grassland:
							till()
					plant(crop)
				move(East)
			index += drone_count
			if index >= size[1]:
				if forever:
					index = orig_index
				else:
					return
			libfarm.go_to(xy[0],xy[1] - index)

	libfarm.go_to(0,xy[1])
	for _ in range(drone_count - 1):
		spawn_drone(harvest_row)
		move(East)
	harvest_row()
	while num_drones() > 1:
		pass
			
def plant_crop(x,y,size,crop):
	libfarm.go_to(x,y)
	must_till = crop in must_till_ls
	stepsNS = 0
	stepsEW = 0
	direction = South
	for i in range(size):
		stepsNS = 0
		for j in range(size):
			if must_till and get_ground_type() != Grounds.Soil:
				till()
			elif not must_till and get_ground_type() == Grounds.Soil:
				till()
			if get_entity_type() != None and get_entity_type() != crop:
				if can_harvest():
					harvest()
				else:
					till()
					till()
			plant(crop)
			if stepsNS < size - 1:
				move(direction)
				stepsNS+=1
		if stepsEW < size - 1:
			move(East)
			stepsEW+=1
		if direction == South:
			direction = North
		else:
			direction = South

def plant_crop_para(xy,size,crop):
	if max_drones() >= size[1]:
		drone_count = size[1]
	else:
		drone_count = max_drones()
	
	def plant_row():
		index = get_pos_x()
		libfarm.go_to(xy[0],xy[1] - index)
		while True:
			for _ in range(size[0]):
				if can_harvest():
					harvest()
				if crop in must_till_ls:
					if get_ground_type() != Grounds.Soil:
						till()
				else:
					if get_ground_type() != Grounds.Grassland:
						till()
				if get_entity_type() != None:
					till()
					till()
				plant(crop)
				move(East)
			index += drone_count
			if index >= size[1]:
				return
			libfarm.go_to(xy[0],xy[1] - index)

	libfarm.go_to(0,xy[1])
	for _ in range(drone_count - 1):
		spawn_drone(plant_row)
		move(East)
	plant_row()
	while num_drones() > 1:
		pass

def harvest_cactus(x,y,size):
	crop_map = []

	# libfarm.go_to(x+size-1,y)
	# if can_harvest():
	# 	harvest()

	#libfarm.go_to(x,y)
	direction = East
	for i in range(size):
		new_row = []
		for j in range(size):
			# if can_harvest():
			# 	harvest()
			# if get_ground_type() != Grounds.Soil:
			# 	till()
			till()
			plant(Entities.Cactus)

			lvl = measure()
			# if direction == East:
			while lvl > j+5 or lvl < i-5:
				till()
				till()
				plant(Entities.Cactus)
				lvl = measure()
			
			new_row.append(lvl)
			# else:
			# 	if lvl < j-4:
			# 		harvest()
			# 		plant(Entities.Cactus)
			# 		lvl = measure()
			# 	new_row.insert(0,lvl)
			# if j < size - 1:
			# 	move(direction)
			move(East)
				
		#crop_map.append(new_row)
		crop_map.insert(0,new_row)
		move(North)
		# if direction == East:
		# 	direction = West
		# else:
		# 	direction = East
	libfarm.cactus_sort(crop_map,(x,y))
	return

def harvest_cactus_leaderboard():

	def jobA():
		ls = []
		redo = []
		y = get_pos_y()
		x = 0
		for i in range(32):
			till()
			plant(Entities.Cactus)
			lvl = measure()
			if (x <= 15 and y <= 15) and lvl >= 5:
				redo.append((x,y))
			if (x > 15 and y > 15) and lvl < 5:
				redo.append((x,y))
			ls.append([(x,y),lvl])
			move(East)
			x += 1
		while len(redo) > 0:
			i = 0
			l = len(redo)
			for j in range(l):
				if i > l - 1:
					break
				kill_em = redo[i]
				libfarm.go_to(kill_em[0],kill_em[1])
				while not can_harvest():
					pass
				till()
				till()
				plant(Entities.Cactus)
				use_item(Items.Water)
				lvl = measure()
				ls[kill_em[0]][1] = lvl
				go_on = False
				if (kill_em[0] > 15 and y > 15) and lvl < 5:
					go_on = True
				if (kill_em[0] <= 15 and y <=15) and lvl >= 5:
					go_on = True
				if go_on:
					i += 1
				else:
					redo.pop(i)
			# l = len(redo)
			# for i in range(l):
			# 	kill_em = redo[l]
			# 	libfarm.go_to(kill_em[0],kill_em[1])
			# 	while not can_harvest():
			# 		pass
			# 	till()
			# 	till()
			# 	plant(Entities.Cactus)
			# 	lvl = measure
			# 	ls[kill_em[0]][1] = lvl


		libfarm.insert_sort(ls,East)

	def jobB():
		x = get_pos_x()
		y = 0
		ls = []
		for i in range(32):
			lvl = measure()
			ls.append([(x,y),lvl])
			move(North)
			y += 1
		libfarm.insert_sort(ls,North)

	for col in range(31):
		spawn_drone(jobA)
		move(North)
	jobA()
	libfarm.go_home()
	while num_drones() > 1:
		pass
	for row in range(31):
		spawn_drone(jobB)
		move(East)
	jobB()
	libfarm.go_to(31,31)
	while num_drones() > 1:
		pass
	harvest()

def clear_field():
	plant_crop_para((0,get_world_size()-1),(get_world_size(),get_world_size()),Entities.Grass)

