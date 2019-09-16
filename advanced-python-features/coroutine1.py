def coroutine():
    print("yielding 1")
    yield 1
    print("yielding 2 and accepting value")
    a = yield 2
    print("Accepted value", a, ". Yielding * 4")
    b = yield a*4
    print("Accepted value", b, ". Yielding * 8")
    return b * 8

coro = coroutine()

print(next(coro))
print(coro.send(42))
print(coro.send(21))
print(coro.send(2))

