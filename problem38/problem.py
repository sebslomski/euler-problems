import itertools


def pandigital(n, multipliers):
    for i in multipliers:
        if i <= 0:
            return None

    return int(''.join([str(n * i) for i in multipliers]))


def get_multipliers(n):
    multiplier = 1
    multipliers = []

    while n * multiplier < 1000:
        if '0' not in str(multiplier) and \
            len(set(str(multiplier))) == len(str(multiplier)):
            multipliers.append(multiplier)

        multiplier += 1

    return multipliers


def is_pandigit_1_9(n):
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if str(i) not in str(n):
            return False

    n_set = set(str(n))

    return len(n_set) == len(str(n))


def get_all_combinations(items):
    res = []

    for r in range(0, len(items) + 1):
        for subset in itertools.combinations(items, r):
            res.append(subset)

    return filter(lambda x: len(x) > 0, res)


def main():
    res = []

    for i in reversed(range(1, 1000)):
        multipliers = get_multipliers(i)

        for m in get_all_combinations(multipliers):
            pandigit = pandigital(i, m)

            if is_pandigit_1_9(pandigit):
                res.append(pandigit)

    return max(res)
