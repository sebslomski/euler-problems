from problem import (
    main, pandigital, get_multipliers, is_pandigit_1_9, get_all_combinations
)

res = main()

def test_is_nine_digits_long():
    assert len(str(res)) == 9


def test_result_does_not_contain_zeros():
    assert '0' not in str(res)


def test_result_should_contain_each_number_once():
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        assert str(i) in str(res)


def test_pandigital_192():
    assert pandigital(192, [1, 2, 3]) == 192384576


def test_pandigital_9():
    assert pandigital(9 , [1, 2, 3, 4, 5]) == 918273645


def test_pandigital_should_return_none_if_multiplier_lte_than_0():
    assert pandigital(9 , [0, 1, 2, 3, 4, 5]) == None
    assert pandigital(9 , [0, -1, 2, 3, 4, 5]) == None


def test_get_multipliers():
    assert get_multipliers(999) == [1]


def test_get_multipliers_with_too_hight_number():
    assert get_multipliers(1000) == []


def test_is_pandigit_1_9_with_too_less_characters():
    assert is_pandigit_1_9(111111) == False


def test_is_pandigit_1_9_with_zero():
    assert is_pandigit_1_9(102345678) == False


def test_is_pandigit_1_9():
    assert is_pandigit_1_9(123456789) == True


def test_is_pandigit_1_9_with_double_characters():
    assert is_pandigit_1_9(123456799) == False


def test_get_all_combinations_123():
    res = [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    assert get_all_combinations([1,2, 3]) == res


def test_get_all_combinations_12():
    res = [(1,), (2,), (1, 2)]
    assert get_all_combinations([1,2]) == res
