# Syracuse

## Dépendances

Pour faire fonctionner le programme, il faut Python 3.7 ou supérieur ([télécharger Python](https://www.python.org/downloads/)) et avoir installé matplotlib ([installer matplotlib](https://www.tutorialspoint.com/how-to-install-matplotlib-in-python)).
Les fichiers python doivent être dans le même répertoire.

Pour lire le code vous pouvez utiliser l’éditeur basique mais je vous conseille Visual Studio Code qui fonctionne aussi avec Java ou php ([installer vsCode](https://code.visualstudio.com/Download)).

## Lancer

Il existe quatres fichiers python :

* *syracuse_num.py* s’occupe des calculs et d’afficher un graphique simple
* *syracuse_graphs.py* permet d’afficher un graphique dynamique
* *syracuse_app.py* affiche 3 graphiques cliquables avec le bouton droit (graphiques altitude pour les nombre de 1 à 100, vol pour les nombre de 1 à 100, graphique simple de syracuse pour nombre entré)
* *syracuse_best.py* permet de trouver les meilleurs nombres selon des caractéristiques (plus grande altitude, plus grand rapport altitude/nombre ...)

## Nombres

Je vous conseille de tester les programmes avec :

* *27* qui possède le meilleur ratio vol/nbr testé pour au  moins les nombres inférieurs à 10 millions
* *10709980568908647* qui possède la plus haute altitude [^1]
* *2361235441021745907775* qui possède le plus long vol pour les nombres inférieurs à 2<sup>72</sup> [^1]
* *77671* qui possède la plus haute altitude pour les nombres inférieurs à 100 000 [^1]

[^1]: D'après <https://calculis.net/syracuse>
