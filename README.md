# LearnPythonTheHardWay
LearnPythonTheHardWay File


## ex39.py
```Python
class Thing():
    def test(hi):
        print(type(hi))
        print("hi")

a = Thing()
a.test() ##注意：这里虽然需要1个参数但是我们使用a调用test方法的时候，首先会传一个a过去，因此我们调用的时候不需要加参数否则会报错



```


## 字典中的内容是无序的

### 使用for循环遍历字典
```Python
for v,k in a.items():
    print("{v}：{k}".format(v=v, k=k))
```

### 使用for循环获取字典中的键
```Python
for k in a.keys():
    print(k)
```

### 使用for循环获取字典中的值
```Python
for v in a.values():
    print(v)
```