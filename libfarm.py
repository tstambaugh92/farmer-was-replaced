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

def go_to_no_wrap(x,y):
	cur_x = get_pos_x()
	cur_y = get_pos_y()

	NS = North
	EW = East
	if cur_x > x:
		EW = West
	if cur_y > y:
		NS = South
	
	while cur_x != x:
		move(EW)
		if EW == West:
			cur_x -= 1
		else:
			cur_x += 1
	
	while cur_y != y:
		move(NS)
		if NS == North:
			cur_y += 1
		else:
			cur_y -= 1
	return [cur_x,cur_y]
	
#bubble sort lol
def sunflower_sort(tuple_list):
	l = len(tuple_list)
	for i in range(l-1):
		for j in range(l -1 - i):
			if tuple_list[j][2] < tuple_list[j+1][2]:
				tmp = tuple_list[j]
				tuple_list[j] = tuple_list[j+1]
				tuple_list[j+1] = tmp
				
#this is slow as shit because of inserts and pops
#I don't think I even did it right.
#Even if I redid it correctly, I don't think it
#would be faster than shoving them in buckets
def sun_qsort(tuple_list,a,z):
	if a == z:
		return
	pivot = tuple_list[a][2]
	pivot_index = a
	for i in range(a+1,z+1):
		if tuple_list[i][2] >= pivot:
			tmp = tuple_list[i]
			tuple_list.pop(i)
			tuple_list.insert(pivot_index,tmp)
			pivot_index+=1
	if pivot_index > a:
		sun_qsort(tuple_list,a,pivot_index-1)
	if pivot_index < z:
		sun_qsort(tuple_list,pivot_index+1,z)

#actual quick sort not done shit
#its faster than the bubble sort, but
#the coordinates are all fucked, so the
#travel time makes it worse than putting them
#in buckets left to right.
def sun_qsort2(tuple_list,a,z):
	if a == z:
		return
	pivot = tuple_list[a][2]
	left_ptr = a+1
	right_ptr = z
	while left_ptr < right_ptr:
		while tuple_list[left_ptr][2] >= pivot:
			left_ptr += 1
			if left_ptr == right_ptr:
				break
		while tuple_list[right_ptr][2] < pivot:
			right_ptr -= 1
			if left_ptr == right_ptr:
				break
		if left_ptr < right_ptr:
			tmp = tuple_list[right_ptr]
			tuple_list[right_ptr] = tuple_list[left_ptr]
			tuple_list[left_ptr] = tmp
		elif left_ptr == right_ptr:
			left_ptr -= 1
			tmp = tuple_list[left_ptr]
			tuple_list[left_ptr] = tuple_list[a]
			tuple_list[a] = tmp
			break
	if left_ptr > a:
		sun_qsort2(tuple_list,a,left_ptr - 1)
	if right_ptr < z:
		sun_qsort2(tuple_list,right_ptr,z)

#this returns a new list of the passed flowers
#sorted into buckets, so 15 petals first, down to 7.
#the order they're returned in is also sorted to
#optimize travel while harvesting
def sun_buckets(tuple_list):
	list = []
	for i in range(0,16):
		list.append([])
	for flower in tuple_list:
		list[flower[2]].append(flower)
	new_list = []
	x = get_pos_x()
	y = get_pos_y()
	for i in range(15,6,-1):
		new_bucket = sort_bucket(list[i],x,y)
		if len(new_bucket) > 0:
			x = new_bucket[-1][0]
			y = new_bucket[-1][1]
		new_list = new_list + new_bucket
	return new_list
	
#returns list sorted in such a way that
#each X,Y cordinate is the closest to the 
#previous. The x,y passed in is the starting position.
def sort_bucket(list,x,y):
	new_bucket = []
	while len(list) > 0:
		best = None
		best_index = 0
		i = 0
		for item in list:
			dist = man_dist(item,(x,y))
			if best == None or dist < best:
				best = dist
				best_index = i
			i+=1
		new_bucket.append(list.pop(best_index))
		x = new_bucket[-1][0]
		y = new_bucket[-1][1]
	return new_bucket
		
def man_dist(a,b):
	return abs(a[0]-b[0])+abs(a[1]-b[1]) 

def go_swap(xy,dir):
	go_to(xy[0],xy[1])
	swap(dir)

def cactus_sort(crop_map,origin):
	rows, cols = len(crop_map), len(crop_map[0])
	
	# Primary loop: start at (0,n) and work down each column
	for start_row in range(rows):
		for start_col in range(7, -1, -1):	#7 -> cols - 1
			
			# Keep working on this starting position until no swaps occur
			while True:
				total_swaps_this_iteration = 0
				current_row, current_col = start_row, start_col
				
				# Phase 1: Move down/left, swapping with greater value
				while True:
					swapped = False
					
					# Check left and down neighbors
					if current_col > 0:
						left_val = crop_map[current_row][current_col - 1]
					else:
						left_val = None
					if current_row < rows - 1: # rows - 1
						down_val = crop_map[current_row + 1][current_col]
					else:
						down_val = None

					
					swap_left = left_val != None and left_val > crop_map[current_row][current_col]
					swap_down = down_val != None and down_val > crop_map[current_row][current_col]
					
					if swap_left and swap_down:
						# Pick the greater of the two
						if left_val >= down_val:
							swap_down = False
						else:
							swap_left = False
					
					if swap_left:
						# Swap left
						crop_map[current_row][current_col], crop_map[current_row][current_col - 1] = crop_map[current_row][current_col - 1], crop_map[current_row][current_col]
						go_swap((origin[0]+current_col,origin[1]-current_row),West)
						current_col -= 1
						total_swaps_this_iteration += 1
						swapped = True
					elif swap_down:
						# Swap down
						crop_map[current_row][current_col], crop_map[current_row + 1][current_col] = crop_map[current_row + 1][current_col], crop_map[current_row][current_col]
						go_swap((origin[0]+current_col,origin[1]-current_row),South)
						current_row += 1
						total_swaps_this_iteration += 1
						swapped = True
					
					if not swapped:
						break
				
				# Phase 2: Move up/right from the current position
				while True:
					swapped = False
					
					# Check right and up neighbors
					if current_col < cols - 1: #cols - 1
						right_val = crop_map[current_row][current_col + 1]
					else:
						right_val = None
					if current_row > 0:
						up_val = crop_map[current_row - 1][current_col]
					else:
						up_val = None
					
					# Find which neighbor to swap with (the lesser one)
					swap_right = right_val != None and right_val < crop_map[current_row][current_col]
					swap_up = up_val != None and up_val < crop_map[current_row][current_col]
					
					if swap_right and swap_up:
						# Pick the lesser of the two
						if right_val <= up_val:
							# Swap right
							swap_up = False
						else:
							# Swap up
							swap_right = False
					
					if swap_right:
						# Swap right
						crop_map[current_row][current_col], crop_map[current_row][current_col + 1] = crop_map[current_row][current_col + 1], crop_map[current_row][current_col]
						go_swap((origin[0]+current_col,origin[1]-current_row),East)
						current_col += 1
						total_swaps_this_iteration += 1
						swapped = True
					elif swap_up:
						# Swap up
						crop_map[current_row][current_col], crop_map[current_row - 1][current_col] = crop_map[current_row - 1][current_col], crop_map[current_row][current_col]
						go_swap((origin[0]+current_col,origin[1]-current_row),North)
						current_row -= 1
						total_swaps_this_iteration += 1
						swapped = True
					
					if not swapped:
						break
				
				# If no swaps occurred in this complete iteration, move to next starting position
				if total_swaps_this_iteration == 0:
					break
