import random
from itertools import permutations
import time
import tracemalloc
import random


def get_min_diff(perm: list) -> list:
    results = [(None, float('inf'))]
    for p in perm:
        odd = 0
        if len(p) % 2 == 0:
            middle = int(len(p) / 2)
        else:
            middle = len(p)//2
            odd = 1
        sum_l = p[:middle]
        sum_r = p[middle + odd:]
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
    combinations = random.randint(len(args)//2, len(args) - 1)
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
    possible_permutations = list(permutations(args))
    half_permutations = possible_permutations[:len(possible_permutations)//2]
    half_results = get_min_diff(half_permutations)
    results = []
    for res in half_results:
        results.append(res)
        reversed_res = (tuple(reversed(res[0])), res[1])
        results.append(reversed_res)
    return results


if __name__ == "__main__":
    lulw = []
    for i in range(0,5):
        lulw.append(i)
    tracemalloc.start()
    startTime = time.time()
# ============== Zacatek mereneho zdrojoveho kodu ==================
    print(bruteforce(*lulw))
    print(monte_carlo(*lulw))
    print(heuristic(*lulw))
# =============== Konec mereneho zdrojoveho kodu ==================
    timeConsupmtion = (time.time() - startTime) * 1000
    memoryConsumption = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()

    print("Spotreba pameti: " + str(memoryConsumption) + " Bytes")
    print("Spotreba casu: " + str(timeConsupmtion) + " milisec")

