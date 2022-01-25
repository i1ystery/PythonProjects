import math
import random
from itertools import permutations


def get_min_diff(perm: list) -> list:
    results = [(None, float('inf'))]
    for p in perm:
        middle = int(len(p) / 2) if len(p) % 2 == 0 else int(len(p) // 2)
        #print(f'middle {middle}')
        sum_l = p[:middle]
        #print(f'sum_l {sum_l}')
        sum_r = p[middle:]
        #print(f'sum_r {sum_r}')
        diff = abs(sum(sum_l) - sum(sum_r))
        if diff < results[0][1]:
            results.clear()
            results.append((p, diff))
        elif diff == results[0][1]:
            results.append((p, diff))
    return results


def bruteforce(*args):
    possible_permutations = list(permutations(args))
    a = get_min_diff(possible_permutations)
    return a


def monte_carlo(*args):
    combinations = random.randint(2, len(args) - 1)
    perm = list()
    input_data = list(args)
    while combinations > 0:
        shuffled_list = list(input_data)
        random.shuffle(input_data)
        if shuffled_list not in perm:
            perm.append(tuple(shuffled_list))
            combinations -= 1
    results = get_min_diff(perm)
    return results


def heuristic(*args):
    pass


print(bruteforce(1, 2, 3, 4, 5))
print(monte_carlo(72, 73, 83, 32, 53))
