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
#     title: "pr\xE9sentation du code"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python/main/notebooks/_static/style.html")


# %% [markdown]
# # présentation du code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## style de présentation du code
#
# * tout le code de la librairie standard obéit à des règles de présentation
# * elles ne sont pas imposées par le langage, **MAIS**
# * elles sont très largement appliquées
# * autant prendre de bonnes habitudes
# * survol rapide ici des traits les plus marquants

# %% [markdown] slideshow={"slide_type": "slide"}
# ## PEP-008

# %% [markdown]
# ces règles de présentation sont explicitées dans [la note dite *PEP-008*](https://www.python.org/dev/peps/pep-0008/)
#
# les points les plus importants qu'on vous demande **de retenir et d'appliquer** :

# %% [markdown]
# | OUI | NON |
# |-|-|
# | `fonction(a, b, c)` | ~~`fonction (a,b,c)`~~
# | `GLOBALE = 1000` | ~~`globale=1000`~~ |
# | `variable`, `ma_variable` | ~~`Variable`~~, ~~`maVariable`~~ |
# | `module`, `function` | ~~`Module`~~, ~~`Function`~~ |
# | `Classe`, `UneClasse`  | ~~`classe`~~, ~~`ma_classe`~~, ~~`maClasse`~~ |
# | lignes de longueur <= 80 caractères | lignes très longues |
# | *docstrings* pour documenter à minima| |

# %% [markdown]
# on va voir tout ça un peu plus en détail

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les espaces

# %% [markdown]
# |  OUI  |  NON  |
# |------------------|---------------|
# | `a = 10` | ~~`a=10`~~ |
# | `L = [1, 2, 3, 4]` | ~~`L = [1,2,3,4]`~~ |
# | `D = ['k1': 'v1', 'k2': 'v2'}` | ~~`D = ['k1':'v1', 'k2' : 'v2'}`~~ |

# %% [markdown]
# |  OUI  |  NON  |
# |------------------|---------------|
# | `def foo(a, b, c):` | ~~`def foo (a, b, c):`~~ | 
# |                     | ~~`def foo(a,b,c):`~~ | 
# | `res = foo(a, b, c)` | ~~`res = foo (a, b, c)`~~ |

# %% [markdown]
# ### les espaces...

# %% [markdown]
# | **OUI** | **NON** |
# |---------|---------|
# | `d = {1: 'un', 2: 'deux'}` | ~~`d = {1:'un',2:'deux'}`~~ |
# |                          | ~~`d = { 1 : 'un', 2 : 'deux' }`~~ |
# | `s = {'a', 'b', 'c', 'd'}` | ~~`s = {'a','b','c','d'}`~~ |
# |                          | ~~`s = { 'a' , 'b' , 'c' , 'd' }`~~ |

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les noms de variables

# %% [markdown] cell_style="split"
# | type d'objet | catégorie |
# |------------------|---------------|
# | variable usuelle | 1 | 
# | fonction | 1 |
# | module | 1 | 
# | classe | 2 |

# %% [markdown] cell_style="split"
# | catégorie |  OUI  |  NON  |
# |------|------------------|---------------|
# | 1    | `minuscule` | ~~`MAJUSCULE`~~ |
# | 1    | `deux_mots` | ~~`DeuxMots`~~  |
# | 2    | `Mixte`     | ~~`minuscule`~~ (sauf types prédéfinis) |
# | 2    | `DeuxMots`  | ~~`MAJUSCULE`~~ |

# %% [markdown] slideshow={"slide_type": "slide"}
# ## largeur de la page
#
# * dans sa version orthodoxe, la largeur de la page est limitée à 80 caractères
#   en pratique aujourd'hui on peut être un peu plus souple,   
#   mais **jamais > 100 caractères de large**
#
# * l'idée est de pouvoir juxtaposer plusieurs codes (3 voire 4 )  
#   dans la largeur d'un écran moderne
#
# * on a parfois besoin de recourir à des astuces pour y arriver

# %% [markdown] slideshow={"slide_type": "slide"}
# ### longueur des lignes

# %% [markdown]
# plusieurs astuces pour respecter une largeur fixe :

# %%
# 1. utiliser les parenthèses

def foo():
    if expression(args):
        return (le_resultat() and de_l_expression() 
                and est_susceptible() and de_prendre()
                and beaucoup_de_place())


# %% [markdown] slideshow={"slide_type": "slide"}
# ### longueur des lignes et parenthèses

# %%
# 2. ça marche aussi avec les {} et [] 

GLOBAL_MAP = [
    {'shortcut': 'ctrl-w', 'function': 'RISE:render-all-cells'},
    {'shortcut': 'ctrl-q', 'function': 'RISE:edit-all-cells'},
]


# %% [markdown] slideshow={"slide_type": "slide"}
# ### longueur des lignes et chaines littérales

# %%
# 3. lorsqu'on a besoin de retourner des chaines de caractères très longues
# on peut utiliser un conjonction de
# * parenthèses
# * concaténation des chaines dans le source

def longue_chaine(nom, prenom):
    return (
        f"<table><thead><tr><th>Nom</th><th>Prénom</th></tr></thead>"
        f"<tbody><tr><td>{nom}</td><td>{prenom}</td></tr></tbody>"
        f"</table>"
    )


# %% cell_style="center"
# astuce
# là on a produit du HTML, pour le voir rendu 
# dans le notebook

from IPython.display import HTML
HTML(longue_chaine("Jean", "Dupont"))


# %% [markdown] slideshow={"slide_type": "slide"}
# ### longueur des lignes : éviter le `\`

# %% [markdown]
# enfin il peut être utile de savoir qu'on peut 'échapper' les fins de ligne

# %%
# on **pourrait** écrire ça (sachez le lire) 
# mais je vous recommande de **ne pas faire comme ça**
# essayez par exemple d'ajouter un espace juste après un \ 
# ça ne se voit pas et pourtant ça fait tout planter

def foo():
    if expression(args):
        return le_resultat() and de_l_expression() \
                and est_susceptible() and de_prendre() \
                and beaucoup_de_place()


# %% [markdown]
# **les parenthèses, c'est mieux**  
# dans l'exemple 1. on a le même code, mais avec les parenthèses on n'a pas cette fragilité

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le docstring
#
# lorsqu'on écrit une fonction (ou une classe, ou un module) on la documente comme ceci

# %% cell_style="split" slideshow={"slide_type": ""}
def gcd(a, b):
    """
    returns the greatest common divisor
    of both inputs
    """
    while b:
        a, b = b, a % b
    return a


# %% cell_style="split"
help(gcd)


# %% [markdown] slideshow={"slide_type": "slide"}
# * le docstring est une simple chaine  
#   qui apparaît en premier
#
# * permet de ranger de la documentation 
#   directement dans l'objet fonction
#
# * pas indispensable pour les fonctions internes  
#   mais nécessaire pour celles qui sont exposées aux utilisateurs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## type hints
#
# de manière optionnelle, on peut indiquer les types des arguments et le type de retour

# %% cell_style="split" slideshow={"slide_type": ""}
def gcd2(a: int, b: int) -> int:
    """
    returns the greatest common divisor
    of both inputs
    """
    while b:
        a, b = b, a % b
    return a


# %% cell_style="split"
help(gcd2)

# %% [markdown] slideshow={"slide_type": "slide"}
# * annotations de type (*type hints*) totalement optionnelles et ignorées par l'interpréteur
# * mais utiles pour une meilleure documentation
# * et aussi pour détecter des erreurs de type par **analyse statique** i.e. avant l'exécution, avec des outils dédiés [comme par exemple `mypy`](http://mypy-lang.org/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fait partie des attendus
#
# * ne pas parler le PEP008, c'est un peu  
#   comme faire plein de fautes d'orthographe
#
# * ça n'empêche pas d'avoir de bonnes idées  
#   mais ça donne mauvaise impression
#
# * faites-y attention à partir de maintenant 
# * fait partie des critères pour l'évaluation

# %% [markdown] slideshow={"slide_type": "slide"}
# ## de nombreux outils

# %% [markdown] cell_style="center"
# * très grand nombre d'outils de vérification de code Python
# * du plus simple qui vérifie seulement *PEP008* - par exemple `flake8`
# * au plus compliqué - genre `pylint` - qui peut trouver 
#   * les erreurs de frappe dans les noms de variable
#   * les imports inutiles

# %% [markdown] slideshow={"slide_type": "slide"}
# ### command line

# %% [markdown]
# regardez du coté de 
#
# * `autopep8` (sait *réparer* avec l'option `-i`)
# * `black` (sait réparer)
#
# * `flake8` (affiche les erreurs)
# * `pylint` (affiche les erreurs pep8 
#  et bien d'autres d'ailleurs)

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ### vs-code

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ![](media/vscode-problems.png)

# %% [markdown] cell_style="split"
# ← <span style="font-size:small;">par exemple avec flake8</span>

# %% [markdown] cell_style="split"
# et pour naviguer entre les erreurs
#
# ![](media/vscode-next-problem.png)
