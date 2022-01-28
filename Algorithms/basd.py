import random
import time
import tracemalloc


def find(pole, kolikanasobnost, poc_prub):
    best = None
    for i in range(poc_prub):
        pom_rek =  find_rek(pole, [], kolikanasobnost)
        if (best == None or best[0] > pom_rek[0]):
            best = pom_rek
    return best [1]

def find_rek(pole, serazene, kolikanasobnost):
    nejlepsi = None
    if len(pole) != 0:
        pole1 = pole[:]
        vysledek = serazene[:]
        vysledek.append(pole1.pop(random.randint(0, len(pole1) - 1)))
        return find_rek(pole1, vysledek, kolikanasobnost)
    else:
        pom = int(len(serazene)/2)
        rozdil = 0
        for i in range(len(serazene)):
            if (pom == 0 and len(serazene)/2 == int(len(serazene)/2)):
                pom -= 1
            if (pom > 0):
                rozdil += serazene[i] * (kolikanasobnost  -pom)
            elif (pom < 0):
                rozdil -= serazene[i] * (kolikanasobnost  -pom)
            pom -= 1
        if (rozdil < 0):
            rozdil *= -1
        return [rozdil, serazene]

if __name__ == "__main__":
    time_complex = []
    space = []
    for i in range(0,200):
        arr = []
        for i in range(0, i):
            arr.append(i)
        tracemalloc.start()
        startTime = time.time()
# ============== Zacatek mereneho zdrojoveho kodu ==================
        find(arr, 2, 500)
        #bruteforce(*arr)
        #monte_carlo(*arr)
        #heuristic(*arr)
        #boat_boat_heurestics(*arr)
# =============== Konec mereneho zdrojoveho kodu ==================
        timeConsupmtion = (time.time() - startTime) * 1000
        memoryConsumption = tracemalloc.get_tracemalloc_memory()
        tracemalloc.stop()
        time_complex.append(timeConsupmtion)
        space.append(len(arr))
        #space.append(memoryConsumption)

    import matplotlib.pyplot as plt
    # plotting the points
    plt.plot(space, time_complex)

    # naming the x axis
    plt.xlabel('x - Space')
    # naming the y axis
    plt.ylabel('y - Time')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()