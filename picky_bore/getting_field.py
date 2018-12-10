def get_field(file_name):
    with open(file_name, "r") as file:
        readed = file.read().split("\n")
        field = [list(i) for i in readed[3:]]

    return field
