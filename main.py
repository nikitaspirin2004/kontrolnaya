class Couriers:
    def __init__(self, name, x, y, bag):
        self.name = name
        self.x = x
        self.y = y
        self.bag = bag

class Zakazi:
    def __init__(self, name, x, y, weight = 10):
        self.name = name
        self.x = x
        self.y = y
        self.weight = weight

f = open("couriers.txt")
n = int(f.readline())
kurieri = [] # список классовых курьеров
for i in range (n):
    a = f.readline().split(';')[:-1]
    couriers = {}
    couriers[a[0]] = a[1], a[2]
    _courier = Couriers(int(a[0]),int(a[1][0]),int(a[1][2]), int(a[2]))
    kurieri.append(_courier)
f.close()

zakazi = []
f = open("zakazi.txt")
n = int(f.readline())
for i in range (n):
    a = f.readline().split(';')[:-1]
    zakazi = {}
    zakazi[a[0]] = a[1], a[2]
    _zakaz = Zakazi(int(a[0]),int(a[1][0]),int(a[1][2]), int(a[2]))
    zakazi.append(_zakaz)
f.close()
print (zakazi)