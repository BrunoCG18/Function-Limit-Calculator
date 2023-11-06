import matplotlib.pyplot


def funct(func, init_range, final_range):
    y_values = list()
    x_values = list()
    biggest_y = -1 * 10 ^ 20
    smallest_y = 10 ^ 20
    last_y = 0
    for x in range(init_range, final_range):
        y_values.append(func(x))
        x_values.append(x)

        if func(x) >= biggest_y:
            biggest_y = func(x)

        if func(x) <= smallest_y:
            smallest_y = func(x)

        last_y = func(x)

        if x % 1000 == 0:
            print(x)

    print(biggest_y)
    print(smallest_y)
    print(last_y)

    matplotlib.pyplot.plot(x_values, y_values)
    matplotlib.pyplot.show()


"""funct(lambda n: ((5*n) / (2*n+1))**3, 0, 1000000)"""
