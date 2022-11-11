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
#     title: "traits r\xE9cents"
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python/main/notebooks/_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # traits récents

# %% [markdown]
# ## *walrus operator* `:=`

# %% [markdown]
# > depuis Python-3.8

# %% [markdown]
# en Python - comme dans tous les langages on distingue entre
#
# ### expressions
#
# on appelle "expression" tous les bouts de code qui "donnent un résultat" et que donc on peut "combiner" entre eux;  
#
# par exemple quand on écrit
# ```python
# my_function(the_index[a+10], "message")
# ```
# il y a là-dedans 
#
# * la chaine `"message"`
# * le nombre `10`,
# * la variable `a`
# * la somme `...+...`
# * l'indexation `the_index[...]`
# * l'appel de fonction `my_function(...)`
# et tous ces fragments de code sont des expressions, comme elles renvoient un résultat on peut les combiner 

# %% [markdown]
# ### instructions
#
# les instructions au contraire sont des fragments qui "changent l'état" du programme, mais ne retournent pas de résultat; vous en connaissez plein déjà, par exemple:
#
# * la boucle `for`
# * la définition de classe avec `class ...:`
# * ... je vous laisse compléter cette liste, est-ce que vous pouvez citer d'autres instructions ?

# %% [markdown]
# ### la condition `if`
#
# petite digression: avant de parler de l'opérateur d'afectation, on peut examiner le cas du `if..then..else`  
# en fait il en existe deux formes en Python:
#
# * l'instruction - que vous connaissez tous bien sûr  
#   ```python
#   if condition:
#       do_something()
#   else:
#       something_else()
#   ```
# * l'expression, qu'on appelle .. eh bien tout simplement l'expression conditionnelle
#   ```python
#   do_something() if condition else something_else()
#   ```
#
# quelle différence me direz-vous ?  
# eh bien si j'ai besoin de récupérer le résultat de - selon le cas - `do_something()` ou `something_else()` pour, soit le ranger dans une variable, ou le passer en paramètre à autre chose, la forme **expression** est bien plus élégante parce que ça me permet de remplacer
#
# ```python
# if condition:
#     variable = do_something()
# else:
#     variable = something_else()
# on_continue(variable)
# ```
#
# par plus simplement
#
# ```python
# on_continue(do_something() if condition else something_else())
# ```

# %% [markdown]
# ### le *walrus*
#
# l'opérateur *walrus* (*a.k.a. *assignment expression*) 
# est un peu à l'affectation (`a = b`) ce que l'expression conditionnelle est au `if .. else:` 
#
# c'est-à-dire que c'est une **expression** qui à la fois
#
# * fait une affectation
# * et renvoie le résultat, qui peut donc être utilisé par une expression englobante

# %%
# exemple 1

# ceci fonctionne
a = 10
b = 20
c = a + b

# %%
# mais je ne pourrais pas le remplacer par ceci
c = (a = 10) + (b = 20)

# %%
# par contre, je peux faire ceci
(c := (a := 10) + (b := 20))

# %%
# exemple 2

# je ne peux pas écrire ceci
try:
    print( a = 100 )
except Exception as exc:
    print(f"OOPS {type(exc)} {exc}")

# %%
# mais je peux écrire ceci
print( b:= 100 )

# %%
# on a affecté b
b

# %% [markdown]
# ### cas d'usage
#
# le *walrus* est donc relativement récent, on s'en est passé pendant des décennies, ça signifie que son usage n'est pas non plus hyper-critique
#
# je vous recommande de l'utiliser de manière parcimonieuse; 
# en effet il existe des cas où son comportement peut sembler étrange - [voir par exemple ceci](https://stackoverflow.com/questions/63836490/strange-behavior-python-3-8-walrus-operator-chained-inequalities)
#
# toutefois dans certains cas d'usage ça peut être très pratique; par exemple voici un bout de code qui utilise des regexps pour faire une chose ou une autre selon celle qui matche
#
# essayez de récrire la même chose sans le *walrus*...

# %%
import re

RE_EMAIL = re.compile(r"mail:(?P<login>[.\w]+)@(?P<domain>[.\w]+)")
RE_HTTPS = re.compile(r"https://(?P<hostname>[.\w]+)/(?P<path>[-\w/]+)")

def display(token):
    if match := RE_EMAIL.match(token):
            print(f"token is a mail address with login= {match.group('login')}")
    elif match := RE_HTTPS.match(token):
            print(f"token is a https url with path= {match.group('path')}")
    else:
        print(f"{token} not understood")

display("mail:jean.mineur@minesparis.psl.eu")
display("https://nbhosting.inria.fr/the-path/to-the/notebooks")
        

# %% [markdown]
# ## l'instruction `match`
#
# > depuis python-3.10
#
# encore connu sous le nom de *structural pattern matching*

# %% [markdown]
# ### exemple 1: la base

# %%
# dans sa forme la plus simple

def display(x):
    match x:
        case 0:
            print('zéro')
        case 1:
            print('un')
        case _:
            print('autre chose')

display(0)
display(1)
display(2)

# %% [markdown]
# ### rappel: le *unpacking*

# %%
# pour rappel, le "unpacking" c'est le trait qui permet d'écrire
composite = (1, 2, 3)
a, b, c = composite

# on a 'déballé' le contenu de composite 
# pour le ranger dans les 3 variables
b

# %%
# et toujours pour rappel, le "extended unpacking"
first, *rest = composite

# étendu parce que ici la variable attrape-tout 'rest'
# capture tout ce qui n'est pas attrapé par une variable 'simple'
rest


# %% [markdown]
# ### exemple 2: unpacking

# %%
# avec match on peut aussi faire du unpacking
def display(x):
    match x:
        case a, b:
            print(f"deux {a=} et {b=}")
        case a, b, *c:
            print(f"trois {a=}, {b=} et {c=}")
        case _:
            print(f"autre chose {x}")

display((10, 20, 30))
display([10, 20])
display(100)


# %% [markdown]
# ### exemple 3: mixte

# %%
# on peut aussi mélanger des parties 'fixes'
# et des parties 'à assigner'

def display(x):
    match x:
        case 0, b:
            print(f"deux-zéro {b=}")
        case a, b:
            print(f"deux {a=} et {b=}")
        case _:
            print(f"autre chose {x}")

display((0, 20))
display((10, 20))


# %% [markdown]
# ### exemple 4: alternatives

# %%
def fact(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n*fact(n-1)

fact(3)

# %% [markdown]
# ### et bien plus...

# %% [markdown]
# sachez que c'est bien puissant que ce que j'ai illustré ici, notamment lorsque le sujet du `match` est une instance de classe
#
# ces quelques exemples vous donnent seulement un aperçu, au moins vous savez que ça existe et où aller chercher la documentation, , et vous pouvez deviner comment fonctionner un code qui utiliserait cette feature
#
# par contre ce trait date de la version 3.10 qui n'est pas encore forcément disponible partout; aussi je vous recommande, ici encore, d'user de ce trait avec modération, notamment si votre code a besoin d'être déployé prochainement.

# %% [markdown]
# ***
