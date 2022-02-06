import random
import numpy as np
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
    #combinations = random.randint(len(args)//2, len(args) - 1)
    combinations = 500
    perm = list()
    input_data = list(args)
    while combinations > 0:
        shuffled_list = random.sample(input_data, len(input_data))
        if shuffled_list not in perm:
            perm.append(tuple(shuffled_list))
            combinations -= 1
    results = get_min_diff(perm)
    return results


def boat_boat_heurestics(*args):
    left = []
    right = []
    pomu = list(args)
    addLeft = True
    count_to_add = 1
    for _ in range(len(pomu)):
        maximal = max(pomu)
        pomu.remove(maximal)
        if addLeft:
            left.append(maximal)
            count_to_add -= 1
            if count_to_add == 0:
                addLeft = False
                count_to_add = 2
        elif not addLeft:
            right.append(maximal)
            count_to_add -= 1
            if count_to_add == 0:
                addLeft = True
                count_to_add = 2

    right.reverse()
    return left + right


if __name__ == "__main__":
    time_complex = []
    space = []
    for i in range(0, 10):
        arr = []
        for j in range(0, i):
            arr.append(j)
        tracemalloc.start()
        startTime = time.time()
# ============== Zacatek mereneho zdrojoveho kodu ==================
        bruteforce(*arr)
        #monte_carlo(*arr)
        #heuristic(*arr)
        #boat_boat_heurestics(*arr)
# =============== Konec mereneho zdrojoveho kodu ==================
        timeConsupmtion = (time.time() - startTime) * 1000
        memoryConsumption = tracemalloc.get_tracemalloc_memory()
        tracemalloc.stop()
        time_complex.append(timeConsupmtion)
        space.append(len(arr))
        space.append(memoryConsumption)

    # import matplotlib.pyplot as plt
    # # plotting the points
    # plt.plot(space, time_complex)
    #
    # # naming the x axis
    # plt.xlabel('x - Space')
    # # naming the y axis
    # plt.ylabel('y - Time')
    #
    # # giving a title to my graph
    # plt.title('My first graph!')
    #
    # # function to show the plot
    # plt.show()
    a = np.array(time_complex)
    b = np.array(space)
    print(a)
    print(b)
