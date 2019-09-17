def adder(value):
    x = yield

    while True:
        x = yield x + value


def multiplier(value):
    x = yield

    while True:
        x = yield x * value


add = adder(5)
mul = multiplier(3)
add2 = multiplier(2)
next(add)
next(mul)
next(add2)

def pipeline(coros):
    x = yield
    while True:
        val = x
        for coro in coros:
            val = coro.send(val)
        x = yield val


p = pipeline([add, mul, add2])
next(p)
print(p.send(2))


