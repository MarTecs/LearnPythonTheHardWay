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



def prin(j):
    global i ##声明全局变量i，如果没有这条语句，将会认为下面的i是一个局部变量
    while i < j:
        print("At the top i is %d" % i)
        numbers.append(i)

        i = i + 1
        print("Numbers now：", numbers)
        print("At the bottom i is %d" % i)

prin(10)