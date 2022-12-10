#compatible python > 3.10
from decimal import Decimal
from typing import Generator
import matplotlib.pyplot as plt
from numpy import array

def is_even(num:int|Decimal) -> bool:
    return num%2 == 0

class Cache:

    class InexistantError(Exception): pass

    def __init__(self) -> None:
        self.cache:dict[int, tuple[int, int]] = {}
    
    def add(self, num:int, alt:int, vol:int) -> None:
        num = int(num)
        self.cache[num] = (alt, vol)
        try :
            del self.cache[num*2]
        except KeyError: pass
        if (num/3-1).is_integer():
            try:
                del self.cache[num/3-1]
            except KeyError: pass
    
    def get(self, num:int) -> tuple[int, int]:
        try:
            return self.cache[int(num)]
        except KeyError:
            raise Cache.InexistantError(num)
    
    def clear(self) -> None:
        self.cache = {}

cache:Cache = Cache()

def find_next(num: int) -> int:
    assert num > 0
    #calcul de la suite
    if is_even(num):
        next = int(num / 2)
    else:
        next = num *3 +1
    return next

def find_suite(num: int) -> Generator:
    while num != 1:
        num = find_next(num)
        yield num

def graphique(num:int) -> None:
    fig, ax = plt.subplots()
    l = list(find_suite(num))
    ax.plot(list(range(len(l))), l, linewidth=2.5)
    # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
    #     ylim=(0, 8), yticks=np.arange(1, 8))
    plt.show()

def get_prop(num: int) -> tuple[int, int]:
    assert num > 0
    alt = num
    vol = 1
    next = num
    while next != 1:
        try: ralt, rvol = cache.get(next)
        except Cache.InexistantError:
            next = find_next(next)
            if next > alt: alt = int(next)
            vol += 1
        else:
            if alt < ralt: alt = ralt
            vol += (rvol - 1)
            break
    cache.add(num, alt, vol)
    return alt, vol

def get_best(print_to=100000):
    num = Decimal(0)
    balt = (-1, -1)
    bvol = (-1, -1)
    while True:
        num += 1
        alt, vol = get_prop(num)

        #TESTS
        if balt[1] < alt/num:
            balt = (num, alt/num)
        if bvol[1] < vol/num:
            bvol = (num, vol/num)
        
        #PRINT
        if num%print_to == 0:
            print(balt, bvol)

###INFO###
print(get_prop(Decimal(2361235441021745907775)))