from getting_information import get_params
from getting_field import get_field


def get_around_area(field, info, coords):
    R = info["radius"]
    a, b, list_of_X = coords[0], coords[1], []

    for x in range(a - R, a + R + 1):
        for y in range(b - R, b + R + 1):
            if has_no_wall(field, a, b, x, y) and (x, y) != (a, b):
                list_of_X.append((x, y))

    return list_of_X


def place_r(field, coords):
    field[coords[0]][coords[1]] = 'R'


def place_X(field, coords):
    field[coords[0]][coords[1]] = 'x'


def has_no_wall(field, a, b, x, y):
    for w in range(min(a, x), max(a, x) + 1):
        for v in range(min(b, y), max(b, y) + 1):
            if field[w][v] == "#":
                return False

    return True


def greedy_rs_placement(field, info):
    rows = info["rows"]
    cols = info["columns"]
    radius = info["radius"]
    r_dict = {}

    for line in range(rows):
        for symb in range(0, cols, 2):  # placement_optimization
            if field[line][symb] == '.':
                counter = 1

                while counter < radius and field[line][symb] == '.':
                    symb += 1

                symb -= 1
                coords = (line, symb)
                area = len(get_around_area(field, info, coords))
                r_dict[area] = coords

            if len(r_dict) == 2:
                router_coords = r_dict[max(r_dict)]
                for i in get_around_area(field, info, router_coords):
                    place_X(field, i)
                place_r(field, router_coords)
                r_dict = {}

    return field


def write_file(in_file, out_file, field):
    info = get_params(in_file)
    with open(out_file, "w", encoding='UTF-8', errors='ignore') as file:
        res = greedy_rs_placement(field, info)

        final_str = ""
        for i in res:
            final_str += " ".join(i) + "\n"

        file.write(final_str)


if __name__ == "__main__":
    file_name = 'lets_go_higher.in'
    out_name = 'lets_go_higher_res.txt'
    field = get_field(file_name)
    info = get_params(file_name)

    new_field = greedy_rs_placement(field, info)
    print('BUILT')
    write_file(out_name, new_field)
    print('DONE')