import matplotlib.pyplot as plt

def is_even(num:int) -> bool:
    return num%2 == 0

class SyracuseNum():
    def __init__(self, num:int, cache=None) -> None:
        assert num > 0 and isinstance(num, int)
        self._num = num
        self._cache = cache

        self._vol_cache = None
        self._alt_cache = None
    
    @property
    def is_even(self) -> bool:
        return is_even(self._num)
    
    @staticmethod
    def next(num:int):
        assert num > 0
        if is_even(num):
            next = num // 2
        else:
            next = num *3 +1
        return next
    
    def graphique(self, ax=None, show=True):
        if not ax:
            _, ax = plt.subplots()
        self._graph_plot(ax)
        if show:
            plt.show()
    
    def _graph_plot(self, ax, *args, **kwargs):
        return ax.plot(range(len(self)), list(self), *args, **kwargs) #type:ignore
    
    def __iter__(self):
        self._iter_num = self._num
        self._iter_first = True
        self._iter_vol = 1
        self._iter_alt = self._num
        self._iter_avenir = None
        return self
    
    def __next__(self):
        if self._iter_first:
            self._iter_first = False
            return self._iter_num
        elif self._iter_avenir != None:
            if len(self._iter_avenir) == 0:
                raise StopIteration
            else:
                return self._iter_avenir.pop(0)
        elif self._iter_num != 1:
            if self._cache:
                try:
                    data_cache = self._cache.get(self._iter_num)
                except KeyError: pass #retour dans le cycle normal
                else: #on embranche dans les donnés mise en cache
                    if not self._vol_cache:
                        self._vol_cache = data_cache.vol
                    if not self._alt_cache:
                        self._alt_cache = data_cache.alt
                    if data_cache.suite:
                        liste_avenir = data_cache.suite.copy()
                        while self._iter_num != liste_avenir.pop(0): pass#BUG Erreur avec numpy
                        self._iter_avenir = liste_avenir
                    else:
                        self._iter_num = SyracuseNum.next(self._iter_num)
                    return self._iter_num
            self._iter_num = SyracuseNum.next(self._iter_num)

            if not self._vol_cache:
                self._iter_vol += 1
            if not self._alt_cache:
                if self._iter_num > self._iter_alt:
                    self._iter_alt = self._iter_num

            return self._iter_num
        else:
            if not self._vol_cache:
                self._vol_cache = self._iter_vol
            if not self._alt_cache:
                self._alt_cache = self._iter_alt
            if self._cache:
                self._cache.add(self._num, self._alt_cache, self._vol_cache)
            raise StopIteration
    
    def __len__(self):
        return self.vol

    @property
    def vol(self):
        if self._vol_cache:
            return self._vol_cache
        else:
            [_ for _ in self]
            return self._vol_cache
    
    @property
    def alt(self):
        if self._alt_cache:
            return self._alt_cache
        else:
            [_ for _ in self]
            return self._alt_cache


if __name__ == "__main__":
    """
    s = SyracuseNum(10709980568908647)
    print(f"vol : {s.vol}")
    print(f"altitude : {s.alt}")
    s.graphique()
    """
    from syracuse_cache import Cache
    c = Cache("1test.csv")
    s = SyracuseNum(27, c)
    print([n for n in s])
    print(f"vol: {s.vol}")
    print(f"alt: {s.alt}")
    c.save()