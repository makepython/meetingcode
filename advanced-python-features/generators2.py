def number_generator():
    yield 1
    yield 2
    yield from subgenerator()
    for i in range(50,53):
        yield i
    yield 0

def subgenerator():
    yield 25
    yield 39
    yield 42

g = number_generator()
for entry in g:
    print(entry)
