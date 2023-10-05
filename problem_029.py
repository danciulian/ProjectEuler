"""Project Euler: Distinct Powers"""
from itertools import product

LIMIT = 100


def distinct_powers():
    """product is equivalent with the cartesian product"""
    terms = set()
    for a, b in product(range(2, LIMIT + 1), repeat=2):
        terms.add(a ** b)

    return len(terms)

print(distinct_powers())
