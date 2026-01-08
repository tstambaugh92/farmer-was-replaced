import harvester
import libfarm
import reset_02

#First Speed Upgrade
i = 0
while i < 20:
	if can_harvest():
		harvest()
		i += 1

unlock(Unlocks.Speed)
libfarm.mark_time("Unlocked Speed 1")
i = 0

#First expansion
while i < 30:
	if can_harvest():
		harvest()
		i += 1

unlock(Unlocks.Expand)
libfarm.mark_time("Unlocked Expand 1")

#Shrubs
i = 0
while i < 50:
	if can_harvest():
		harvest()
		i += 1
	#move(North)

unlock(Unlocks.Plant)
libfarm.mark_time("Unlocked Plant")

#Speed 2
wood = 0
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
while wood < 20:
	if can_harvest():
		harvest()
		wood += 1
		plant(Entities.Bush)
	move(North)

unlock(Unlocks.Speed)
libfarm.mark_time("Unlocked Speed 2")
wood = 0

#Expand 2
while wood < 20:
	if can_harvest():
		harvest()
		wood += 1
		plant(Entities.Bush)
	move(North)

unlock(Unlocks.Expand)
libfarm.mark_time("Unlocked Expand 2")


#carrots
libfarm.go_home()
for j in range(2):
	for i in range(3):
		plant(Entities.Bush)
		move(North)
	move(East)
while num_items(Items.Wood) < 53:
	if can_harvest():
		crop = get_entity_type()
		harvest()
		plant(crop)
	move(North)
	if get_pos_y() == 0:
		move(East)


unlock(Unlocks.Carrots)
libfarm.mark_time("Unlocked Carrots")

#speed 3
libfarm.go_home()
for i in range(3):
	harvest()
	till()
	plant(Entities.Carrot)
	move(North)

while num_items(Items.Wood) < 53 or num_items(Items.Carrot) < 50:
	if can_harvest():
		crop = get_entity_type()
		harvest()
		plant(crop)
	move(North)
	if get_pos_y() == 0:
		move(East)

unlock(Unlocks.Speed)
libfarm.mark_time("Unlocked Speed 3")

#Expand 3
while num_items(Items.Wood) < 46 or num_items(Items.Carrot) < 20:
	if can_harvest():
		crop = get_entity_type()
		harvest()
		plant(crop)
	move(North)
	if get_pos_y() == 0:
		move(East)

unlock(Unlocks.Expand)
libfarm.mark_time("Unlocked Expand 4")

#Trees
libfarm.go_home()
for j in range(4):
	till()
	plant(Entities.Carrot)
	move(North)
move(East)

for j in range(2):
	for i in range(4):
		plant(Entities.Bush)
		move(North)
	move(East)

move(East)
while num_items(Items.Wood) < 58 or num_items(Items.Carrot) < 70:
	if can_harvest():
		crop = get_entity_type()
		harvest()
		plant(crop)
	if get_ground_type() == Grounds.Soil:
		plant(Entities.Carrot)
	move(North)
	if get_pos_y() == 0:
		move(East)

unlock(Unlocks.Trees)
libfarm.mark_time("Unlocked Trees")

#water
while num_items(Items.Wood) < 58:
	harvester.harvest_crop_para((0,3),(2,4),Entities.Carrot)
	harvester.harvest_crop_para((2,3),(2,4),Entities.Grass,True)

unlock(Unlocks.Watering)
libfarm.mark_time("Unlocked Watering")

#expand 4
while num_items(Items.Wood) < 108 or num_items(Items.Carrot) < 50:
	harvester.harvest_crop_para((0,3),(2,4),Entities.Carrot)
	harvester.harvest_crop_para((2,3),(2,4),Entities.Grass,True)

unlock(Unlocks.Expand)
libfarm.mark_time("Unlocked Expand 4")

reset_02.part_2()