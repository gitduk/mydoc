# Python

### [深入 Python 流程控制](http://www.pythondoc.com/pythontutorial3/controlflow.html#python)

`else` 的另类用法

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```



**默认参数只会被赋值一次**

```python
def func(num,l=[]):
    l.append(num)
    return l

> func(1)
> [1]
> func(2)
> [1, 2]
> func(3)
> [1,2,3]
```



列表解析

```python
# * 解析列表
num_list = [1, 10]
for i in range(*num_list):
    print(i)

> 1
> 2
...
> 9

# ** 解析字典
param_dict = {'name':'kaige', 'age':18}
def print_person_info(name, age=None):
    print(f"name: {name}\nage: {age}")

print_person_info(**param_dict)

> name: kaige
> age: 18
```

