VALUES = {
    (True, True): 1,
    (False, True): 2,
    (False, False): 3,
    (True, False): 4,
    (None, True): 'y',
    (None, False): 'y',
    (True, None): 'x',
    (False, None): 'x',
}


def is_zero(num: int):
    if num == 0:
        return True
    else:
        return False


def is_positive_negative(num: int):
    if is_zero(num):
        return None
    elif num > 0:
        return True
    else:
        return False


def coordinate_value_test(x: int, y: int):
    return is_positive_negative(x), is_positive_negative(y)

def get_quadrent(x: int, y: int):
    pass