#https://www.geeksforgeeks.org/box-stacking-problem-dp-22/

# Pattern H,W,D


def boxes_fitting_base(boxes,base):
    fitting_boxes = []
    height,width,depth = base
    for box in boxes:
        if (box[1] < width) and (box[2] < depth):
            fitting_boxes.append(box)
    return fitting_boxes


def get_tallest_tower(all_boxes):
    if len(all_boxes) == 0:
        return 0
    if len(all_boxes) == 1:
        height_of_box = all_boxes[0][0]
        return height_of_box
    
    tallest_tower_height = 0
    for base in all_boxes:
        remaining_boxes = all_boxes.copy()
        remaining_boxes.remove(base)
        base_height = base[0]
        tower_height = base_height + get_tallest_tower(boxes_fitting_base(remaining_boxes,base))
        if tower_height > tallest_tower_height:
            tallest_tower_height = tower_height
    
    return tallest_tower_height



def box_stacking(box_sizes):
    all_boxes = []
    for box_size in box_sizes:
        height,width,depth = box_size
        rotations = [[height,width,depth],[depth,height,width],[width,depth,height]]
        for rotation in rotations:
            if rotation not in all_boxes:
                all_boxes.append(rotation)
    
    tallest_tower_height = get_tallest_tower(all_boxes)
    return tallest_tower_height



def main():
    box_sizes = [ [4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
    tallest_tower_height = box_stacking(box_sizes)
    print(tallest_tower_height)


if __name__ == '__main__':
    main()
