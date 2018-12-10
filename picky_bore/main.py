import backbone_counter
import getting_information


def main():
    field = backbone_counter.open_field("charleston_res.txt")
    information = getting_information.get_params("charleston_road.in")

    number_routers, number_x = backbone_counter.number_of_xr(field)
    number_backbones = backbone_counter.number_of_backbones(field, information)

    budget = information["budget"]
    price_router = information["r_price"]
    price_backbone = information["b_price"]

    result_formula = 1000*number_x + (budget -
                                      (price_backbone*number_backbones
                                       + price_router*number_routers))
    return result_formula


print(main())
