def get_params(file_name):
    with open(file_name, "r") as file:
        readed = file.read().split("\n")
        field = [int(j) for i in readed[:3] for j in i.split()]

    info_dict = {"rows": field[0],
                 "columns": field[1],
                 "radius": field[2],
                 "b_price": field[3],
                 "r_price": field[4],
                 "budget": field[5],
                 "b_coordinates": [field[6], field[7]]}

    return info_dict
