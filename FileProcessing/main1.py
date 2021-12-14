from SchoolProfile import SchoolProfile
import pickle


profile = SchoolProfile('Max', 'Kuzma', 'I1yStery', 'PV', 'SPSE Jecna', 'Ondrej Mandik')
with open('my_favorite_friend.dat', 'wb') as file:
    pickle.dump(profile, file)
