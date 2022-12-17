from syracuse_num import SyracuseNum
from decimal import Decimal

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