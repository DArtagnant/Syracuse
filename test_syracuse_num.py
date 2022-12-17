import syracuse_num
from syracuse_num import SyracuseNum as SN
import pytest


def test_func_is_even():
    assert syracuse_num.is_even(2)
    assert syracuse_num.is_even(306)
    assert not syracuse_num.is_even(3)
    assert not syracuse_num.is_even(456457)

def test_method_is_even():
    assert SN(10).is_even
    assert SN(464).is_even
    assert SN(89552).is_even
    assert not SN(9).is_even
    assert not SN(48483).is_even
    assert not SN(845).is_even

@pytest.mark.parametrize("nbr, voulu", [
    (1, 4),
    (2, 1),
    (3, 10),
    (4, 2),
    (1863, 5590),
    (5455644, 2727822),
    (49846589789798464549, 149539769369395393648)
    ])
def test_func_next(nbr, voulu):
    assert SN.next(nbr) == voulu

def test_integre_next():
    assert [n for n in SN(27)] == [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161,
                                484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155,
                                466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780,
                                890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566,
                                283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079,
                                3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102,
                                2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433,
                                1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35,
                                106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert [n for n in SN(684641548778)] == [684641548778, 342320774389, 1026962323168, 513481161584,
                                256740580792, 128370290396, 64185145198, 32092572599, 96277717798,
                                48138858899, 144416576698, 72208288349, 216624865048, 108312432524,
                                54156216262, 27078108131, 81234324394, 40617162197, 121851486592,
                                60925743296, 30462871648, 15231435824, 7615717912, 3807858956, 1903929478,
                                951964739, 2855894218, 1427947109, 4283841328, 2141920664, 1070960332,
                                535480166, 267740083, 803220250, 401610125, 1204830376, 602415188,
                                301207594, 150603797, 451811392, 225905696, 112952848, 56476424,
                                28238212, 14119106, 7059553, 21178660, 10589330, 5294665, 15883996,
                                7941998, 3970999, 11912998, 5956499, 17869498, 8934749, 26804248,
                                13402124, 6701062, 3350531, 10051594, 5025797, 15077392, 7538696,
                                3769348, 1884674, 942337, 2827012, 1413506, 706753, 2120260, 1060130,
                                530065, 1590196, 795098, 397549, 1192648, 596324, 298162, 149081,
                                447244, 223622, 111811, 335434, 167717, 503152, 251576, 125788,
                                62894, 31447, 94342, 47171, 141514, 70757, 212272, 106136, 53068,
                                26534, 13267, 39802, 19901, 59704, 29852, 14926, 7463, 22390, 11195,
                                33586, 16793, 50380, 25190, 12595, 37786, 18893, 56680, 28340, 14170,
                                7085, 21256, 10628, 5314, 2657, 7972, 3986, 1993, 5980, 2990, 1495,
                                4486, 2243, 6730, 3365, 10096, 5048, 2524, 1262, 631, 1894, 947,
                                2842, 1421, 4264, 2132, 1066, 533, 1600, 800, 400, 200, 100, 50,
                                25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40,
                                20, 10, 5, 16, 8, 4, 2, 1]

@pytest.mark.parametrize("nbr, voulu", [
    (1, 1),
    (27, 112),
    (36, 22),
    (646443, 292),
    (4894984848264864984165468984966256131160456145041046412567, 1382)
    ])
def test_vol(nbr, voulu):
    sn = SN(nbr)
    assert sn.vol == voulu
    assert len(sn) == voulu #type: ignore

@pytest.mark.parametrize("nbr, voulu", [
    (1, 1),
    (27, 9232),
    (36, 52),
    (646443, 2908996),
    (4894984848264864984165468984966256131160456145041046412567,
        33041147725787838643116915648522228885333078979027063284832)
    ])
def test_alt(nbr, voulu):
    sn = SN(nbr)
    assert sn.alt == voulu