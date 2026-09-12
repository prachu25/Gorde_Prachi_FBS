
def demo():

    for i in range(100,200):
        yield i


o = demo()
print(next(o))
print('Next Value..')
print(next(o))
print('Next Value..')
print(next(o))
print('Next Value..')
print(next(o))
print('Next Value..')
print(next(o))
print('Next Value..')