# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: while循环


'''
i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print("Numbers now：", numbers)
    print("At the bottom i is %d" % i)

print("The numbers.")
for num in numbers:
    print(num)

'''

i = 0
numbers = []
def print_other(j):
    while i < j:
        print("At the top i is %d" % i)
        numbers.append(i)

        i = i + 1
        print("Numbers now：", numbers)
        print("At the bottom i is %d" % i)

print_other(4)