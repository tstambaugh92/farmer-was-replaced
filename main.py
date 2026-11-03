import libfarm2
import harvester

def main():
    set_world_size(16)
    libfarm2.go_home()
    libfarm2.center()
    harvester.harvest_coal()

clear()
main()
while True:
    pass