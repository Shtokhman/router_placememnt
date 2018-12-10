from getting_information import get_params
from getting_field import get_field
import numpy
import copy


def get_around_area(field, needed_info):
    rows, cols, R = needed_info[0], needed_info[1], needed_info[2]
    a, b, list_of_X = needed_info[3][0], needed_info[3][1], []

    for x in range(rows+1):
        for y in range(cols+1):
            if abs(a-x) <= R and abs(b-y) <= R and \
                    has_no_wall(field, a, b, x, y) and (x, y) != (a, b):
                field[x][y] = "X"
                list_of_X.append((x, y))

    field[a][b] = "r"

    return (a, b), list_of_X


def has_no_wall(field, a, b, x, y):
    for w in range(min(a, x), max(a, x) + 1):
        for v in range(min(b, y), max(b, y) + 1):
            if field[w][v] == "#":
                return False

    return True


def all_rs_possible(field, info):
    needed_info = [info["rows"], info["columns"], info["radius"], ()]
    r_dictionary = dict()

    for line in range(info["rows"]):
        for symb in range(info["columns"]):
            if field[line][symb] != "#" and field[line][symb] != "-":
                needed_info[3] = (line, symb)
                key, value = get_around_area(field, needed_info)
                r_dictionary[key] = value

    return sorted(r_dictionary.items(), key=lambda kv: len(kv[1]), reverse=True)


def only_needed_rs(field, info_dict):
    all_points_dict, final_list_of_rs = all_rs_possible(field, info_dict), []

    for i in range(len(all_points_dict)):
        for j in range(len(all_points_dict)):
            if len(all_points_dict[i][1]) > len(all_points_dict[j][1]) and \
               bool(set(all_points_dict[i][1]) & set(all_points_dict[j][1])):
                all_points_dict[j] = ((0, 0), [])

    for i in all_points_dict:
        if i != ((0, 0), []):
            final_list_of_rs.append(i)

    return final_list_of_rs


def filling_new_field(new_field, coords_list):
    for i in coords_list:
        r_coord1, r_coord2 = i[0][0], i[0][1]
        new_field[r_coord1][r_coord2] = "R"
        for coords in i[1]:
            new_field[coords[0]][coords[1]] = "x"

    return numpy.array(new_field)


def write_file(file_name, write_in_file):
    field = get_field(file_name)
    new_field = copy.deepcopy(field)
    info_dict = get_params(file_name)

    with open(write_in_file, "w") as file:
        res = filling_new_field(new_field, only_needed_rs(field, info_dict))

        final_str = ""
        for i in res:
            final_str += " ".join(i) + "\n"

        file.write(final_str)


if __name__ == "__main__":
    given_files = "charleston_road.in"
    output_files = "charleston_res.txt"

    for i in range(len(given_files)):
        write_file(given_files[i], output_files[i])
