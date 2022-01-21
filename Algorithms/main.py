from itertools import permutations


def boat_brute_force(*args):
    possible_permutations = list(permutations(args))


def find_best(perumations):
    perm_diff = dict
    for p in perumations:
        middle = len(p)//2
        sum_l = p[:middle]
        sup_r = p[middle:]
        diff = sum_l - sup_r
        perm_diff[p] = diff
    differences = perm_diff.values().sort()
    result = [perm_diff.ind]




bruteforce(81, 73, 85)