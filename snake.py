import libfarm


def snake():
	change_hat(Hats.Dinosaur_Hat)
	apple = measure()
	while True:
		libfarm.go_to_no_wrap(apple[0],apple[1])
		apple = measure()

def cheese():
	size = get_world_size()
	pos = [get_pos_x(),get_pos_y()]
	keep_going = True
	while keep_going:
		while pos[1] > 0 and keep_going:
			while pos[0] < size - 1 and keep_going:
				keep_going = move(East)
				pos[0] += 1
			keep_going = move(South)
			pos[1] -= 1
			if pos[1] == 0:
				break
			while pos[0] > 1 and keep_going:
				keep_going = move(West)
				pos[0] -= 1
			keep_going = move(South)
			pos[1] -= 1
		while pos[0] > 0 and keep_going:
			keep_going = move(West)
			pos[0] -= 1
		while pos[1] < size - 1 and keep_going:
			keep_going = move(North)
			pos[1] += 1
	clear()
	
def try_to_do_better_lol():
	size = get_world_size()
	size_mod = size - 1
	pos = libfarm.go_to_no_wrap(0,size - 1)
	change_hat(Hats.Dinosaur_Hat)
	goal = measure()
	score = 0
	keep_going = True
	while keep_going:
		if score > size_mod * 8: #size_mod * 8 got me avg 17:45 (67th spot, whoo)
			return cheese()
		pos = libfarm.go_to_no_wrap(goal[0],pos[1])
		pos = libfarm.go_to_no_wrap(pos[0],goal[1])
		goal = measure()
		score += 1
		length = (score / size_mod) // 1
		if pos[1] == size_mod:
			move(South)
			pos[1] -= 1
			if pos[0] == goal[0] and pos[1] == goal[1]:
				goal = measure()
				score += 1
				length = (score / size_mod) // 1
		while goal[1] > length + 3 and goal[0] > 0 and goal[1] < pos[1]:
			pos = libfarm.go_to_no_wrap(goal[0],pos[1])
			pos = libfarm.go_to_no_wrap(pos[0],goal[1])
			length = (score / size_mod) // 1
			goal = measure()
			score+=1
			length = (score / size_mod) // 1
			move(South)
			pos[1] -= 1
			if pos[0] == goal[0] and pos[1] == goal[1]:
				goal = measure()
				score += 1
				length = (score / size_mod) // 1
			if goal[1] == pos[1]:
				pass
			# keep_going = move(South)
			# pos[1] -= 1
			# if pos[0] == goal[0] and pos[1] == goal[1]:
			#     goal = measure()
			#     score += 1
			#break
		while pos[0] < size_mod:
			keep_going = move(East)
			pos[0] += 1
			if pos[0] == goal[0] and pos[1] == goal[1]:
				goal = measure()
				score += 1
				length = (score / size_mod) // 1
		length = (score / size_mod) // 1
		if length % 2 == 1:
			length += 1
		while pos[1] > length:
			keep_going = move(South)
			pos[1] -= 1
			if pos[0] == goal[0] and pos[1] == goal[1]:
				goal = measure()
				score += 1
		while length > 0:
			while pos[0] > 1:
				keep_going = move(West)
				pos[0] -= 1
				if goal[0] == pos[0] and pos[1] == goal[1]:
					goal = measure()
					score += 1
			keep_going = move(South)
			pos[1] -= 1
			if goal[0] == pos[0] and pos[1] == goal[1]:
					goal = measure()
					score += 1
			while pos[0] < size_mod:
				keep_going = move(East)
				pos[0] += 1
				if goal[0] == pos[0] and pos[1] == goal[1]:
					goal = measure()
					score += 1
			keep_going = move(South)
			pos[1] -= 1
			if goal[0] == pos[0] and pos[1] == goal[1]:
					goal = measure()
					score += 1
			length -= 2
		while pos[0] > 0:
			keep_going = move(West)
			pos[0] -= 1
			if goal[0] == pos[0] and pos[1] == goal[1]:
				goal = measure()
				score += 1
		while pos[1] < size_mod and pos[1] <= goal[1]:
			keep_going = move(North)
			pos[1] += 1
			if goal[0] == pos[0] and pos[1] == goal[1]:
				goal = measure()
				score += 1
			if not keep_going:
				#why the fuck is this even happening sometimes like 1 in 4 runs
				keep_going = True
				pos = [0,size_mod]
				break
	while True:
		pass