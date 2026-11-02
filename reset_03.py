import libfarm
import harvester
import maze
import snake

def part_3():
	mazes()
	megafarm()
	trees4()
	fertilizer4()
	pumpkins3()
	cactus2()
	dinosaur()
	get_power()
	play_snake()
	get_weird()
	finish_it()
	return

def mazes():
	while num_items(Items.Weird_Substance) < 2000:
		harvester.harvest_crop_para((0,7),(8,8),Entities.Carrot,False,True,False)
		if num_items(Items.Hay) < 10:
			clear()
			while num_items(Items.Hay) < 4000:
				harvester.harvest_crop_para((0,7),(8,8),Entities.Grass)
			clear()
	unlock(Unlocks.Mazes)
	libfarm.mark_time("Unlocked Mazes")

def megafarm():
	clear()
	maze.spawn(5,(2,2))
	maze.solve_mapped(5,301)

	unlock(Unlocks.Megafarm)
	libfarm.mark_time("Unlocked Megafarm")

def trees4():
	while num_items(Items.Hay) < 21000:
		harvester.harvest_crop_para((0,get_world_size()-1),(get_world_size(),get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Trees)
	libfarm.mark_time("Unlocked Trees 4")

def fertilizer4():
	while num_items(Items.Wood) < 56000:
		harvester.harvest_crop_para((0,get_world_size()-1),(get_world_size(),get_world_size()),Entities.Grass,True)

	unlock(Unlocks.Fertilizer)
	libfarm.mark_time("Unlocked Fertilizer 4")

def pumpkins3():
	clear()
	while num_items(Items.Carrot) < 30000:
		harvester.harvest_crop_para((0,get_world_size()-1),(get_world_size()/2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((get_world_size()/2,get_world_size()-1),(get_world_size()/2,get_world_size()),Entities.Grass,True)

	unlock(Unlocks.Pumpkins)
	libfarm.mark_time("Unlocked Pumpkins 3")

def cactus2():
	clear()
	def foo():
		x = get_pos_x()
		y = get_pos_y()
		while num_items(Items.Pumpkin) < 40000:
			harvester.harvest_pumpkins(x,y+5,6,True)

	libfarm.go_to(6,6)
	spawn_drone(foo)
	libfarm.go_home()
	foo()
	
	unlock(Unlocks.Cactus)
	libfarm.mark_time("Unlocked Cactus 2")

def get_power():
	while num_items(Items.Power) < 3000:
		harvester.harvest_sunflower(0,7,8)
	clear()

def dinosaur():
	clear()
	while num_items(Items.Cactus) < 680000:
		harvester.harvest_cactus(0,0, get_world_size())
	libfarm.go_to(11,11)
	harvest()

	unlock(Unlocks.Dinosaurs)
	unlock(Unlocks.Dinosaurs)
	unlock(Unlocks.Dinosaurs)
	unlock(Unlocks.Dinosaurs)
	unlock(Unlocks.Mazes)
	unlock(Unlocks.Mazes)
	libfarm.mark_time("Unlocked Dinosaurs 1-4, Mazes 3")

def play_snake():
	while num_items(Items.Bone) < 2000000:
		libfarm.go_home()
		snake.cheese()

	libfarm.mark_time("Have the bones")

def get_weird():
	while num_items(Items.Weird_Substance) < 210000:
		harvester.harvest_cactus(0,0,get_world_size(),True)

	libfarm.go_to(11,11)
	harvest()

def finish_it():
	libfarm.go_to(2,2)
	while num_items(Items.Gold) < 1000000:
		maze.spawn(5,(2,2))
		maze.solve_mapped(5,301)
	
	unlock(Unlocks.Leaderboard)

