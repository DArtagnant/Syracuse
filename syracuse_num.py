from typing import Optional
import matplotlib.pyplot as plt

def is_even(num:int) -> bool:
    """Renvois vrai si le nombre passé est pair

    Args:
        num (int): nombre à tester

    Returns:
        bool: 
    """
    return num%2 == 0

class SyracuseNum():
    def __init__(self, num:int) -> None:
        """Crée un nouvel objet SyracuseNum du nombre num

        Args:
            num (int): nombre supérieur à 0 avec lequel est créé l'instance
        """
        assert num > 0 and isinstance(num, int)
        self._num = num

        self._vol_cache = None
        self._alt_cache = None
    
    @property
    def is_even(self) -> bool:
        """Vrai si le nombre de l'instance est pair, fait appel à la méthode globale is_even

        Returns:
            bool:
        """
        return is_even(self._num)
    
    @staticmethod
    def next(num:int) -> int:
        """Fonction statique qui renvoi le prochain nombre de num d'après la suite de Syracuse

        Args:
            num (int): Nombre supérieur à 0 dont on veut le nombre suivant

        Returns:
            int: le nombre suivant
        """
        assert num > 0
        if is_even(num):
            next = num // 2
        else:
            next = num *3 +1
        return next
    
    def graphique(self, ax: Optional[plt.Axes] = None, show:bool = True) -> None:
        """Affiche un graphique avec matplotlib

        Args:
            ax (plt.Axes, optional): ax de matplotlib, peut être défini pour afficher
                le graphique dans un graphique matplotlib déjà inititié. Defaults to None.
            show (bool, optional): Si vrai affiche le graphique avec plt.show(). Defaults to True.
        """
        if not ax:
            _, ax = plt.subplots()
        self._graph_plot(ax)
        if show:
            plt.show()
    
    def _graph_plot(self, ax:plt.Axes, *args, **kwargs):
        return ax.plot(range(len(self)), list(self), *args, **kwargs) #type:ignore
    
    def __iter__(self):
        self._iter_num = self._num
        self._iter_first = True
        self._iter_vol = 1
        self._iter_alt = self._num
        return self
    
    def __next__(self):
        if self._iter_first:
            self._iter_first = False
            return self._iter_num
        elif self._iter_num != 1:
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

    s = SyracuseNum(10709980568908647)
    print(f"vol : {s.vol}")
    print(f"altitude : {s.alt}")
    s.graphique()