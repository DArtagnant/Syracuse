from syracuse_num import SyracuseNum
from decimal import Decimal

"""
Explications :

calcul de 5:
5 - 16 - 8 - 4 - 2 - 1
vol: 6 alt: 16
=> étapes de calcul : 5

calcul de 10
10 - cache 5
vol: 6+1 = 7 alt: max(10, 16) = 16
suppression de 5 dans le cache
=> étapes de calcul : 2 au lieu de 6
"""


class Cache:
    def __init__(self) -> None:
        self._cache = {}

    def add(self, num, alt, vol):
        assert isinstance(num, int)
        assert isinstance(alt, int)
        assert isinstance(vol, int)
        self._cache[num] = (alt, vol)

    def get(self, num, sup=True):
        r = self._cache[num]
        if sup: self.sup(num)
        return r

    def sup(self, num):
        del self._cache[num]
    
    def update(self, autre_cache):
        assert isinstance(autre_cache, Cache)
        self._cache.update(autre_cache._cache)

def b_alt(num1, num2):
    return num1 if num1.alt > num2.alt else num2

def b_vol(num1, num2):
    return num1 if num1.vol > num2.vol else num2

def b_rap_alt_num(num1, num2):
    return num1 if Decimal(num1.alt)/num1._num > Decimal(num2.alt)/num2._num else num2

def b_rap_vol_num(num1, num2):
    return num1 if Decimal(num1.vol)/num1._num > Decimal(num2.vol)/num2._num else num2

def best(print_to, cherche, addtour=2):
    assert (print_to-1) % addtour == 0, f"pour que la valeur soit printé, il faut que print_to respecte (print_to-1) % addtour == 0 (print_to={print_to}, addtour={addtour})"
    bests = [SyracuseNum(1)] * len(cherche)
    num = 1
    while True:
        newnum = SyracuseNum(num)
        for fnum, func in enumerate(cherche):
            bests[fnum] = func(bests[fnum], newnum)
        if num % print_to == 0:
            print([b._num for b in bests])
        num += addtour

if __name__ == "__main__":
    best(10001, (b_rap_alt_num, b_rap_vol_num))