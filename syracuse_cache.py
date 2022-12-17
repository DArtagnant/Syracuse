import pandas as pd
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
    def __init__(self, chemin) -> None:
        self._chemin = chemin
        self._df = pd.read_csv(self._chemin).set_index('num')
    
    @classmethod
    def create(cls, chemin):
        df = pd.DataFrame(columns=['num', 'alt', 'vol', 'suite'])
        df = df.set_index('num')
        df.to_csv(chemin)
        return cls(chemin)

    def add(self, num, alt, vol, long=None):
        assert isinstance(num, int)
        assert isinstance(alt, int)
        assert isinstance(vol, int)
        self._df.loc[num] = [alt, vol, long]

    def get(self, num, sup=True):
        print(f"cherche {num}")
        return self._df.loc[num]
    
    def sup(self, num):
        self._df = self._df.drop(index=num)
    
    def save(self):
        self._df.to_csv(self._chemin)

if __name__ == "__main__":
    cache = Cache.create("1test.csv")
    cache.add(5,10,6,[5,65,48,8498,48])
    print(cache.get(7).vol)
    cache.sup(5)