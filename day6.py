import fileinput
import operator
from collections import defaultdict
def day6part1():
    coord_list = make_coord_list()
    border_coords = check_border()
    distances = defaultdict(lambda: 0)
    max_x, max_y = get_max_points(coord_list)
    min_x, min_y = get_min_points(coord_list)

    print(min_x, max_x, min_y, max_y)

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            temp_dict = defaultdict(lambda: 0)

            for coord_index in range(len(coord_list)):

                x_coord = coord_list[coord_index][0]
                y_coord = coord_list[coord_index][1]

                dist_points = abs(i - x_coord) + abs(j - y_coord)

                temp_dict[tuple(coord_list[coord_index])] = dist_points

            minval = min(temp_dict.values())

            min_keys = [k for k, v in temp_dict.items() if v == minval]


            if len(min_keys) == 1:
                distances[tuple(min_keys)] += 1
    for key in list(distances.keys()):
        if key[0] in border_coords:
            del distances[key]
    print(distances)
    return max(distances.values())

def day6part2():
    coord_list = make_coord_list()
    max_x, max_y = get_max_points(coord_list)
    min_x, min_y = get_min_points(coord_list)
    count = 0

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            temp_dist = 0
            for coord_index in range(len(coord_list)):
                x_coord = coord_list[coord_index][0]
                y_coord = coord_list[coord_index][1]

                dist_points = abs(i - x_coord) + abs(j - y_coord)

                temp_dist += dist_points

            if temp_dist < 10000:
                count += 1

    return count








def check_border():
    coord_list = make_coord_list()
    border_points = []
    max_x, max_y = get_max_points(coord_list)
    min_x, min_y = get_min_points(coord_list)


    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            temp_dict = defaultdict(lambda: int)
            #0, 5
            if (i != min_x and i != max_x) and (j != min_y and j != max_y):
                continue

            for coord_index in range(len(coord_list)):
                x_coord = coord_list[coord_index][0]
                y_coord = coord_list[coord_index][1]
                dist_points = abs(i - x_coord) + abs(j - y_coord)
                temp_dict[tuple(coord_list[coord_index])] = dist_points
            border_points.append(min(temp_dict.items(), key=operator.itemgetter(1))[0])


    return list(set(border_points))

def get_min_points(list):
    list_0 = []
    list_1 = []
    for i in range(len(list)):
        list_0 += [list[i][0]]
        list_1 += [list[i][1]]

    return min(list_0), min(list_1)


def get_max_points(list):
    list_0 = []
    list_1 = []
    for i in range(len(list)):
        list_0 += [list[i][0]]
        list_1 += [list[i][1]]

    return max(list_0), max(list_1)


def make_coord_list():
    coords = []
    for line in fileinput.input("day6input.txt"):
        coords.append(str(line).rstrip("\n").split(','))

    for i in range(len(coords)):
        coords[i][0] = int(coords[i][0])
        coords[i][1] = int(coords[i][1])

    return coords

#print(make_coord_list())
print(day6part2())
#print(check_border())
