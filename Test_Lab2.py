import Lab2


def test_get_user_input():
    result = [1, 2, 69, 7, 43, 27]
    sample = "1,2,69,7,43,27"
    assert (result == Lab2.get_user_input(sample))


def test_calc_average():
    result = 3.5
    assert (result == Lab2.calc_average([2, 3, 4, 5]))
