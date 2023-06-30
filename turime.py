def f(p):
    return p // 100 + 10 if p // 100 >= 10 else p // 100


p = int(input())
result = f(p)
print(result)
