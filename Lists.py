import random

random_list = [random.randint(0, 9) for i in range(15)]
for index, item in enumerate(random_list):
    print("Index position: {} , Number: {}".format(index, item))
print("Enter your number")
number = int(input())
index=random_list.index(number)
for index, item in enumerate(random_list):
    if number==item:
        print("Your number {} index in the list is {}".format(number, index))