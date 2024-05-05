# Bug Demo

> Missing Parenthesis (Shorter Version of Input)

```python
1 | def fahrenheit_to_celsius(fahrenheit):
2 |   return (fahrenheit - 32) * 5.0/9.0
3 |
4 | def is_prime(num:
5 |     if num <= 1:
6 |         return False
7 |     for i in range(2, int(num**0.5) + 1):
8 |         if num % i == 0:
9 |             return False
10|     return True
Answer: 4, missing_parenthesis
```

> Missing Colons

```python
def foo(bar)
```

> Missing Quotations

```python
var = "hello world
```

> Missing Commas

```
lst = [1, 2 3]
```

> Mismatched Quotations

```python
var = "hello world'
```

> Mismatched Brackets

```python
lst = [(1, 2}, (3, 4)]
```

> Keywords as Identifiers

```python
if = "val"
```