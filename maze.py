import libfarm

def spawn(size,xy=(0,0)):
	libfarm.go_to(xy[0],xy[1])
	if get_entity_type() != Entities.Grass:
		if get_ground_type() == Grounds.Soil:
			till()
		plant(Entities.Grass)
	plant(Entities.Bush)
	num_sub = size*(2**(num_unlocked(Unlocks.Mazes)-1))
	use_item(Items.Weird_Substance,num_sub)

def solve():
	while get_entity_type() != Entities.Treasure:
		dir = (random() * 4 + 1) // 1
		if dir == 1:
			move(North)
		elif dir == 2:
			move(South)
		elif dir == 3:
			move(East)
		elif dir == 4:
			move(West)

def solve_ok(size,xy=(0,0),repeat=0):
	maze_map = {}
	
	#start = size // 2
	perf_order = get_ideal_order((get_pos_x(),get_pos_y()),measure())
	maze_map[(xy[0],xy[1])] = [perf_order[0],perf_order[1],perf_order[2],perf_order[3]]
	cur_pos = [xy[0],xy[1]]

	while get_entity_type() != Entities.Treasure:
		if num_items(Items.Gold) > 9863168:
			return False
		dir = maze_map[(cur_pos[0],cur_pos[1])].pop(0)
		while not move(dir):
			dir = maze_map[(cur_pos[0],cur_pos[1])].pop(0)
		perf_order = get_ideal_order((get_pos_x(),get_pos_y()),measure())
		if dir == North:
			cur_pos[1] += 1
			if (cur_pos[0],cur_pos[1]) not in maze_map:
				maze_map[(cur_pos[0],cur_pos[1])] = [perf_order[0],perf_order[1],perf_order[2],perf_order[3]]
				maze_map[(cur_pos[0],cur_pos[1])].remove(South)
				maze_map[(cur_pos[0],cur_pos[1])].append(South)
		elif dir == South:
			cur_pos[1] -= 1
			if (cur_pos[0],cur_pos[1]) not in maze_map:
				maze_map[(cur_pos[0],cur_pos[1])] = [perf_order[0],perf_order[1],perf_order[2],perf_order[3]]
				maze_map[(cur_pos[0],cur_pos[1])].remove(North)
				maze_map[(cur_pos[0],cur_pos[1])].append(North)
		elif dir == East:
			cur_pos[0] += 1
			if (cur_pos[0],cur_pos[1]) not in maze_map:
				maze_map[(cur_pos[0],cur_pos[1])] = [perf_order[0],perf_order[1],perf_order[2],perf_order[3]]
				maze_map[(cur_pos[0],cur_pos[1])].remove(West)
				maze_map[(cur_pos[0],cur_pos[1])].append(West)
		elif dir == West:
			cur_pos[0] -= 1
			if (cur_pos[0],cur_pos[1]) not in maze_map:
				maze_map[(cur_pos[0],cur_pos[1])] = [perf_order[0],perf_order[1],perf_order[2],perf_order[3]]
				maze_map[(cur_pos[0],cur_pos[1])].remove(East)
				maze_map[(cur_pos[0],cur_pos[1])].append(East)
	if repeat > 0:
		use_item(Items.Weird_Substance,size*(2**(num_unlocked(Unlocks.Mazes)-1)))
		return True #solve_ok(size,(cur_pos[0],cur_pos[1]),repeat-1)
	harvest()

def get_ideal_order(cur,target):
	x_dist = abs(cur[0] - target[0])
	y_dist = abs(cur[1] - target[1])
	new_order = []
	if y_dist > x_dist: #prefer going up or down
		if cur[1] > target[1]:
			new_order.append(South)
			if cur[0] > target[0]:
				new_order.append(West)
				new_order.append(East)
			else:
				new_order.append(East)
				new_order.append(West)
			new_order.append(North)
		else:
			new_order.append(North)
			if cur[0] > target[0]:
				new_order.append(West)
				new_order.append(East)
			else:
				new_order.append(East)
				new_order.append(West)
			new_order.append(South)
	else: #prefer going left or right
		if cur[0] > target[0]:
			new_order.append(West)
			if cur[1] > target[1]:
				new_order.append(South)
				new_order.append(North)
			else:
				new_order.append(North)
				new_order.append(South)
			new_order.append(East)
		else:
			new_order.append(East)
			if cur[1] > target[1]:
				new_order.append(South)
				new_order.append(North)
			else:
				new_order.append(North)
				new_order.append(South)
			new_order.append(West)
	return new_order

def solve_para(size,pref_order,repeats=0):
	substance_count = num_items(Items.Weird_Substance)
	maze_map = []
	for i in range(size):
		maze_map.append([])
		for j in range(size):
			maze_map[i].append([])
	
	#start = size // 2
	maze_map[get_pos_x()][get_pos_y()] = [pref_order[0],pref_order[1],pref_order[2],pref_order[3]]
	cur_pos = [get_pos_x(),get_pos_y()]

	while get_entity_type() != Entities.Treasure:
		if get_entity_type() != Entities.Hedge:
			return
		if substance_count > num_items(Items.Weird_Substance):
			new_cords = measure()
			new_order = get_ideal_order(cur_pos,new_cords)
			return solve_para(size,new_order,repeats-1)
		dir = maze_map[cur_pos[0]][cur_pos[1]].pop(0)
		while not move(dir):
			dir = maze_map[cur_pos[0]][cur_pos[1]].pop(0)
		#pref_order = get_ideal_order((get_pos_x(),get_pos_y()),measure())
		if dir == North:
			cur_pos[1] += 1
			if len(maze_map[cur_pos[0]][cur_pos[1]]) == 0:
				maze_map[cur_pos[0]][cur_pos[1]] = [pref_order[0],pref_order[1],pref_order[2],pref_order[3]]
				maze_map[cur_pos[0]][cur_pos[1]].remove(South)
				maze_map[cur_pos[0]][cur_pos[1]].append(South)
		elif dir == South:
			cur_pos[1] -= 1
			if len(maze_map[cur_pos[0]][cur_pos[1]]) == 0:
				maze_map[cur_pos[0]][cur_pos[1]] = [pref_order[0],pref_order[1],pref_order[2],pref_order[3]]
				maze_map[cur_pos[0]][cur_pos[1]].remove(North)
				maze_map[cur_pos[0]][cur_pos[1]].append(North)
		elif dir == East:
			cur_pos[0] += 1
			if len(maze_map[cur_pos[0]][cur_pos[1]]) == 0:
				maze_map[cur_pos[0]][cur_pos[1]] = [pref_order[0],pref_order[1],pref_order[2],pref_order[3]]
				maze_map[cur_pos[0]][cur_pos[1]].remove(West)
				maze_map[cur_pos[0]][cur_pos[1]].append(West)
		elif dir == West:
			cur_pos[0] -= 1
			if len(maze_map[cur_pos[0]][cur_pos[1]]) == 0:
				maze_map[cur_pos[0]][cur_pos[1]] = [pref_order[0],pref_order[1],pref_order[2],pref_order[3]]
				maze_map[cur_pos[0]][cur_pos[1]].remove(East)
				maze_map[cur_pos[0]][cur_pos[1]].append(East)
	if repeats > 0:
		use_item(Items.Weird_Substance,size*(2**(num_unlocked(Unlocks.Mazes)-1)))
		new_cords = measure()
		new_order = get_ideal_order(cur_pos,new_cords)
		return solve_para(size,new_order,repeats-1)
	harvest()
	

def four_drones(reps=0):
	size = get_world_size()
	spawn(size,(get_pos_x(),get_pos_y()))
	def jobA():
		solve_para(size,[North,South,East,West],reps)

	def jobB():
		solve_para(size,[South,North,West,East],reps)

	def jobC():
		solve_para(size,[East,West,North,South],reps)

	def jobD():
		solve_para(size,[West,East,South,North],reps)

	spawn_drone(jobA)
	spawn_drone(jobB)
	spawn_drone(jobC)
	jobD()

def eight_drones(reps=0):
	size = get_world_size()
	spawn(size,(get_pos_x(),get_pos_y()))
	def jobA():
		change_hat(Hats.Brown_Hat)
		solve_para(size,[North,South,East,West],reps)

	def jobB():
		change_hat(Hats.Gold_Hat)
		solve_para(size,[South,North,West,East],reps)

	def jobC():
		change_hat(Hats.Pumpkin_Hat)
		solve_para(size,[East,West,North,South],reps)

	def jobD():
		change_hat(Hats.Traffic_Cone)
		solve_para(size,[West,East,South,North],reps)

	def jobE():
		change_hat(Hats.Wizard_Hat)
		solve_para(size,[North,South,West,East],reps)
	
	def jobF():
		change_hat(Hats.Cactus_Hat)
		solve_para(size,[South,North,West,East],reps)

	def jobG():
		change_hat(Hats.Purple_Hat)
		solve_para(size,[East,West,South,North],reps)

	def jobH():
		change_hat(Hats.Straw_Hat)
		solve_para(size,[West,East,North,South],reps)

	spawn_drone(jobA)
	spawn_drone(jobB)
	spawn_drone(jobC)
	spawn_drone(jobD)
	spawn_drone(jobE)
	spawn_drone(jobF)
	spawn_drone(jobG)
	jobH()

def twenty_four_drones(reps=0):
	dirs = [
		[North, South, East, West], [North, South, West, East], [North, East, South, West], [North, East, West, South], [North, West, South, East], [North, West, East, South],
		[South, North, East, West], [South, North, West, East], [South, East, North, West], [South, East, West, North], [South, West, North, East], [South, West, East, North],
		[East, North, South, West], [East, North, West, South], [East, South, North, West], [East, South, West, North], [East, West, North, South], [East, West, South, North],
		[West, North, South, East], [West, North, East, South], [West, South, North, East], [West, South, East, North], [West, East, North, South], [West, East, South, North]
	]

	while len(dirs) > 1:
		i = dirs.pop(0)
		def drone_solve():
			solve_para(get_world_size(),i,reps)
		spawn_drone(drone_solve)
	i = dirs.pop(0)
	solve_para(get_world_size(),i,reps)

#coordinerates for 25 6x6 maxes
# ls = [
# 	(3+6*0,29-6*0),(3+6*1,29-6*0),(3+6*2,29-6*0),(3+6*3,29-6*0),(3+6*4,29-6*0),
# 	(3+5*0,29-6*1),(3+6*1,29-6*1),(3+6*2,29-6*1),(3+6*3,29-6*1),(3+6*4,29-6*1),
# 	(3+5*0,29-6*2),(3+6*1,29-6*2),(3+6*2,29-6*2),(3+6*3,29-6*2),(3+6*4,29-6*2),
# 	(3+5*0,29-6*3),(3+6*1,29-6*3),(3+6*2,29-6*3),(3+6*3,29-6*3),(3+6*4,29-6*3),
# 	(3+5*0,29-6*4),(3+6*1,29-6*4),(3+6*2,29-6*4),(3+6*3,29-6*4),(3+6*4,29-6*4)
# ]

def twenty_five_drones():
	ls = [
		(3+6*0,29-6*0),(3+6*1,29-6*0),(3+6*2,29-6*0),(3+6*3,29-6*0),(3+6*4,29-6*0),
		(3+5*0,29-6*1),(3+6*1,29-6*1),(3+6*2,29-6*1),(3+6*3,29-6*1),(3+6*4,29-6*1),
		(3+5*0,29-6*2),(3+6*1,29-6*2),(3+6*2,29-6*2),(3+6*3,29-6*2),(3+6*4,29-6*2),
		(3+5*0,29-6*3),(3+6*1,29-6*3),(3+6*2,29-6*3),(3+6*3,29-6*3),(3+6*4,29-6*3),
		(3+5*0,29-6*4),(3+6*1,29-6*4),(3+6*2,29-6*4),(3+6*3,29-6*4),(3+6*4,29-6*4)
	]

	while len(ls) > 1:
		i = ls.pop(0)
		libfarm.go_to(get_pos_x(),i[1])
		libfarm.go_to(i[0],i[1])
		def foo():
			while True:
				do_a_flip()
				do_a_flip()
				do_a_flip()
				do_a_flip()
				do_a_flip()
				spawn(6,i)
				solve_mapped(6,500)
				if num_items(Items.Gold) >= 9863168:
					return
		spawn_drone(foo)
	i = ls.pop()
	libfarm.go_to(i[0],i[1])
	spawn(6,i)
	solve_mapped(6,300)
	while num_items(Items.Gold) < 9863168:
		pass
	

def test_cell(cur_pos):
	can_go = []
	if can_move(North):
		can_go.append((cur_pos[0],cur_pos[1] + 1))
	if can_move(South):
		can_go.append((cur_pos[0],cur_pos[1] - 1))
	if can_move(East):
		can_go.append((cur_pos[0]+1,cur_pos[1]))
	if can_move(West):
		can_go.append((cur_pos[0]-1,cur_pos[1]))
	return can_go

	
def get_opposite(i):
	opps = {
		North : South,
		East : West,
		South : North,
		West : East
	}
	return opps[i]

def map_maze(map_of_maze,size,reps,prev_dir=None):
	cur_pos = (get_pos_x(),get_pos_y())
	if cur_pos in map_of_maze:
		return
	this_cell = test_cell(cur_pos)
	map_of_maze[cur_pos] = this_cell
	for i in this_cell:
		if i[1] > cur_pos[1]:
			dir = North
		elif i[1] < cur_pos[1]:
			dir = South
		elif i[0] > cur_pos[0]:
			dir = East
		else:
			dir = West
		opposite = get_opposite(dir)
		if prev_dir == None or prev_dir != opposite:
			move(dir)
			if get_entity_type() == Entities.Treasure:
				use_item(Items.Weird_Substance,size*(2**(num_unlocked(Unlocks.Mazes)-1)))
				reps[0] -= 1
			map_maze(map_of_maze,size,reps,dir)
			move(opposite)


	return map_of_maze

def solve_mapped(size,reps=0):
	map_of_maze = {}
	orig_reps = reps
	tmp = [reps]
	map_maze(map_of_maze,size,tmp)
	while reps >= 0:
		#uncomment below for single maze leaderboard
		# if num_items(Items.Gold) >= 9863168:
		# 	return
		target = measure()
		cur_pos = (get_pos_x(),get_pos_y())
		path = a_star(map_of_maze,cur_pos,target)
		while len(path) > 0:
			i = path.pop()
			move(i)
			if reps % 5 == 0: #just trial and error.
				cur_pos = (get_pos_x(),get_pos_y())
				cell = test_cell(cur_pos)
				map_of_maze[cur_pos] = cell
				
		reps -= 1
		if reps > 0:
			use_item(Items.Weird_Substance,size*(2**(num_unlocked(Unlocks.Mazes)-1)))
	harvest()
	return

def a_star(map,start,target):	
	# Open set as list of (f_score, coordinates)
	open_set = [(0, start)]
	
	# Tracking dictionaries
	came_from = {}
	g_score = {start: 0}
	f_score = {start: abs(start[0] - target[0]) + abs(start[1]-target[1])}
	
	while open_set:
		# Find node with lowest f_score
		min_idx = 0
		for i in range(len(open_set)):
			if open_set[i][0] < open_set[min_idx][0]:
				min_idx = i
		
		current_f, current = open_set.pop(min_idx)
		
		if current == target:
			# Reconstruct path as directions
			path = []
			while current in came_from:
				prev = came_from[current]
				dx = current[0] - prev[0]
				dy = current[1] - prev[1]
				if dy == 1:
					path.append(North)
				elif dy == -1:
					path.append(South)
				elif dx == 1:
					path.append(East)
				elif dx == -1:
					path.append(West)
				current = prev
			return path
		
		for neighbor in map[current]:
			tentative_g = g_score[current] + 1
			
			if neighbor not in g_score or tentative_g < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g
				f = tentative_g + abs(neighbor[0] - target[0]) + abs(neighbor[1]-target[1])
				f_score[neighbor] = f
				open_set.append((f, neighbor))
	
	return []

def bfs(map, start, target):
	queue = [start]
	visited = {start}
	came_from = {}
	
	while queue:
		current = queue.pop(0)
		
		if current == target:
			# Reconstruct path as directions
			path = []
			while current in came_from:
				prev = came_from[current]
				dx = current[0] - prev[0]
				dy = current[1] - prev[1]
				if dy == 1:
					path.append(North)
				elif dy == -1:
					path.append(South)
				elif dx == 1:
					path.append(East)
				elif dx == -1:
					path.append(West)
				current = prev
			
			return path
		
		for neighbor in map[current]:
			if neighbor not in visited:
				visited.add(neighbor)
				came_from[neighbor] = current
				queue.append(neighbor)
	
	return []