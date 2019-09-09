def number_generator():
    yield 1
    yield 2
    yield 25
    yield 39
    yield 42
    for i in range(50,53):
        yield i
    yield 0

g = number_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# Exhausted!
try:
    print(next(g))
except StopIteration as e:
    print(e.__class__)

g = number_generator()
for entry in g:
    print(entry)
