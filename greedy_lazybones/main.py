import backbone_counter
from getting_information import *
from getting_field import get_field
from putting_routers import greedy_rs_placement, write_file


def main():
    # lists of maps
    in_names = ['charleston_road.in', 'opera.in', 'rue_de_londres.in',
                'lets_go_higher.in']

    out_names = ['charleston_road_res.txt', 'opera_res.txt',
                'rue_de_londres_res.txt', 'lets_go_higher_res.txt']

    results = {}

    overall_score = 0

    for i in range(len(in_names)):
        start = default_timer()

        # initializing required params
        field = get_field(in_names[i])
        info = get_params(in_names[i])

        # building router map
        new_field = greedy_rs_placement(field, info)
        print('BUILT')
        # writing down the results
        write_file(in_names[i], out_names[i], new_field)
        print('WRITTEN')

        finish = default_timer()
        time = round(finish - start, 8)

        # counting scores
        field = backbone_counter.open_field(out_names[i])
        information = get_params(in_names[i])

        # initializing params needed for counting score
        number_routers, number_x = backbone_counter.number_of_xr(field)
        number_backbones = backbone_counter.number_of_backbones(field, information)
        budget = information["budget"]
        price_router = information["r_price"]
        price_backbone = information["b_price"]

        # counting final_score
        total_score = 1000 * (number_x + number_routers) + (budget -
                                        (price_backbone * number_backbones
                                         + price_router * number_routers))
        overall_score += total_score
        results[out_names[i][:-4]] = {"Score" : total_score, 'Time' : time}

    results['Overall score'] = overall_score

    return results


if __name__ == "__main__":
    from timeit import default_timer
    start = default_timer()
    print(main())
    finish = default_timer()
    time = round(finish - start, 8)
