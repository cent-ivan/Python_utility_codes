def make_cross(number):
    cross_index = number // 2
    cross = ""
    for i in range(number):
        if i == cross_index:
            for x in range(number):
                cross += "*"
        else:
            for y in range(number):
                if y == cross_index:
                    cross += "*"
                else:
                    cross += "-"
        cross += "\n"
    
    print(cross)

make_cross(7)