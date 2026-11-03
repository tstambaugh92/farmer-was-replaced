import libfarm2 as libfarm2
import harvester as harvester

def main():
    set_world_size(9)
    libfarm2.go_home()
    libfarm2.center()

main()
while True:
    do_a_flip()