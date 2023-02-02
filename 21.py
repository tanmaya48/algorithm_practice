'''The Towers of Hanoi'''

def move(towers,source_tower,target_tower):
    towers[target_tower].append(towers[source_tower].pop(-1))
    print(f'{source_tower} > {target_tower}')



def create_towers(n_disks = 3):
    towers= {
        'A':[ n_disks-i for i in range(n_disks) ],
        'B':[],
        'C':[]
        }
    return towers



def step_towers_of_hanoi(towers,disk_to_move, source_tower, auxilary_tower, target_tower):
    if len(towers[source_tower]) == 0:
        return
    if disk_to_move == towers[source_tower][-1]:
        move(towers, source_tower, target_tower)
        return
    
    disk_height = towers[source_tower].index(disk_to_move)

    above_disk = towers[source_tower][disk_height+1]

    step_towers_of_hanoi(towers, 
                        disk_to_move=above_disk, 
                        source_tower=source_tower, 
                        auxilary_tower=target_tower,
                        target_tower=auxilary_tower)

    
    
    move(towers, source_tower, target_tower)


    step_towers_of_hanoi(towers, 
                        disk_to_move=above_disk, 
                        source_tower=auxilary_tower, 
                        auxilary_tower=source_tower,
                        target_tower=target_tower)




def towers_of_hanoi(n_disks = 3):
    towers = create_towers(n_disks=n_disks)

    step_towers_of_hanoi(towers, towers['A'][0], 'A', 'B', 'C')


def main():
    towers_of_hanoi(n_disks=5)


if __name__ == '__main__':
    main()