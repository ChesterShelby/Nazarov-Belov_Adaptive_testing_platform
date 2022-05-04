def gen(num):
    a = 10
    for i in range(3):
        a = yield i + num + a

gen_o = gen(5)

try:
    print(gen_o.send(None))
    print(gen_o.send(100))
    print(gen_o.send(50))
    print(gen_o.send(60))
except StopIteration:
    print('StopIteration')



class A:
    def __init__(self, num):
        self.num = num

    def __await__(self):
        a = 0
        for i in range(3):
            a = yield i + self.num + a


async def cor(num):
    await A(num)

cor_o = cor(5)
try:
    print(cor_o.send(None))
    print(cor_o.send(200))
    print(cor_o.send(30))
    print(cor_o.send(40))
except StopIteration:
    print('StopIteration')

