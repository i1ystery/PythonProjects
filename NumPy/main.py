# import numpy as np
#
# a = [[1.542, 1.521, 1.234, 1.213, 2.1211, 1.534, 1.234, 1.213, 2.1211, 1.534], [532, 567, 634, 532, 532, 532, 532, 532, 532, 532], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
# b = [[1.542, 1.521, 1.234, 1.213, 2.1211, 1.534, 1.234, 1.213, 2.1211, 1.534], [532, 567, 634, 532, 532, 532, 532, 532, 532, 532], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
# c = [[1.542, 1.521, 1.234, 1.213, 2.1211, 1.534, 1.234, 1.213, 2.1211, 1.534], [532, 567, 634, 532, 532, 532, 532, 532, 532, 532], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
#
# a = np.array(a)
# b = np.array(b)
# c = np.array(c)
#
# print('Brute force, časová složitost [sec]: ' + str(a[1][1:-1]))
# print('Monte carlo, časová složitost [sec]: ' + str(b[0][-5:]))
# print('Heuristika, časová složitost [sec]: ' + str(c[2][0]))
#
# print(c.data)


# import numpy as np
#
# brute_force = np.array([1, 2, 3, 0.1932, 1.1247, 2.2435, 2243, 2124, 2143])
# #a = np.array_split(brute_force, 3)
# # print(a.shape)
#  #spojeni po ose 1
# #vysledek = np.stack((a[0], a[1], a[2]), axis=1)
#  #vertikalni spojeni, po sloupcich
# #vysledek = np.vstack((a[0], a[1], a[2]))
#
# # #horizontalni spojeni, po radcich
# vysledek = np.hstack((a[0], a[1], a[2]))
# #
# # #spojeni do hloubky, po rozmerech
# #vysledek = np.dstack((a[0], a[1], a[2]))
# print(vysledek)

# import numpy as np
# data = np.array([0.1743, 0.2732, 0.3521, 0.4924])
# filter = [True, False, True, False]
# bubu = np.array([1, 2, 3, 4])
# nova_data = data+bubu
# print(nova_data)
# pripraveny_filtr = data < 0.25
# print(pripraveny_filtr)

# import numpy as np
# data = np.array([20, 23, -100, -5, 30, 70, -18,99,81,16,45,90,-39,-82,75,0,16,91,48,0,70])
# #new_data = np.where(data < 0)
# new_data = np.where(((1 <= data) & (data <= 50)) | (data < 0))
# print(data[new_data])


# import numpy as np
# print(np.random.randint(1,100, size=(10,10)))
# print(np.random.rand(3,5))
# print(np.random.choice([21,22,34,56]))
# print(np.random.choice([1,2,3,4,5], p=[0.1, 0.25, 0.25, 0.28, 0.12]))

# import numpy as np
# kamaradi = ['Dima', 'Anton', 'Matej']
# # np.random.shuffle(kamaradi)
# a = np.random.permutation(kamaradi)
# print(a)
# print(kamaradi)


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=2,scale=3,size=20), hist=False)

plt.show()
print(np.random.binomial(5,[1,2,3,4,5,6], 0.16))

