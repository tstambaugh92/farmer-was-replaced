import harvester
import libfarm
import reset_03

def part_2():
	water2()
	fertilizer()
	fertilizer2()
	grass2()
	carrots2()
	speed4()
	carrots3()
	speed5()
	trees2()
	grass3()
	fertilizer3()
	water3()
	grass4()
	trees3()
	water4()
	sunflowers()
	get_power()
	water5()
	trees4()
	carrots4()
	grass5()
	gather_wood_carrots()
	unlock(Unlocks.Pumpkins)
	unlock(Unlocks.Pumpkins)
	expand5()
	unlock(Unlocks.Cactus)
	unlock(Unlocks.Expand)

	reset_03.part_3()

def water2():
	while num_items(Items.Wood) < 220:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)

	unlock(Unlocks.Watering)
	libfarm.mark_time("Unlocked Water 2")

def fertilizer():
	while num_items(Items.Wood) < 600:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)

	unlock(Unlocks.Fertilizer)
	libfarm.mark_time("Unlocked Fertilizer")

def fertilizer2():
	while num_items(Items.Wood) < 1600:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)

	unlock(Unlocks.Fertilizer)
	libfarm.mark_time("Unlocked Fertilizer 2")

def fertilizer3():
	while num_items(Items.Wood) < 9100:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)

	unlock(Unlocks.Fertilizer)
	libfarm.mark_time("Unlocked Fertilizer 3")

def grass2():
	while num_items(Items.Hay) < 320:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Grass)
	libfarm.mark_time("Unlocked Grass 2")

def carrots2():
	while num_items(Items.Wood) < 270:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Carrots)
	libfarm.mark_time("Unlocked Carrots 2")

def speed4():
	while num_items(Items.Carrot) < 520:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Speed)
	libfarm.mark_time("Unlocked Speed 4")

def carrots3():
	while num_items(Items.Wood) < 1300:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Carrots)
	libfarm.mark_time("Unlocked Carrots 3")

def speed5():
	while num_items(Items.Carrot) < 1000:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Speed)
	libfarm.mark_time("Unlocked Speed 5")

def trees2():
	while num_items(Items.Hay) < 330:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),((get_world_size()-2)/2,get_world_size()),Entities.Grass,False)
		harvester.harvest_crop_para((4,get_world_size()-1),((get_world_size()-2)/2,get_world_size()),Entities.Grass,True)

	unlock(Unlocks.Trees)
	libfarm.mark_time("Unlocked Trees 2")

def grass3():
	while num_items(Items.Wood) < 530:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Grass)
	libfarm.mark_time("Unlocked Grass 3")

def water3():
	while num_items(Items.Wood) < 830:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Watering)
	libfarm.mark_time("Unlocked Water 3")

def grass4():
	while num_items(Items.Wood) < 2600:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Grass)
	libfarm.mark_time("Unlocked Grass 4")

def trees3():
	while num_items(Items.Hay) < 1300:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),((get_world_size()-2)/2,get_world_size()),Entities.Grass,False)
		harvester.harvest_crop_para((4,get_world_size()-1),((get_world_size()-2)/2,get_world_size()),Entities.Grass,True)

	unlock(Unlocks.Trees)
	libfarm.mark_time("Unlocked Trees 3")

def water4():
	while num_items(Items.Wood) < 3300:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Watering)
	libfarm.mark_time("Unlocked Water 4")

def sunflowers():
	while num_items(Items.Carrot) < 600:
		harvester.harvest_crop_para((0,get_world_size()-1),(2,get_world_size()),Entities.Carrot)
		harvester.harvest_crop_para((2,get_world_size()-1),(get_world_size()-2,get_world_size()),Entities.Grass,True)
	
	unlock(Unlocks.Sunflowers)
	libfarm.mark_time("Unlocked Sunflowers")

def get_power():
	clear()
	while num_items(Items.Power) < 2500:
		harvester.harvest_sunflower(0,get_world_size()-1,get_world_size())
		
def water5():
	clear()
	while num_items(Items.Wood) < 13000:
		harvester.harvest_crop_para((0,5),(6,6),Entities.Grass,True)
	
	unlock(Unlocks.Watering)
	libfarm.mark_time("Unlocked Water 5")

def trees4():
	while num_items(Items.Hay) < 5000:
		harvester.harvest_crop_para((0,5),(6,6),Entities.Grass,True)
	
	unlock(Unlocks.Trees)
	libfarm.mark_time("Unlocked Trees 4")

def carrots4():
	while num_items(Items.Wood) < 7000:
		harvester.harvest_crop_para((0,5),(6,6),Entities.Grass,True)

	unlock(Unlocks.Carrots)
	libfarm.mark_time("Unlocked Carrots 4")

def grass5():
	while num_items(Items.Wood) < 13000:
		harvester.harvest_crop_para((0,5),(2,6),Entities.Carrot)
		harvester.harvest_crop_para((2,5),(4,6),Entities.Grass,True)

	unlock(Unlocks.Grass)
	libfarm.mark_time("Unlocked Grass 5")

def gather_wood_carrots():
	while num_items(Items.Wood) < 10000 or num_items(Items.Carrot) < 10000:
		harvester.harvest_crop_para((0,5),(3,6),Entities.Carrot)
		harvester.harvest_crop_para((3,5),(3,6),Entities.Grass,True)

def expand5():
	clear()
	while num_items(Items.Pumpkin) < 15000:
		harvester.harvest_pumpkins(0,5,6,True)

	unlock(Unlocks.Expand)
	libfarm.mark_time("Unlocked Expand 5")