def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))

print(func_two(100000))