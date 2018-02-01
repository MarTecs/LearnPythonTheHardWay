# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 可爱的字典


things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])
print(things)

stuff = {
    'name': 'Zed',
    'age': 36,
    'height': 6 * 12 + 2
}

print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "San Francisco"
print(stuff['city'])


stuff[1] = 'Wow'
stuff[2] = 'Neato'
print(stuff[1])
print(stuff[2])
print(stuff)


## 删除字典中的部分内容
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

###############################练习
print("*" * 20)
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you.", "I don't want to get sued", "So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family", 'With pockets full of shells'])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()



a = {
    1: '1',
    2: '2'
}

## 使用for循环遍历字典
for v,k in a.items():
    print("{v}：{k}".format(v=v, k=k))

## 使用for循环获取字典中的键
for k in a.keys():
    print(k)

## 使用for循环获取字典中的值
for v in a.values():
    print(v)