import timeit

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))


setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
stmt = 'func_one(100)'

print(timeit.timeit(stmt, setup, number=1000))

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

stmt2 = 'func_two(100)'

print(timeit.timeit(stmt2, setup2, number=1000))
