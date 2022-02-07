import matplotlib.pyplot as plt
import numpy as np

monte_carlox = np.array([2, 5, 20])
monte_carloy = np.array([2, 2, 2])

heuristicx = np.array([2, 8, 14])
heuristicy= np.array([5, 5, 5])

monte_carlox_space = np.array([2, 5, 20])
monte_carloy_space = np.array([2, 2, 2])

heuristicx_space = np.array([2, 8, 14])
heuristicy_space = np.array([5, 5, 5])

bruteforcex = np.array([2, 3, 5])
pow = np.array([2, 2, 2])
bruteforcey = np.power(pow, bruteforcex)

bruteforcex_space = np.array([2, 3, 5])
pow = np.array([2, 2, 2])
bruteforcey_space = np.power(pow, bruteforcex)


#
# plt.subplot(1, 2, 1)
# plt.plot(bruteforcex, bruteforcey, marker='o', color='g', label='bruteforce')
# plt.plot(monte_carlox, monte_carloy, marker='o', color='b', label='monte carlo')
# plt.plot(heuristicx, heuristicy, marker='x', color='r', label='heuristic')
# plt.xlabel('Number of items')
# plt.ylabel('Time(ms)')
# plt.title('Time complexity')
# plt.legend()
# plt.grid(color='turquoise', linestyle='-', linewidth=2)
# plt.subplot(1, 2, 2)
# plt.plot(bruteforcex_space, bruteforcey_space, marker='o', color='grey', label='bruteforce_space')
# plt.plot(monte_carlox_space, monte_carloy_space, marker='o', color='b', label='monte carlo_space')
# plt.plot(heuristicx_space, heuristicy_space, marker='x', color='r', label='heuristic_space')
# plt.xlabel('Number of items')
# plt.ylabel('Space requirement(b)')
# plt.title('Space complexity')
# plt.legend()
# plt.grid(color='turquoise', linestyle='-', linewidth=2)
#
# plt.plot()
# plt.show()



y = np.array([3, 2, 1, 18])
y_labels = np.array([f'Vyznamenani - {y[0]}', f'Propadnuti - {y[1]}', f'Nehodnocen - {y[2]}', f'Ostatni - {y[3]}'])
plt.pie(y, labels=y_labels)
plt.title('Vysvedceni zaku')
plt.show()


x = np.random.normal(38.2, 3.1, 845)
plt.xlabel('Velikost obovu')
plt.ylabel('Pocet zakazniku')
plt.hist(x)
plt.title('Velikosti obvodu krku v Jiznich cechach')

plt.show()


x = np.array([5,8,7,15,31,34,18,4,2,10,17,26,23,45])
y = np.array([5,3,3,2,1,1,2,4,4,3,2,2,2,1])
plt.ylabel('Cas(min)')
plt.xlabel('Znamka')
plt.xticks(np.arange(0, 6, step=1))
plt.yticks(np.arange(0, 50, step=5))
plt.scatter(y, x)
plt.title('Znamky z anglictiny')
plt.show()