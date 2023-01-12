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
#     title: "d\xE9corateurs"
# ---

# %% [markdown] slideshow={"slide_type": "-"}
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # décorateurs

# %% [markdown]
# en guise de complément, ce notebook introduit la notion de *decorator*

# %% [markdown] slideshow={"slide_type": "slide"}
# ## déjà rencontré

# %% [markdown]
# on  déjà rencontré les décorateurs lorsqu'on a vu les méthodes statiques et les méthodes de classe
#
# ```python
#
# class Foo:
#     
#     @staticmethod
#     def bidule():
#         print("une méthode statique")
# ```
#     

# %% [markdown]
# dans cette notation, `staticmethod` est un **décorateur**  
# nous allons voir ça plus en détail

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pourquoi faire ?

# %% [markdown]
# l'idée du décorateur, c'est de **transformer** une fonction pour en déduire une autre fonction, qui fait un peu plus de choses que la première
#
# exemples
#
# * je veux afficher un message en entrant et en sortant de la fonction
# * je veux compter le nombre de fois qu'une fonction est appelée
# * je veux 'cacher' les résultats de la fonction que j'ai déjà calculés
# * ...
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## principe

# %% [markdown]
# * un décorateur, c'est donc un bidule qui transforme une fonction en une autre fonction
# * de quelle nature est ce bidule ? une fonction, bien sûr
#
# ![](media/decorator.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple

# %% slideshow={"slide_type": ""}
# pour débugger une fonction, c'est pratique
# de pouvoir afficher les arguments et le résultat

def decorator(f):
    def decorated(*args, **kwds):
        print(f"IN {f.__name__}({args=}, {kwds=})")
        result = f(*args, **kwds)
        print(f"OUT {f.__name__} -> {result}")
        return result
    return decorated        


# %% cell_style="split"
# une fonction au hasard
def add(x, y):
    """
    la somme
    """
    return x + y


# %% cell_style="split"
# la version décorée
# affiche les paramètres et le résultat
add1 = decorator(add)

add1(10, 20)


# %% slideshow={"slide_type": "slide"} cell_style="split"
# on peut appliquer la même recette
# à n'importe quelle fonction
# une autre
def mul(x, y=10):
    return x * y


# %% cell_style="split"
# la version décorée ... pareil
mul1 = decorator(mul)

mul1(10, y=20)


# %% [markdown]
# <div class=note>
#
# remarquez ici l'usage idiomatique de `*args` et `**kwds`  
# puisqu'on veut pouvoir faire ça quelque soit la signature de `f`    
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la syntaxe `@truc`

# %% [markdown]
# * bien sûr en pratique on nomme les décorateurs de manière plus explicite
# * disons qu'on appelle le nôtre `print_in_out`

# %% [markdown] cell_style="split"
# au lieu d'écrire
#
# ```
# def add(x, y):
#     return x + y
#     
# add = print_in_out(add)
# ```

# %% [markdown] cell_style="split"
# on peut se contenter de
#
# ```python
# @print_in_out
# def add(x, y):
#     return x + y
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le module `functools`

# %% [markdown]
# expose quelques décorateurs d'usage courant
#
# <https://docs.python.org/3/library/functools.html>

# %%
# c'est super inefficace comme façon de faire !
def fibo(n):
    return 1 if n <= 1 else fibo(n-1) + fibo(n-2)


# %%
# la preuve
# %timeit -n 1 -r 1 fibo(30)

# %% cell_style="split"
# avec ce décorateur, la fonction va retenir les 
# calculs qu'elle a faits précédemment
from functools import cache

@cache
def fibo(n):
    return 1 if n <= 1 else fibo(n-1) + fibo(n-2)


# %% cell_style="split"
# et du coup ça va plusieurs ordres de grandeur fois plus vite !

# %timeit -n 1 -r 1 fibo(30)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## conclusion
#
# * un décorateur est une fonction qui transforme une fonction en une autre fonction  
#   (ou encore, une fonction qui transforme une classe en une classe)  
# * avec la syntaxe  
#   ```python
#   @bidule
#   def ma_fonction(...):
#       ...
#   ```
#   on peut remplacer dans tout le code chaque appel à `ma_fonction` par un appel équivalent à la fonction décorée par `bidule`
# * sachez aussi que les usages avancés des décorateurs permettent de passer des paramètres ... au décorateur lui-même; un sujet que je vous laisse creuser si vous êtes intéressé
#   
# <div class=note>
#
# en toute rigueur, on devrait dire qu'un décorateur est un **callable** qui transforme ...  
# ça signifie qu'on peut aussi implémenter un décorateur .. comme une classe, avec la dunder `__call__`   
#     
# </div>    
#

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## les attributs de fonction (avancé)

# %% [markdown] tags=["level_intermediate"]
# * une fonction est un objet Python
# * sur lequel on peut définir des attributs arbitraires
# * et qui possède de base des attributs spéciaux

# %% cell_style="split" tags=["level_intermediate"]
# quand on utilise `def` 
# on a gratuitement le nom
add.__name__

# %% cell_style="split" tags=["level_intermediate"]
# et le docstring
add.__doc__

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### préserver les attributs spéciaux

# %% [markdown] tags=["level_intermediate"]
# du coup, notre première implémentation est améliorable car

# %% cell_style="split" tags=["level_intermediate"]
add1.__name__

# %% cell_style="split" tags=["level_intermediate"]
# vide

add1.__doc__


# %% slideshow={"slide_type": ""} cell_style="split" tags=["level_intermediate"]
# du coup on pourrait écrire
# quelque chose comme ceci  
# (mais voyez le slide suivant 
# pour la 'bonne' façon de faire)

def decorator2(f):
    def decorated(*args, **kwds):
        print(f"IN {f.__name__}({args=}, {kwds=})")
        result = f(*args, **kwds)
        print(f"OUT {f.__name__}")
        return result
    decorated.__name__ = f.__name__
    decorated.__doc__ = f.__doc__
    return decorated        


# %% cell_style="split" tags=["level_intermediate"]
add2 = decorator2(add)
add2.__name__, add2.__doc__

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### préserver les attributs spéciaux (2)

# %% [markdown] tags=["level_intermediate"]
# ou encore, la méthode recommandée est d'utiliser .. le décorateur `wraps`  
# qui va faire tout ce travail pour nous  
# avec juste une simple ligne en plus par rapport à la version naïve
#

# %% cell_style="split" tags=["level_intermediate"]
from functools import wraps

def decorator3(f):
    @wraps(f)
    def decorated(*args, **kwds):
        print(f"IN {f.__name__}({args=}, {kwds=})")
        result = f(*args, **kwds)
        print(f"OUT {f.__name__}")
        return result
    return decorated        


# %% cell_style="split" tags=["level_intermediate"]
add3 = decorator3(add)

add3.__name__, add3.__doc__
