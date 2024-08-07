import random

random.seed(1)
msgs = ["Hi", "Hello", "Good mornig", "Good night", "See you later", "How are you", "Have a good day"]
with open("some.txt","w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))

with open("some.txt", "r") as f:
    for _ in range(3):
        print(f.readline().strip())
