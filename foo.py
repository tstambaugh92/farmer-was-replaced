import libfarm
import harvester
import snake
import maze

clear()
set_world_size(3)
for j in range(3):
    for i in range(3):
        till()
        move(East)
    move(North)
    
while True:
	for j in range(3):
		for i in range(3):
			use_item(Items.Water)
			move(East)
		move(North)



