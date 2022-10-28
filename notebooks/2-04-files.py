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
#     title: fichiers
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

# %% language="python"
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python/main/notebooks/_static/style.html")

# %% [markdown]
# # les fichiers

# %% [markdown] slideshow={"slide_type": "slide"}
# * lire et écrire un fichier est très facile en Python
# * ouvrir un fichier pour créer un objet "fichier"
# * `open('mon_fichier.txt', 'r')`
#   * `'r'` ouvre le fichier en lecture (défaut),
#   * `‘w’` en écriture,
#   * `‘a’` en écriture à la suite (*append*),

# %% [markdown] slideshow={"slide_type": "slide"}
# ## utilisez un `with`

# %% [markdown]
# * prenez l'habitude de **toujours utiliser un context manager**
# * **pas besoin de fermer** le fichier ici

# %%
# on n'a pas encore étudié l'instruction with
# mais je vous conseille de toujours procéder comme ceci

# avec with on n'a pas besoin de fermer le fichier
with open('temporaire.txt', 'w') as f:
    for i in 10, 20, 30:
        print(f"{i} {i**2}", file=f)

# %%
# on triche un peu pour regarder le contenu
# du fichier qu'on vient de créer

# !cat temporaire.txt

# %% [markdown] slideshow={"slide_type": "slide"}
# ## lecture avec `for`

# %% [markdown]
# * l'objet fichier est un **itérable** lui-même
# * on peut faire un `for` dessus
# * **attention** toutefois, chaque ligne  
#   va contenir un caractère `"\n"` de fin de ligne

# %% cell_style="split"
# lire un fichier texte 
# ligne par ligne
# c'est compact et lisible !

# remarquez aussi:
# open() sans le mode ⇔ open('r')

with open('temporaire.txt') as f:
    for line in f:
        print(f"-- {line}", end='')

# %% cell_style="split"
# si on ne fait rien
# on obtient 2 fins de ligne
# (i.e. une ligne blanche)

with open('temporaire.txt') as f:
    for line in f:
        print(f"-- {line}") 

# %% [markdown] cell_style="split"
# <div class="note">
#     
# **Précision**
#
# * `print(...)` ajoute une fin de ligne
# * `print(..., end="")` évite cet ajout automatique
#     
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fichiers texte ou binaire

# %% [markdown]
# * parfois utile d'ouvrir un fichier en binaire  
#   par ex. un exécutable, un fichier dans un format propriétaire
#
# * ajouter `'b'` au mode pour ouvrir **en binaire**
#   * pas de décodage
#   * travaille alors à base de **`bytes`** et non de `str`

# %% cell_style="center" slideshow={"slide_type": "slide"}
# on part d'une chaine avec des accents
text = "noël en été\n"

# rappelez vous la section sur Unicode
# j'ai besoin d'un objet bytes
# j'encode mon str en un bytes
binaire = text.encode(encoding="utf-8")

type(binaire), binaire

# %% cell_style="center"
# remarquez le 'b' dans le mode d'ouverture

with open('temporaire.bin', 'wb') as out_file:
    # je peux du coup écrire un objet bytes
    out_file.write(binaire)

# %%
# !cat temporaire.bin

# %% slideshow={"slide_type": "slide"}
# pareil en lecture, le mode avec un 'b'
# va faire que read() retourne un objet bytes

with open('temporaire.bin', 'rb') as in_file:
    binaire2 = in_file.read()

# %% slideshow={"slide_type": ""}
# et donc on retombe bien sur nos pieds
binaire2 == binaire

# %%
# ça aurait été pareil 
# si on avait ouvert le fichier en mode texte
# puisque ce qu'on a écrit dans le fichier binaire,
# c'est justement l'encodage en utf-8 d'un texte

#             sans le b ici ↓↓↓
with open('temporaire.bin', 'r') as feed:
    text2 = feed.read()
    
text2 == text

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## le module `pathlib`

# %% [markdown] slideshow={"slide_type": "-"}
# ### objectifs
#
# * simplifier la gestion des noms de fichier 
#   * pour rendre le code plus concis
#   * et donc plus lisible
#   * sous-titre: *object-oriented filesystem paths*
#   
# * capable de 
#   * ouvrir les fichiers
#   * savoir si le fichier existe, si c'est un dossier...
#   * accéder aux métadata (taille, date)
#   * parcourir un dossier par pattern-matching
#   * ...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un exemple

# %% cell_style="split"
# savoir si un chemin correspond à un dossier
from pathlib import Path

tmp = Path("temporaire.txt")

if tmp.is_file():
    print("c'est un fichier")

# %% cell_style="split"
# donc on peut l'ouvrir

with tmp.open() as feed:
    for line in feed:
        print(line, end="")

# %% [markdown]
# ### construire un objet `Path`

# %% cell_style="split"
# un chemin absolu
prefix = Path("/etc")

# le chemin absolu du directory courant
dot = Path.cwd()

# ou du homedir
home = Path.home()

# un nom de ficher
filename = Path("apache")

# %% cell_style="split"
# par exemple le répertoire courant est

dot

# %% [markdown] slideshow={"slide_type": "slide"}
# ### l'opérateur `/`

# %% [markdown]
# un exemple intéressant de surcharge d'opérateur - ici `/`  
# selon le type de ses opérandes, `/` fait .. ce qu'il faut  
# par exemple ici on ne fait pas une division !

# %% cell_style="center"
# Path / Path -> Path bien sûr
type(prefix / filename)

# %% cell_style="split" slideshow={"slide_type": "slide"}
# Path / str -> Path
type(prefix / "apache2")

# %% cell_style="split"
# str / Path -> Path
type("/etc" / Path("apache2"))

# %%
# mais bien sûr str / str -> TypeError
try:
    "/etc" / "apache2"
except Exception as e:
    print("OOPS", e)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### calculs sur les chemins

# %% [markdown] cell_style="split"
# j'ai créé un petite hiérarchie de fichiers dans le dossier `filepath-globbing` qui ressemble à ceci

# %% [markdown] cell_style="split"
# ![](media/filepath-globbing.png)

# %% slideshow={"slide_type": "slide"}
# pour commencer, voilà comment on peut trouver son chemin absolu

globbing = Path("filepath-globbing")
absolute = globbing.absolute()
absolute

# %%
# si on a besoin d'un str, comme toujours il suffit de faire
str(absolute)

# %%
# les différents morceaux de ce chemin absolu
absolute.parts

# %% cell_style="split"
# juste le nom du fichier, sans le chemin
absolute.name

# %% cell_style="split"
# le chemin, sans le nom du fichier
absolute.parent

# %%
# tous les dossiers parent

list(absolute.parents)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pattern-matching

# %% cell_style="center" slideshow={"slide_type": ""}
# est-ce que le nom de mon objet Path 
# a une certaine forme ?

absolute.match("**/notebooks/*")

# %%
absolute.match("**/*globbing*")

# %% [markdown] slideshow={"slide_type": "slide"} cell_style="split"
# #### pattern-matching - dans un dossier
# ![](media/filepath-globbing.png)

# %% cell_style="split" slideshow={"slide_type": ""}
# à présent c'est plus intéressant
# avec des chemins relatifs
globbing = Path("filepath-globbing")

# tous les fichiers / répertoires 
# qui sont immédiatement dans le dossier
list(globbing.glob("*"))

# %% cell_style="split"
# les fichiers/dossiers immédiatement dans le dossier
# et dont le nom se termine par un chiffre
list(globbing.glob("*[0-9]"))

# %% [markdown] slideshow={"slide_type": "slide"} cell_style="split"
# #### pattern-matching - dans tout l'arbre
# ![](media/filepath-globbing.png)

# %% cell_style="split"
# ce dossier, et les dossiers en dessous
# à n'importe quel étage
list(globbing.glob("**"))

# %% cell_style="split"
# tous les fichiers/dossiers 
# dont le nom termine par un chiffre
list(globbing.glob("**/*[0-9]"))
