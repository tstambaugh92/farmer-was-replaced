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

def solve_maze_leaderboard():
	# 25 6x6 mazes
	# ls = [
	# 	(3+6*0,29-6*0),(3+6*1,29-6*0),(3+6*2,29-6*0),(3+6*3,29-6*0),(3+6*4,29-6*0),
	# 	(3+5*0,29-6*1),(3+6*1,29-6*1),(3+6*2,29-6*1),(3+6*3,29-6*1),(3+6*4,29-6*1),
	# 	(3+5*0,29-6*2),(3+6*1,29-6*2),(3+6*2,29-6*2),(3+6*3,29-6*2),(3+6*4,29-6*2),
	# 	(3+5*0,29-6*3),(3+6*1,29-6*3),(3+6*2,29-6*3),(3+6*3,29-6*3),(3+6*4,29-6*3),
	# 	(3+5*0,29-6*4),(3+6*1,29-6*4),(3+6*2,29-6*4),(3+6*3,29-6*4),(24,7) #(3+6*4,29-6*4)
	# ]

	#no real luck with 16 8x8
	# ls = [
	# 	(4,28),(4+8,28),(4+16,28),(4+24,28),
	# 	(4+24,20),(4+16,20),(4+8,20),(4,20),
	# 	(4,12),(12,12),(20,12),(28,12),
	# 	(28,4),(20,4),(12,4),(4,4)
	# ]

	#24 6x6 mazes with one 8x8 in the corner
	# ls = [
	# 	[(3+6*0,29-6*0),(3+6*1,29-6*0),(3+6*2,29-6*0),(3+6*3,29-6*0),(3+6*4,29-6*0)],
	# 	[(3+5*0,29-6*1),(3+6*1,29-6*1),(3+6*2,29-6*1),(3+6*3,29-6*1),(3+6*4,29-6*1)],
	# 	[(3+5*0,29-6*2),(3+6*1,29-6*2),(3+6*2,29-6*2),(3+6*3,29-6*2),(3+6*4,29-6*2)],
	# 	[(3+5*0,29-6*3),(3+6*1,29-6*3),(3+6*2,29-6*3),(3+6*3,29-6*3),(3+6*4,29-6*3)],
	# 	[(3+5*0,29-6*4),(3+6*1,29-6*4),(3+6*2,29-6*4),(3+6*3,29-6*4),(31,0)] 
	# ]

	#second drones for the aboxe 24 6x6 + 8x8
	# ls2 = [
	# 	(5,13),(11,13),(17,13),
	# 	(5,7),(11,7),(17,7),
	# 	(24,7)
	# ]

	#winning combo seems to be 25 5x5 mazes
	ls = [
		[( 2,29),( 7,29),(12,29),(17,29),(22,29)],
		[( 2,24),( 7,24),(12,24),(17,24),(22,24)],
		[( 2,19),( 7,19),(12,19),(17,19),(22,19)],
		[( 2,14),( 7,14),(12,14),(17,14),(22,14)],
		[( 2, 9),( 7, 9),(12, 9),(17, 9),(22, 9)]
	]

	#plus fill in the gaps with 8x8s
	ls2 = [
		(3,3),(10,3),(17,3),(24,3),(28,28),(28,21),(28,14)
	]

	#the bar functions spawn the 7x7 mazes
	def bar():
		def bar2():
			first = True
			while True:
				# while get_entity_type() != Entities.Hedge:
				# 	if num_items(Items.Gold) >= 9863168:
				# 		return
				if first:
					do_a_flip()
					first = False
				spawn(7,j)
				solve_mapped(7,500,bfs)
				if num_items(Items.Gold) >= 9863168:
					return
		while len(ls2) > 1:
			j = ls2.pop(0)
			libfarm.go_to(j[0],j[1])
			spawn_drone(bar2)
		j = ls2.pop()
		libfarm.go_to_no_wrap(j[0],j[1])
		bar2()

	spawn_drone(bar)
	libfarm.go_to(ls[0][0][0],ls[0][0][1])
	while len(ls) > 1:
		i = None
		row = ls.pop(0)
		libfarm.go_to_no_wrap(row[0][0],row[0][1])
		def spawn_job():
			def foo():
				first = True
				while True:
					if first:
						do_a_flip()
						first = False
					spawn(5,i)
					solve_mapped(5,500)
					if num_items(Items.Gold) >= 9863168:
						return
			while len(row) > 1:
				i = row.pop(0)
				libfarm.go_to_no_wrap(i[0],i[1])
				spawn_drone(foo)
			i = row.pop()
			libfarm.go_to_no_wrap(i[0],i[1])
			foo()
		spawn_drone(spawn_job)
	row = ls.pop()

	#these functions are identical to above, but are needed for the last row
	#scope is a bitch. 
	def foo2():
		first = True
		while True:
			if first:
				do_a_flip()
				#do_a_flip()
				first = False
			spawn(5,i)
			solve_mapped(5,500)
			if num_items(Items.Gold) >= 9863168:
				return
	def foo3():
		while True:			
			spawn(5,i)
			solve_mapped(5,500)
			if num_items(Items.Gold) >= 9863168:
				return
	while len(row) > 1:
			i = row.pop(0)
			libfarm.go_to_no_wrap(i[0],i[1])
			spawn_drone(foo2)
	i = row.pop()
	libfarm.go_to_no_wrap(i[0],i[1])
	foo3()

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

OPPOSITES = {
	North : South,
	East : West,
	South : North,
	West : East
}

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
		opposite = OPPOSITES[dir] #get_opposite(dir)
		if prev_dir == None or prev_dir != opposite:
			move(dir)
			ent = get_entity_type()
			if ent == Entities.Treasure:
				use_item(Items.Weird_Substance,size*(2**(num_unlocked(Unlocks.Mazes)-1)))
				reps[0] -= 1
			map_maze(map_of_maze,size,reps,dir)
			move(opposite)


	return map_of_maze

def solve_mapped(size,reps=0,func=bfs):
	map_of_maze = {}
	orig_reps = reps
	tmp = [reps]
	map_maze(map_of_maze,size,tmp)
	while reps >= 0:
		#uncomment below for single maze leaderboard
		if num_items(Items.Gold) >= 9863168:
			return
		target = measure()
		cur_pos = (get_pos_x(),get_pos_y())
		if get_entity_type() not in [Entities.Hedge,Entities.Treasure]:
			return
		path = func(map_of_maze,cur_pos,target)
		while len(path) > 0:
			i = path.pop()
			move(i)
			#occasionally remap while you walk to find new paths
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
	# g score is the actual distance traveled to a given node
	# f score is the distance plus the manhatten distance from the target
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

def dfs(map, start, target):
	stack = [start]
	visited = {start}
	came_from = {}
	
	while stack:
		current = stack.pop()
		
		if current == target:
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
				stack.append(neighbor)
	
	return []