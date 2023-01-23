#https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/


def get_line_equation(point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    if (x2 - x1) == 0:
        m = float('inf')
    else:
        m = (y2-y1)/(x2-x1) #slope
    c = y1 - (m*x1) # intersect

    return m,c

def point_is_left_of_line(point,line):
    point_x,point_y = point
    vert1,vert2 = line
    vert1x,vert1y = vert1 
    vert2x,vert2y = vert2 
    y_between_points = (point_y - vert1y)*(point_y - vert2y) <= 0
    if not y_between_points:
        return False
    slope,intersect = get_line_equation(vert1, vert2) # m,c
    # y= mx + c, so at the same y as point, on the line x = (point_y - intersect)/slope
    x_on_line = (point_y - intersect)/slope
    if x_on_line >= point_x:
        return True
    return False


def is_point_in_shape(point,shape):
    point_left_of = 0
    for idx in range(len(shape)):
        vert1, vert2 = shape[idx-1],shape[idx]
        if point_is_left_of_line(point, (vert1,vert2)):
            point_left_of+=1
    return point_left_of%2==1



def main():
    point = [2,2]
    shape = [[1,0],[3,9],[5,1]]
    if is_point_in_shape(point, shape):
        print('point is inside shape')
    else:
        print('point is outside shape')


if __name__ == '__main__':
    main()