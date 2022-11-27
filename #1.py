from itertools import *
def find_comb(amount_couriers):
    a = ''
    combinations = []
    for i in range (amount_couriers):
        a += str(i)
    for i in permutations(a):
        combinations.append(''.join(i))
    return combinations

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other_point):
        x1 = self.x
        x2 = other_point.x
        y1 = self.y
        y2 = other_point.y
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return dist

    def get_distance_to_center(self):
        r = Point(0, 0)
        return self.get_distance(r)


class Couriers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other_point):
        x1 = self.x
        x2 = other_point.x
        y1 = self.y
        y2 = other_point.y
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return dist

    def get_distance_to_center(self):
        r = Point(0, 0)
        return self.get_distance(r)

'''заказы'''
z1 = Point(5,0)
z2 = Point(6,0)

'''курьеры'''
k1 = Couriers(5,1)
k2 = Couriers(4,0)


zakazi_0 = [z1,z2]
kurieri_0 = [k1,k2]
q = Point(0,0)

coriers_kolvo = int(input('Введите количество курьеров: '))
combinations = find_comb(coriers_kolvo)
for combination in combinations:
    print(combination)
    zakazi = []
    kurieri = []
    for i in zakazi_0:
        a = i
        zakazi.append(a)
    for i in kurieri_0:
        a = i
        kurieri.append(a)
    print(zakazi[1].x, zakazi[1].y)
    print(zakazi_0[1].x, zakazi_0[1].y)
    dictance = 0
    distance_with_center = 0
    sum_rasstoyaniy_itog = 0
    for courier in combination:
        courier1 = kurieri[int(courier)] #курьеру присваиваю классовое значения из списка
        cz = [] #массив расстояний
        for zakaz in zakazi:
            distance = courier1.get_distance(zakaz)
            distance_with_center = distance + zakaz.get_distance_to_center()
            cz.append(distance_with_center)
        min_dictance = min(cz)
        for zakaz in zakazi:
            distance = courier1.get_distance(zakaz)
            distance_with_center = distance + zakaz.get_distance_to_center()
            if min(cz) == distance_with_center:
                sum_rasstoyaniy_itog += min(cz)
                zakaz.x = 99999
                zakaz.y = 99999
        print(cz)

print (sum_rasstoyaniy_itog)