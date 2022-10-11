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
#     title: exos
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# <span><img src="media/inria-25-alpha.png" /></span>
# </div>

# %% [markdown]
# # exercices

# %% [markdown]
# ## comptage dans un fichier
#
# un exercice qui demande 
#
# * d'ouvrir des fichiers en lecture et en écriture
# * de faire diverses opérations sur les chaines
#
# en version auto-corrigée:
#
# https://nbhosting.inria.fr/auditor/notebook/exos-mooc:exos/w3/w3-s2-x1-comptage

# %% [markdown]
# ***

# %% [markdown]
# ## la calculette postfix
#
# un exercice pour évaluer les expressions numériques du genre de 
#
# * `10 20 +`  (= 30)
# * `30 40 + 30 *`  (=2 100)
#
# **indices**
#
# * cet exercice se prête à l'utilisation d'une pile
# * on découpe la chaine en morceaux (des `tokens`)
# * on empile les opérandes lorsqu'ils sont des nombres
# * lorsqu'on traite un token parmi `+-*/` :
#   * on dépile deux fois pour obtenir les opérandes
#   * on effectue l'opération
#   * on empile le résultat
#
#
# en version auto-corrigée:
#
# https://nbhosting.inria.fr/auditor/notebook/exos-mooc:exos/w6/w6-s9-x1b-postfix
#
# seul le premier exo est obligatoire, les rapides peuvent s'attaquer au second

# %% [markdown]
# ***

# %% [markdown]
# ## le palindrome

# %% [markdown]
# ### version simple 
#
# écrivez une fonction qui vérifie si une chaine est un palindrome
#
# par exemple
#
# * `palindrome("Eva, Can I Stab Bats In A Cave?")` → `True`
# * `palindrome("A Man, A Plan, A Canal-Panama")` → `True`
#
# indice pour ignorer la ponctuation :
#
# ```python
# In [1]: import string
#
# In [2]: string.punctuation
# Out[2]: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# ```

# %% [markdown]
# ### un peu moins simple
#
# même exercice, mais on veut aussi voir pourquoi :
#
# par exemple:
#
# * quand le mot est un palindrome
#
# ```python
# >>> display_palindrome("kayak")
# kayak
# kayak
# OK
# ```
#
# * quand il n'en est pas un
#
# ```python
# >>> display_palindrome("follet")
# follet
# tellof
# ^^  ^^
# ```
#
# pour cette variante on suppose que le mot ne contient pas de ponctuation

# %% [markdown]
# ***

# %% [markdown]
# ## gravity flip
#
# https://www.codewars.com/kata/5f70c883e10f9e0001c89673

# %% [markdown]
# ***

# %% [markdown]
# ## les files de supermarché
#
# https://www.codewars.com/kata/57b06f90e298a7b53d000a86

# %% [markdown]
# ***

# %% [markdown]
# ## le mot le plus long

# %% [markdown]
# ### chercher un des plus longs mots
#
# écrire une fonction qui prend en paramètre un nom de fichier, et retourne le mot le plus long trouvé dans le fichier
#
# on prendra soin de se débarrasser de la ponctuation, et pour cela un indice:

# %%
from string import punctuation
punctuation

# %% [markdown]
# ### variante
#
# écrire une variante qui retourne la liste de tous les mots les plus longs dans le fichier

# %% [markdown]
# ### fichiers d'entrée
#
# vous pouvez utiliser par exemple les 3 fichiers `hhgg-1.txt` .. `hhgg-3.txt`
#
# dans le troisième les mots les plus longs sont
# ```python
# ['Rickmansworth',
#  'controversial',
#  'philosophical',
#  'civilizations',
#  'extraordinary']
# ```

# %% [markdown]
# ***

# %% [markdown]
# ## scanner de fichiers
#
# écrivez une fonction qui, en partant d'un dossier de votre ordinateur, calcule la profondeur maximale des fichiers qui s'y trouvent
#
# exemple de session:
# ```bash
# python filescanner.py /Users/tparment/git
# depth 22 found with /Users/tparment/git/ue22-p21-web-intro/microapps/microexpo/node_modules/react-native/ReactAndroid/src/main/libraries/fbcore/src/main/java/com/facebook/common/logging/BUCK
# ```
