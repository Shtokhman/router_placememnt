from math import hypot
from getting_information import get_params


def open_field(input_file):
    with open(input_file, "r") as file:
        readed = file.read().split("\n")
        field = [list(i) for i in readed]

    return [[j for j in i if j != " "] for i in field]


def distance(p, q):

    return int(hypot(p[0] - q[0], p[1] - q[1]) - 1)


def number_of_xr(field):
    x_counter, r_counter = 0, 0

    for line in field:
        for j in line:
            if j == "x":
                x_counter += 1
            if j == "R":
                r_counter += 1

    return r_counter, x_counter


def place_backbone(field, coordinates):
    field[coordinates[0]] = field[coordinates[0]][:coordinates[1]] + 'b' + \
        field[coordinates[0]][coordinates[1]+1:]


def number_of_backbones(field, info):
    b_coords = info["b_coordinates"]
    routers_coords = []
    b_cells = 1

    for i in range(info["rows"]):
        for j in range(info["columns"]):
            if field[i][j] == "R":
                routers_coords.append((i, j))

    for coords in routers_coords:
        b_cells += distance(b_coords, coords)

    return b_cells


if __name__ == "__main__":
    source_file = "charleston_road.in"
    field_file = "charleston_res.txt"
    field_file = open_field(field_file)
    print(number_of_backbones(field_file,
                              get_params(source_file)))
    print(number_of_xr(field_file))
