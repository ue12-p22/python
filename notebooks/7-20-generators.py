# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
#       -toc
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: "les g\xE9n\xE9rateurs"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Thierry Parmentelat

# %% language="python"
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python/main/notebooks/_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # les générateurs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## rappels

# %% [markdown]
# pour fabriquer des itérables en Python
#
# * les types de base / containers (`list`, `set`, `dict`)
# * compréhensions - construisent un container, et donc
#   * allouent de la mémoire
#   * font vraiment les calculs tout de suite
# * expression génératrice
#   * syntaxe très voisine de la compréhension de liste
#   * mais construit uniquement **un itérateur**
#   * qui pourra - quand on l'utilisera - passer au suivant, et ainsi de suite

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la fonction génératrice

# %% [markdown]
# * la **fonction génératrice** est une dernière forme très commune d'itérateurs
# * écrite sous la forme d'une fonction  
#   qui fait `yield` au lieu de `return`

# %% cell_style="split"
# si une fonction contient
# au moins un yield
# elle devient une
# fonction génératrice

def squares(iterable):
    for i in iterable:
        yield i**2


# %% cell_style="split"
data = (4, 1, 7)

# cet objet est un générateur
squares(data)

# %% cell_style="split"
# en particulier
# on peut itérer dessus

for square in squares(data):
    print(square, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### vocabulaire
#
# * une expression génératrice retourne un objet de type `generator`
# * il est fréquent - par abus de langage - d'appeler aussi simplement *générateur*  
#   une fonction génératrice
#
# * mais précisément, c'est **l'appel** à une fonction génératrice  
#   qui retourne un objet de type `generator`
#
# * on a donc **deux syntaxes différentes** pour construire  
#   des objets qui sont **tous de type `generator`**

# %% [markdown] slideshow={"slide_type": "slide"}
# ## expression génératrice *vs* fonction génératrice

# %% cell_style="split"
# ces deux objets sont équivalents
gen1 = (x**2 for x in data)


# %% cell_style="split"
def squares(iterable):
    for i in iterable:
        yield i**2

gen2 = squares(data)

# %% cell_style="split"
for x in gen1:
    print(x)

# %% cell_style="split"
for x in gen2:
    print(x)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### expression génératrice *vs* fonction génératrice

# %% [markdown]
# * les deux formes de générateur (expression et fonction)  
#   produisent des objets de même type `generator`

# %% cell_style="split"
# une genexpr
gen1 = (x**2 for x in data)
type(gen1)

# %% cell_style="split"
# (le résultat d'une)
# fonction génératrice
gen2 = squares(data)
type(gen2)


# %% [markdown]
# * la fonction a toutefois une puissance d'expression supérieure
# * notamment elle permet de **conserver l'état** de l'itération  
#   sous la forme de variables locales

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exercice
#
# implémenter un générateur qui parcourt tous les nombres premiers

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## `yield from`

# %% [markdown]
# * une fonction génératrice est une fonction
# * donc elle peut appeler d'autres fonctions
# * qui peuvent elles-mêmes être des fonctions génératrices

# %% [markdown]
# exemple :
# partant d'une fonction génératrice qui énumère  
# tous les diviseurs d'un entier (1 et lui-même exclus)

# %% [markdown] cell_style="center"
# comment écrire un générateur  
# qui énumère tous les diviseurs  
# ... des diviseurs de `n` ?

# %% cell_style="split" slideshow={"slide_type": "slide"}
# on énumère les diviseurs
# en partant du plus grand
def divs(n):
    for i in range(n-1, 1, -1):
        if n % i == 0:
            yield i


# %% cell_style="split"
for div in divs(12):
    print(div, end=" ")

# %% cell_style="center"
# maintenant on voudrait écrire
# quelque chose qui fasse en gros
n = 12
for d1 in divs(n):
    for d2 in divs(d1):
        print(d2)


# %% [markdown]
# mais sous forme de fonction génératrice

# %% [markdown] slideshow={"slide_type": "slide"}
# ### essayons (1)

# %% [markdown]
# pour énumérer les diviseurs des diviseurs, on pourrait penser écrire

# %% cell_style="split"
# première idée

# pourquoi ça ne marche pas ?

def divsdivs1(n):
    for d in divs(n):
        return divs(d)


# %% cell_style="split" slideshow={"slide_type": "fragment"}
# c'est bien un générateur
divsdivs1(12)

# %% cell_style="split"
# mais...
for d in divsdivs1(12):
    print(d)


# %% [markdown] slideshow={"slide_type": "fragment"}
# * on entre dans le `for` avec d=6
# * on évalue `divs(6)` (un générateur)
# * **et c'est ça qu'on retourne** de suite

# %% [markdown] slideshow={"slide_type": "slide"}
# ### essayons (deuxième idée)
# pour énumérer les diviseurs des diviseurs, on pourrait penser écrire

# %% cell_style="split"
# pourquoi ça ne marche pas ?
def divsdivs2(n):
    for d in divs(n):
        yield divs(d)


# %% cell_style="split"
# c'est bien un générateur
divsdivs2(12)

# %% cell_style="split"
# mais...
for d in divsdivs2(12):
    print(d)


# %% [markdown] slideshow={"slide_type": "fragment"}
# * cette fois on va bien énumérer `divs(6)`, `divs(4)`, `divs(3)` puis `divs(2)`
# * **mais pas itérer** sur ces 4 générateurs
# * c'est pourquoi ils se retrouvent imprimés tels quels

# %% [markdown] slideshow={"slide_type": "slide"}
# ### essayons (troisième idée)
# pour y arriver il nous faire ceci
#

# %% cell_style="split"
def divsdivs3(n):
    for d in divs(n):
        for dd in divs(d):
            yield dd


# %% cell_style="split"
for d in divsdivs3(12):
    print(d)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### `yield from`

# %% [markdown]
# * pour rendre cela plus lisible
# * on voit que lorsqu'une fonction génératrice en appelle une autre
# * il y a nécessité pour une syntaxe spéciale: `yield from`

# %% cell_style="split"
def divdivs(n):
    for i in divs(n):
        yield from divs(i)


# %% cell_style="split"
for div in divdivs(12):
    print(div)


# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_advanced"]
# ## itérateurs à base d'une classe

# %% [markdown]
# on peut aussi créer des objets qui sont des itérateurs, grâce à ce qu'on appelle le "protocole" itérable
#
# dans les prochaines slides, on va construire de plusieurs façons différentes un objet qui a toujours les mêmes propriétés :
#
# * `carres_n` est un itérateur
# * qui est capable d'énumérer les carrés des nombres entiers

# %% slideshow={"slide_type": "slide"}
# en utilisant une fonction génératrice

def carres():
    i = 0
    while True:
        yield i*i
        i += 1

carres_1 = carres()

# %%
for _ in range(3):
    print(next(carres_1))

# %% slideshow={"slide_type": "slide"}
# qu'on peut facilement remplacer par une expression génératrice

from itertools import count
carres_2 = (i**2 for i in count())

# %%
for _ in range(3):
    print(next(carres_2))


# %% slideshow={"slide_type": "slide"}
# ou - un peu plus pédestre, dans ce cas d'usage
# on peut écrire une classe qui implémente
# __iter__ et __next__
#
# pour fabriquer un itérateur,
# il faut que __iter__() renvoie self

class Carres3:
    def __init__(self):
        self.i = 0
    def __iter_(self):
        return self
    def __next__(self):
        carre = self.i * self.i
        self.i += 1
        return carre

carres_3 = Carres3()

# %%
for _ in range(3):
    print(next(carres_3))


# %% slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ici on crée un objet qui est bien itérable
# mais comme __iter__(self) renvoie autre chose que self,
# ce n'est pas un itérateur, on ne peut pas faire next() dessus

class Carres4:
     def __iter__(self):
         return ( i*i for i in count() )

carres_4 = Carres4()

# %%
# on ne peut pas faire next()
try:
    for _ in range(3):
        print(next(carres_4))
except Exception as exc:
    print(f"OOPS, {type(exc)} {exc}")

# %%
# mais c'est quand même un itérable
# donc on peut faire un for avec
for x in carres_4:
    print(x)
    if x >= 4:
        break
