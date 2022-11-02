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
#     title: chaines et binaire
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
# # chaines et binaire (`str` et `bytes`)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## rappels

# %% [markdown] cell_style="split"
# ### les séquences
#
# * suite finie et ordonnée d'objets
# * du coup indexable `seq[n]`
# * indices **commencent à 0**
# * peuvent contenir des duplications

# %% [markdown] cell_style="split"
# ### mutable et immutable
#
# * mutable
#   * `list`, `bytearray`
# * immutable
#   * `str`, `bytes`, `tuple`, `range`

# %% [markdown]
# un chaine - de type `str` - est une **séquence immutable**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérations sur (toutes) les séquences

# %% [markdown] cell_style="split"
# * `S[i]`
#   * retourne l’élément d'indice i
# * `len(S)` 
#   * donne la taille en nombre d’éléments

# %% [markdown] cell_style="split"
# * `S + T`
#  * retourne une nouvelle séquence qui est la concaténation de S et T
# * `S*n` ou `n*S`
#   * retourne une nouvelle séquence qui est la concaténation de n *shallow* copies de S

# %% [markdown] slideshow={"slide_type": "slide"}
# #### opérations sur les séquences...

# %% [markdown] slideshow={"slide_type": ""} cell_style="split"
# * `x in S` - selon les types:
#  * `True` si un élément de S  
#    est égal à x (e.g. `list`)
#
#  * **`True` si S contient x**  
#    c'est le cas pour `str`  
#    on cherche *une sous-chaine*

# %% [markdown] slideshow={"slide_type": ""} cell_style="split"
# * `S.index(a)`
#   * retourne l’indice de la première occurrence de a dans S
# * `S.count(a)`
#   * retourne le nombre d’occurrences de a dans S

# %% [markdown] slideshow={"slide_type": "slide"}
# ### slicing

# %% [markdown]
# * `S[i:j]` retourne 
#   * une nouvelle séquence de même type
#   * contenant tous les éléments de l’indice i à l’indice j-1
# * `S[i:j:k]` retourne
#   * une nouvelle séquence de même type
#   * prenant tous les éléments de l’indice i à l’indice j-1, par sauts de k éléments

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# <img src="media/egg-bacon.png"/>

# %% [markdown] cell_style="split"
# #### *slicing*

# %% [markdown] cell_style="split"
# * on peut compter du début ou de la fin
# * on peut omettre les bornes

# %% cell_style="split"
s = "egg, bacon"
s[0:3]

# %% cell_style="split"
# si on omet une borne 
# ce sera le début ..
s[:3]

# %% cell_style="split"
# ... ou la fin:
s[5:]

# %% cell_style="split"
# les indices peuvent être négatifs
s[-3:10]

# %%
# tout entier: une shallow-copy
s[:]

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# <img src="media/egg-bacon-bornes.png" text-align="center">

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# #### les bornes

# %% [markdown] cell_style="split"
# La convention est choisie pour pouvoir facilement encastrer les slices:

# %% cell_style="split"
s[0:3]

# %% cell_style="split"
s[3:6]

# %% cell_style="split"
s[6:]

# %% cell_style="split"
s[0:3] + s[3:6] + s[6:] == s

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# <img src="media/egg-bacon.png" text-align="center">

# %% [markdown] cell_style="split"
# #### le pas

# %% [markdown] cell_style="split"
# * on peut préciser un pas
# * peut aussi être négatif
# * ou omis (défaut 1)

# %% cell_style="split"
s[0:10:2]

# %% cell_style="split"
s[::2]

# %% cell_style="split"
s[:8:3]

# %% cell_style="split"
s[-2::-3]

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# <img src="media/egg-bacon.png" text-align="center">

# %% [markdown] cell_style="split"
# #### pas d'exception

# %% [markdown] cell_style="split"
# les slices ont un comportement plus permissif que l'indexation

# %%
# Si j'essaie d'utiliser un index inexistant
try: s[100]
except Exception as e: print("OOPS", e)

# %% cell_style="split"
# par contre avec un slice, pas de souci
s[5:100]

# %% cell_style="split"
# vraiment..
s[100:200]

# %% [markdown] slideshow={"slide_type": "slide"}
# <img src="media/egg-bacon.png" text-align="center">

# %% cell_style="split"
s[-1]

# %% cell_style="split"
s[-3:-1]

# %% cell_style="split"
s[:-3]

# %% cell_style="split"
s[::-1]

# %% cell_style="split"
# le 2 est inclus et le 0 exclus
s[2:0:-1]

# %% cell_style="split"
s[2::-1]

# %% [markdown] slideshow={"slide_type": "slide"}
# #### slicing, formes idiomatiques

# %%
s = [1, 2, 3]

# %% cell_style="split"
# une copie simple
s[:]

# %% cell_style="split"
# copie renversée
s[::-1]

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `str` et `bytes`

# %% [markdown]
# * deux cas particuliers de **séquences**
#   * `str` pour manipuler **du texte**
#   * `bytes` pour manipuler **de la donnée brute** (des octets)
#   
# * **ATTENTION**
#   * les caractères alphanumériques sans accent  
#     et la ponctuation tiennent sur 1 octet (ASCII)  
#
#   * mais **ce n'est pas le cas** en général

# %% [markdown] slideshow={"slide_type": "slide"}
# ## chaînes de caractères `str`

# %% [markdown]
# * un cas particulier de séquence
# * une chaîne de caractères est définie de manière équivalente par des simples ou doubles guillemets (`'` ou `"`)
# * on peut ainsi facilement inclure un guillemet

# %% cell_style="split"
# une chaine entre double quotes
# pas de souci pour les accents 
print("c'est l'été")

# %% cell_style="split"
# entre simple quotes
print('on se dit "pourquoi pas"')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### construire une chaîne

# %% cell_style="split"
s = "l'hôtel"
print(s)

# %% cell_style="split"
s = 'une "bonne" idée'
print(s)

# %% cell_style="split"
s = """une très longue phrase
avec saut de ligne"""
print(s)

# %% cell_style="split"
s = '  un backslash \\ un quote \' ' 
print(s)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérations sur les `str`
#
# * toutes les opérations des séquences

# %% cell_style="split"
s1 = 'abcdéfg'
s2 = 'bob'
len(s1)

# %% cell_style="split"
# concaténation
s1 + s2

# %% cell_style="split"
s1[-1::-2]

# %% cell_style="split"
'=' * 30

# %% [markdown] slideshow={"slide_type": "slide"}
# #### opérations sur les `str` ...

# %% cell_style="split"
s1

# %% cell_style="split"
'x' in s1

# %% cell_style="split"
'cdé' in s1

# %% cell_style="split"
s1.index('cdé')

# %% [markdown] slideshow={"slide_type": "slide"}
# #### opérations sur les `str` ...

# %% [markdown]
# * par contre **ATTENTION** un `str` n'est **pas mutable**

# %%
try: 
    s1[2] = 'x'
except TypeError as e:
    print("OOPS", e, type(e))    

# %% [markdown] slideshow={"slide_type": "slide"}
# ### formatage des chaînes : f-strings

# %% [markdown] cell_style="split"
# * depuis Python-3.6
# * utilisez les ***f-strings***
# * qui évitent les répétitions fastidieuses

# %% [markdown] cell_style="split"
# * entre `{` et `}` : **du code** 
# * embarqué directement dans le format
# * n'importe quelle expression

# %% cell_style="split"
import math

# %% cell_style="split"
nom, age = "Pierre", 42

# %% cell_style="split"
f"{nom} a {age} ans"

# %% cell_style="split"
f"360° = {2*math.pi} radians"

# %% [markdown] slideshow={"slide_type": "slide"}
# #### formatage des chaînes de caractères

# %% [markdown] slideshow={"slide_type": ""}
# ![](media/f-string.png)

# %%
print(f"ᴨ arrondi à deux décimales = {math.pi:.2f}")

# %% [markdown] slideshow={"slide_type": "slide"}
# #### formats - scientifiques

# %% [markdown]
# formats scientifiques usuels: `e` `f` et `g`, cf. `printf`

# %%
x = 23451.23423536563
f'{x:e} | {x:f} | {x:g} | {x:010.1f} | {x:.2f}'

# %%
y = 769876.11434
f'{y:e} | {y:f} | {y:g} | {y:010.2f} | {y:.2f}'

# %% [markdown]
# voir aussi pour plus de détails:  
# <https://mkaz.blog/code/python-string-format-cookbook/>

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `f"{x=}"` dans Python 3.9

# %% [markdown]
# depuis la version 3.9, on peut utiliser cette astuce  
# qui est assez pratique pour le debugging:
#
# pour ne pas avoir à répéter l'expression deux fois  
# il suffit de terminer la partie *expression*  
# dans le f-string par le signe `=`

# %% cell_style="split"
# avec 3.8 on écrirait ceci
print(f"math.pi={math.pi}")

# %% cell_style="split"
# en 3.9 plus besoin de répéter
# en ajoutant   ↓   
print(f"{math.pi=}")
# on obtient en sortie le texte
#↓↓↓↓↓↓

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# #### formats pour f-string : justification

# %% [markdown]
# justification: formats `<` `ˆ` et `>`

# %%
f"|{nom:<12}|{nom:^12}|{nom:>12}|"

# %%
# on peut aussi préciser avec quel caractère remplir
num = 123
f"|{num:<12}|{num:-^12}|{num:0>12}|"

# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes sur les `str`

# %% [markdown]
# * de nombreuses méthodes disponibles

# %%
s = "une petite phrase"
s.replace('petite', 'grande')

# %% cell_style="split"
s.find('hra')

# %% cell_style="split"
s[12:15]

# %%
liste = s.split()
liste

# %% [markdown] slideshow={"slide_type": "slide"}
# #### sur les `str` : `split()` et `join()`

# %%
liste

# %% cell_style="split"
"".join(liste)

# %% cell_style="split"
" ".join(liste)

# %%
"_".join(liste)

# %% cell_style="split"
s2 = "_".join(liste)
s2

# %% cell_style="split"
s2.split('_')

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `str` *vs* `bytes`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### contenus binaires et textuels

# %% [markdown] slideshow={"slide_type": ""}
# * toutes les données ne sont pas textuelles
#   * exemple: fichiers exécutables comme `cmd.exe`
#   * stockage de données propriétaires (.doc, .xls, ...)
# * dès qu'on utilise des données textuelles,
#   * on décode une suite de bits
#   * il faut leur **donner un sens**
#   * c'est l'**encodage** qui nous dit comment faire

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le problème

# %% [markdown]
# * dès que vous échangez avec l'extérieur, i.e.
#   * Internet (Web, mail, etc.)
#   * stockage (disque dur, clef USB)
#   * terminal ou GUI, etc..
# * vous traitez en fait des flux **binaires**
#   * et donc vous êtes confrontés à l'encodage des chaines
#   * et notamment en **présence d'accents**
#   * ou autres caractères non-ASCII

# %% [markdown] slideshow={"slide_type": "slide"}
# ### codage et décodage en python

# %% [markdown] cell_style="split"
# * le type `bytes` correspond,  
#   comme son nom l'indique,  
#   à une suite d'**octets**
#
#   * dont la signification  
#    (le décodage) est à la  
#    charge du programmeur
#
# * ce qui **n'est pas du tout**  
#   le cas du type `str`
#
#   * décodage fait par Python
#   * le programmeur choisit un  
#     encodage (défaut UTF-8)

# %% [markdown] slideshow={"slide_type": ""} cell_style="split"
# ![](media/str-bytes.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Unicode

# %% [markdown]
# * ***une*** liste des caractères 
#   * avec **chacun un *codepoint*** - un nombre entier unique (*)
#   * de l'ordre de 145.000 en sep. 2021 (v14.0) *and counting...*
#   * limite théorique 1,114,112 caractères
#
# * ***trois*** encodages:
#     * **UTF-8**: taille variable 1 à 4 octets, **compatible ASCII**
#     * UTF-32: taille fixe, 4 octets par caractère
#     * UTF-16: taile variable, 2 ou 4 octets
#     
# <div class="note">
#     (*) le modèle mental "1 caractère = 1 codepoint" est une simplification
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### l'essentiel sur UTF-8
#
# * c'est l'encodage le plus répandu aujourd'hui 
#   * la famille des ISO-latin et autres cp1252  
#     sont **à proscrire absolument**
#
#   * en 2021, c'est de moins en moins un souci
#
# * avec UTF-8, les caractères usuels (dits ASCII),   
#   sans accent, **sont codés sur 1 octet**
#
# * mais ce n'est pas le cas en général :
#   * les caractères **accentués** européens  
#     sont codés sur **2 octets**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### digression: notation hexadécimale
#
# ![](media/hexadecimal.png)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### UTF-8 illustré

# %% [markdown] slideshow={"slide_type": ""}
# le codepoint du caractère `è` est `0xe8` c'est-à-dire `232` 
#
# ![](media/unicode-table.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# voici le flux binaire correspondant à la chaine `"été\n"`
#
# ![](media/unicode-decode-example.png)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_advanced"]
# ### UTF-8 - le codage

# %% [markdown]
# * le nombre d'octets utilisé pour encoder un caractère dépend
#   * du caractère et de l'encodage
# * texte ASCII : identique en UTF-8
#   * en particulier, ne prennent qu'un octet

# %% [markdown] slideshow={"slide_type": ""}
# ![](media/unicode-utf8-areas.png)

# %% [markdown] slideshow={"slide_type": "slide"} hide_input=true
# ## UTF-8 et Python: `encode` et `decode`

# %% cell_style="split"
text = 'été\n'
type(text)

# %% cell_style="split"
# on compte les 
# caractères 

len(text)

# %% cell_style="split"
binaire = text.encode(encoding="utf-8")
for b in binaire:
    print(f"{b:02x}", end=" ")

# %% cell_style="split"
# ici par contre on
# compte les octets

len(binaire)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Unicode et Python: `chr` et `ord`

# %% [markdown] cell_style="split"
# ![](media/unicode-e-accent.png)

# %% cell_style="split"
# le codepoint du é accent aigu
codepoint = 0xe9
codepoint

# %% cell_style="split"
character = chr(codepoint)
character

# %% cell_style="split"
# dans l'autre sens
ord(character)

# %% cell_style="split"
# toujours vrai
ord(chr(codepoint)) == codepoint

# %% cell_style="split"
# toujours vrai
chr(ord(character)) == character

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pourquoi l’encodage c’est souvent un souci ?

# %% [markdown]
# * chaque fois qu'une application écrit du texte dans un fichier
#   * elle utilise un encodage
# * cette information (quel encodage?) est **parfois** disponible
#   * dans ou avec le fichier (ex. `# -*- coding: utf-8 -*-`)
#   * HTTP headers pour le web
#   * MIME extensions pour le mail
# * mais le plus souvent on ne peut pas sauver cette information
#   * pas prévu dans le format
#   * il faudrait des **métadata**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pourquoi l’encodage c’est souvent un souci ?

# %% [markdown]
# * du coup on utilise le plus souvent des heuristiques
#   * ex: un ordinateur (OS) configuré pour `cp-1252`
#   * applications qui utilisent l'encodage défini pour tout l'ordi
# * c'est comme ça qu'on reçoit des mails comme
#   * `j'ai Ã©tÃ© reÃ§u Ã\xa0 l'Ã©cole`
#   * au lieu de
#   * `j'ai été reçu à l'école`
# * sans parler des polices de caractères..

# %% cell_style="center" slideshow={"slide_type": "slide"}
# Jean écrit un mail
envoyé = "j'ai été reçu à l'école"

# %% cell_style="center" slideshow={"slide_type": ""}
# son OS l'encode pour le faire passer sur le réseau
binaire = envoyé.encode(encoding="utf-8")

# %% slideshow={"slide_type": ""}
# Pierre reçoit le binaire
# mais se trompe d'encodage 
# au moment de le décoder
reçu = binaire.decode(encoding="cp1252")

# %% slideshow={"slide_type": ""}
# Pierre voit ceci dans son mailer
reçu
