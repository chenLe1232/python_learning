from test_name import PI

test = 'I am from test_main not __name__'
def calc_round_area(radius):
    return PI * (radius ** 2)


def calculate():
    print("round area: ", calc_round_area(2))


if __name__ == '__main__':
    calculate()
    print('我是__name__')
