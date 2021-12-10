with open("helloworld.txt", "r") as file:
    print(file.read())

with open("helloworld.txt", "r") as file:
    print(file.readline())

with open("helloworld.txt", "r") as file:
    print(file.read(3))

with open("helloworld.txt", "r") as file:
    for count, line in enumerate(file):
        print(str(count) + " " + line)
