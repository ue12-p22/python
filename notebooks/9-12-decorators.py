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

# %% language="python"
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python/main/notebooks/_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # décorateurs

# %% [markdown]
# en guise de complément, ce notebook introduit la notion de *decorator*

# %% [markdown]
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

# %% [markdown]
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

# %% [markdown]
# ## exemple

# %% [markdown]
# * un décorateur, c'est donc un bidule qui transforme une fonction en une autre fonction
# * de quelle nature est ce bidule ? une fonction, bien sûr
#
# ![](media/decorator.png)

# %% slideshow={"slide_type": "slide"}
def decorator(f):
    def decorated(*args, **kwds):
        print(f"IN {f.__name__}({args=}, {kwds=})")
        result = f(*args, **kwds)
        print(f"OUT {f.__name__}")
        return result
    return decorated        


# %% cell_style="split"
def add(x, y):
    """
    la somme
    """
    return x + y


# %% cell_style="split"
add1 = decorator(add)

add1(10, 20)

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

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## les attributs de fonction

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
# notre première implémentation est améliorable car

# %% cell_style="split" tags=["level_intermediate"]
add1.__name__

# %% cell_style="split" tags=["level_intermediate"]
# vide

add1.__doc__


# %% slideshow={"slide_type": ""} cell_style="split" tags=["level_intermediate"]
# du coup on pourrait écrire

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
# ou encore, la méthode recommandée est d'utiliser .. un décorateur

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


# %% [markdown] slideshow={"slide_type": "slide"}
# ## le module `functools`

# %% [markdown]
# expose quelques décorateurs d'usage courant
#
# https://docs.python.org/3/library/functools.html

# %%
def fibo(n):
    return 1 if n <= 1 else fibo(n-1) + fibo(n-2)


# %%
# %timeit fibo(10)

# %% cell_style="split"
from functools import cache

@cache
def fibo(n):
    return 1 if n <= 1 else fibo(n-1) + fibo(n-2)

# %% cell_style="split"
# the cached version is 250 x faster 

# %timeit fibo(10)
