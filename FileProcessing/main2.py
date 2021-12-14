import pickle


with open('my_favorite_friend.dat', 'rb') as file:
    profile = pickle.load(file)
print(profile)