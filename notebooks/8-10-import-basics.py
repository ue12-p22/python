# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   nbhosting:
#     title: modules
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown]
# # modules et packages

# %% [markdown] slideshow={"slide_type": "slide"}
# ## c'est quoi un module ?

# %% [markdown]
# * on peut voir un module comme une boîte à outils
#   * que `import` permet de **charger dans son espace de travail**
# * l'unité de base pour utiliser les librairies
#   * des centaines de modules dans la **librairie standard** Python
#   * des (dizaines de) milliers de **librairies tierces** sont disponibles  
#     voir PyPI - the Python Package Index  
#     <https://pypi.org/>
#
# * permet aussi de découper le code en morceaux  
#   minimiser les couplages

# %% [markdown] slideshow={"slide_type": "slide"}
# ## importation d’un module

# %% cell_style="split"
# ou bien regarder dans vs-code
# %cat mod.py

# %% cell_style="split"
# je peux l'importer
import mod

# %% cell_style="center"
# la variable 'mod' me donne
# une référence vers un objet module
type(mod)

# %% cell_style="split"
# les noms globaux sont exposés 
# comme des attributs dand l'objet module
('GLOBALE' in dir(mod)
 and 'spam' in dir(mod))

# %% cell_style="split"
# qu'on peut utiliser normalement
# ici j'appelle la fonction
mod.spam('good')

# %% [markdown] slideshow={"slide_type": "slide"}
# ## plusieurs formes d'`import`
#
# * la forme `import mod` est la plus basique
# * elle définit la variable `mod` qui désigne le module tout entier
# * on va voir quelques variantes
#   * pour l'instant pour les modules simples
#   * i.e. qui correspondent à un fichier
#   * on verra les packages dans un second temps

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `from module import name`

# %% cell_style="split"
from mod import spam
spam('direct') 

# %% cell_style="split"
# un peu comme
# spam = mod.spam

# %% [markdown]
# * `from mod import spam`
#   * définit la variable `spam` (et non `mod`)
#   * plus besoin de la référence au nom du module

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `import modulename as othername`

# %% cell_style="split"
import mod as mymod
mymod.spam("module renamed")

# %% cell_style="split"
# un peu comme
# import mod
# mymod = mod
# del mod

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `from modulename import name as newname`

# %% cell_style="split"
from mod import spam as myspam
myspam('renamed function')

# %% cell_style="split"
# un peu comme
# import mod
# myspam = mod.spam
# del mod

# %% [markdown] slideshow={"slide_type": "slide"}
# ### importer tous les syboles d'un module

# %% cell_style="split"
from mod import *
spam('star')

# %% cell_style="split"
# un peu comme
# mod.spam = spam
# mod.GLOBALE = GLOBALE
# ...

# %% [markdown]
# * `from mod import *` 
#   * copie le nom de **tous** les attributs du module
#   * dans l’espace de nommage local
#   * plus besoin donc non plus de la référence au nom du module
# * remarque: je **déconseille d'éviter** cette directive dans du code de **production**
#   * on perd la traçabilité des symboles importés

# %% [markdown] slideshow={"slide_type": "slide"}
# ## package = module pour un dossier

# %% [markdown]
# * il est possible d’organiser un gros code source dans un dossier
# * qui peut à son tour contenir d'autres dossiers
# * le **package** est un module qui correspond à un **dossier**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### attributs pour naviguer l'arbre

# %% [markdown]
# * le package est aux directories ce que le module est aux fichiers
# * un objet package est **aussi un objet module**
# * son espace de nommage permet d'accéder à des modules et packages
# * qui correspondent aux fichiers et répertoires contenus dans son répertoire

# %% [markdown] cell_style="split"
# arborescence fichiers
#
#     pack1/
#       pack2/
#         mod.py
#           | def eggs(): pass

# %% [markdown] cell_style="split"
# équivalence attributs
#
#     pack1
#     pack1.pack2
#     pack1.pack2.mod
#     pack1.pack2.mod.eggs

# %% [markdown] slideshow={"slide_type": "slide"}
# ### import d'un package

# %% cell_style="split"
# on peut soit importer le package directement
import pack1

# %% cell_style="split"
# comme tout à l'heure
# la variable pack1 désigne
# un objet de types module

type(pack1)

# %% cell_style="split"
# les attributs dans pack1
# permettent de naviguer
# dans l'arborescence

type(pack1.pack2)

# %% cell_style="split"
# etc...

type(pack1.pack2.mod.eggs)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## formes d'import liées aux packages

# %% [markdown] slideshow={"slide_type": ""}
# ### importer un sous module

# %%
# on peut choisir de n'importer qu'un morceau seulement
import pack1.pack2.mod

# %% [markdown]
# * cette notation demande d’importer le module dans le répertoire `pack1/pack2/mod.py`
# * `pack1` est recherché dans `sys.path`
# * ensuite on descend dans l'arbre des dossiers et fichiers

# %% [markdown] slideshow={"slide_type": "slide"}
# ### et autres variantes...

# %% [markdown] slideshow={"slide_type": ""}
# ici aussi:
#
# * on peut utiliser une clause `as newname`
# * pour renommer la variable importée

# %% slideshow={"slide_type": ""} cell_style="split"
# ex. 1
import pack1.pack2.mod as foo
foo.eggs()

# %% cell_style="split"
# etc...
from pack1.pack2 import mod as bar
bar.eggs()

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## `__init__.py`

# %% [markdown] tags=["level_intermediate"]
# * ce fichier **peut** être présent dans le **dossier**
# * s'il est présent, il est chargé lorsqu'on charge le package
#   * les symboles définis dedans deviennent des **attributs du package**
#   * en plus, donc, du contenu du dossier

# %% cell_style="split" slideshow={"slide_type": ""} tags=["level_intermediate"]
# la variable x ici

# %cat pack1/__init__.py

# %% cell_style="split" tags=["level_intermediate"]
# se retrouve aussi comme 
# un attribut du package
pack1.x

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### use case: raccourcis

# %% [markdown] cell_style="split" slideshow={"slide_type": ""} tags=["level_intermediate"]
# sans raccourci
#
# ```
# graphobj/
#     rect.py     -> classe Rect
#     square.py   -> classe Square
# ```

# %% [markdown] cell_style="split" tags=["level_intermediate"]
#
# il faut connaitre le détail  
# des internes du package
#
# ```python
# from graphobj.rect import Rect
# from graphobj.square import Square
# ```

# %% [markdown] cell_style="split" tags=["level_intermediate"]
# avec raccourci
#
# ```
# cat graphobj/__init__.py
# from .rect import Rect
# from .square import Square
# ```

# %% [markdown] cell_style="split" tags=["level_intermediate"]
# c'est plus simple
#
# ```python
#
# from graphobj import Rect
# from graphobj import Square
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## que fait une importation ?

# %% [markdown]
# * localiser le dossier/fichier correspondant au module 
#   * on ne met pas le `.py` du fichier lors d’un import
# * vérifier si le module est déjà chargé ou non
# * si non:
#   * charger le code en mémoire
#   * i.e. créer l'objet module avec ses attributs
# * affecter la variable locale 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### localisation du fichier du module

# %% [markdown]
# * localisation en parcourant dans l’ordre
#   * répertoire où se trouve **le point d'entrée**
#   * `PYTHONPATH` : variable d’environnement de l’OS
#   * répertoires des librairies standards
# * `sys.path` contient la liste des répertoires parcourus
#   * on peut modifier `sys.path` à l’exécution

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les modules sont en cache

# %% [markdown]
# * comme l’importation est une opération lourde  
#   un module n’est chargé qu’**une seule fois** 
#
# * les imports suivants réutilisent le module déjà présent en mémoire

# %%
# dans pack1/__init__.py on a mis un print(),
# mais ici le module est déjà chargé
# du coup ici, pas d'impression
import pack1

# %% [markdown] slideshow={"slide_type": "slide"}
# ### recharger un module

# %% [markdown] slideshow={"slide_type": ""}
# ### `importlib.reload`

# %%
# pour recharger un fichier 
import importlib
importlib.reload(pack1)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `autoreload` et IPython

# %% [markdown]
# * sous IPython, il existe une extension qui simplifie la vie
#   * pour recharger les modules modifiés
#   * logique en développement
#   * pas utile en production

# %%
# %load_ext autoreload
# %autoreload 2

# %% [markdown]
# <div class="note">
# pour installer ce réglage par défaut :
# <pre>
# <code>
# cat ~/.ipython/profile_default/ipython_config.py
# c.InteractiveShellApp.exec_lines = []
# c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
# c.InteractiveShellApp.exec_lines.append('%autoreload 2')
# </code>
# </pre>
# </div>

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## imports relatifs

# %% [markdown] tags=["level_intermediate"]
# * pour importer un module dans le même package
# * outre les imports absolus (les formes vues jusqu'ici)
# * on peut faire un **import relatif**
#   
# le mécanisme est **un peu** similaire à la navigation dans l'arbre des fichiers :
#
# `from .other import variable`
#
# signifie de faire un import depuis le module `other` **dans le même package** que le module où se trouve ce code

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### exemple

# %% tags=["level_intermediate"]
pack1.pack2.mod.__name__

# %% [markdown] cell_style="split" tags=["level_intermediate"]
# * si dans `pack1/pack2/mod.py` on écrit  
#     `from .aux import foo`
#
# * on va chercher un module dont le nom est  
#     `pack1.pack2.aux`    

# %% [markdown] cell_style="split" tags=["level_intermediate"]
# * si dans `pack1/pack2/mod.py` on écrivait  
#     `from ..aux import foo`
#
# * on chercherait un module dont le nom serait  
#     `pack1.aux`    

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### attention !

# %% [markdown] cell_style="split" tags=["level_intermediate"]
# * l'import relatif **ne fonctionne pas**  
#   sur la base de l'arborescence de *fichiers*
#
# * mais au contraire il se base sur  
#   l'arborescence des *modules*
#   
# différence subtile, mais frustration garantie

# %% [markdown] cell_style="split" tags=["level_intermediate"]
# ** à retenir**
#
# * sachez lire les imports relatifs
# * bien maitriser les imports avant de tenter de les utiliser
