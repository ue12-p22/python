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
#     title: "expressions r\xE9guli\xE8res"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat

# %% language="python"
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python/main/notebooks/_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # expressions régulières

# %% [markdown]
# * notion transverse aux langages de programmation
# * présente dans la plupart d'entre eux
# * en particulier historiquement Perl  
#   qui en avait fait un *first-class citizen*

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples

# %% [markdown] slideshow={"slide_type": ""}
# * `a*` décrit tous les mots  
#   composés **de 0 ou plusieurs** `a`
#
#   * `''`, `'a'`, `'aa'`, …  
#     sont les mots reconnus 
#
# * `(ab)+` : toutes les suites de  
#   **au moins 1 occurrence** de `ab`  
#
#   * `'ab'`, `'abab'`, `'ababab'`, …  
#     sont les mots reconnus

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le module `re`

# %% [markdown] slideshow={"slide_type": ""}
# en Python, les expressions régulières sont accessibles au travers du module `re`

# %%
import re

# en anglais on dit pattern
# en français on dit filtre, 
# ou encore parfois motif
pattern = "a*"

# la fonction `match` 
re.match(pattern, '')

# %% cell_style="split"
re.match(pattern, 'a')

# %% cell_style="split"
re.match(pattern, 'aa')

# %% cell_style="split"
re.match('(ab)+', 'ab')

# %% cell_style="split"
# pas conforme : retourne None
re.match('(ab)+', 'ba')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `re.match()`

# %% [markdown] slideshow={"slide_type": ""}
# * **ATTENTION** car `re.match()` vérifie si l'expression régulière peut être trouvée **au début** de la chaine

# %% cell_style="center"
# ici seulement LE DÉBUT du mot est reconnu

match = re.match('(ab)+', 'ababzzz')
match

# %% cell_style="split"
# commence au début 
match.start()

# %% cell_style="split"
# mais pas jusque la fin
match.end()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `re.search()`

# %% [markdown] slideshow={"slide_type": ""}
# * `re.search()` cherche la première occurrence de l'expression régulière  
# * **pas forcément** au début de la chaine

# %% cell_style="center"
# match répond non car seulement LE DÉBUT de la chaine est essayé

re.match('abzz', 'ababzzz')

# %% cell_style="center"
# un use case pour le "walrus operator"
# i.e. une affectation mais qui est aussi une expression

if (match := re.search('abzz', 'ababzzz')):
    print(f"{match.start()=}, {match.end()=}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### les objets `Match`

# %% [markdown] slideshow={"slide_type": ""}
# * le résultat de `re.match()` est de type `Match` 
# * pour les détails de ce qui a été trouvé  
#   (par exemple quelle partie de la chaine)
#
# * et aussi les sous-chaines  
#   correspondant aux **groupes**  
#   (on en reparlera)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### autres façons de chercher

# %% [markdown] slideshow={"slide_type": ""}
# * `re.findall()` et `re.finditer()` pour trouver toutes les occurences du filtre dans la chaine
# * `re.sub()` pour remplacer …
#
# **notre sujet**
#
# * ici nous nous intéressons surtout à la façon de **construire les regexps**
# * se reporter à [la documentation du module](https://docs.python.org/3/library/re.html) pour ces variantes

# %% [markdown] slideshow={"slide_type": "slide"}
# #### pour visualiser

# %%
# digression : un utilitaire pour montrer
# le comportement d'un pattern / filtre

def match_all(pattern, strings):
    """
    match a pattern against a set of strings and shows result
    """
    col_width = max(len(x) for x in strings) + 2 # for the quotes
    for string in strings:
        string_repr = f"'{string}'"
        print(f"'{pattern}' ⇆ {string_repr:<{col_width}} → ", end="")
        match = re.match(pattern, string)
        if not match:
            print("NO")
        elif match.end() != len(string):
            # start() is always 0
            print(f"BEGINNING ONLY (until {match.end()})")
        else:
            print("FULL MATCH")


# %% cell_style="center"
match_all('(ab)+', ['ab', 'abab', 'ababzzz', ''])

# %% [markdown] slideshow={"slide_type": "slide"}
# ## construire un pattern

# %% [markdown] slideshow={"slide_type": "slide"}
# ### n'importe quel caractère : `.`

# %%
match_all('.', ['', 'a', '.', 'Θ', 'ab'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### filtrer **un seul** caractère : `[..]`

# %% [markdown] slideshow={"slide_type": ""}
# * avec les `[]` on peut désigner un **ensemble** de caractères :
# * `[a-z]` les lettres minuscules
# * `[a-zA-Z0-9_]` les lettres et chiffres et underscore

# %% cell_style="split"
match_all('[a-z]', ['a', '', '0'])

# %% cell_style="split" slideshow={"slide_type": ""}
match_all('[a-z0-9]', ['a', '9', '-'])

# %% cell_style="center"
# pour insérer un '-', le mettre à la fin
# sinon ça va être compris comme un intervalle
match_all('[0-9+-]', ['0', '+', '-', 'A'])

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ### idem mais à l'envers : `[^..]`

# %% [markdown] cell_style="split"
# * si l'ensemble de caractères entre `[]` commence par un `^`
# * cela désigne le **complémentaire** dans l'espace des caractères

# %% cell_style="split"
# complémentaires
match_all('[^a-z]', ['a', '0', '↑', 'Θ'])

# %% cell_style="split"
match_all('[^a-z0-9]', ['a', '9', '-'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### 0 ou plusieurs occurrences : `..*`

# %% cell_style="split"
match_all('[a-z]*', ['', 'cba', 'xyz9'])

# %% cell_style="split"
match_all('(ab)*', ['', 'ab', 'abab'])

# %% [markdown] slideshow={"slide_type": ""}
# ### 1 ou plusieurs occurrences : `..+`

# %% cell_style="split"
match_all('[a-z]+', ['', 'cba', 'xyz9'])

# %% cell_style="split"
match_all('(ab)+', ['', 'ab', 'abab', 'ababba9'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### concaténation
#
# quand on concatène deux filtres, la chaine doit matcher l'un puis l'autre

# %% cell_style="split"
# c'est le seul mot qui matche
match_all('ABC', ['ABC']) 

# %% cell_style="split"
match_all('A*B', ['B', 'AB', 'AAB', 'AAAB']) 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### groupement : `(..)`

# %% [markdown]
# * permet d'appliquer un opérateur sur une regexp
#   * comme déjà vu avec `(ab)+`
# * cela définit un **groupe** qui peut être retrouvé dans le match
#   * grâce à la méthode `groups()`

# %% cell_style="split"
# groupes anonymes
pattern = "([a-z]+)=([a-z0-9]+)"

string = "foo=barbar99"

(match := re.match(pattern, string))

# %% cell_style="split"
# dans l'ordre où ils apparaissent
match.groups()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### alternative : `..|..`

# %% [markdown]
# pour filtrer avec une regexp **ou** une autre :

# %% cell_style="split"
match_all('ab|cd', ['ab', 'cd', 'abcd'])

# %% cell_style="split"
# si besoin, mettez des parenthèses
match_all('ab|cd*', ['ab', 'c', 'cd', 'cdd'])

# %% cell_style="split"
# comme ceci par exemple
match_all('ab|(cd)*', ['ab', 'c', 'cd', 'cdd'])

# %% cell_style="split"
match_all('(ab|cd)*', ['ab', 'c', 'cd', 'cdd', 'abcd'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### 0 ou 1 occurrences : `..?`

# %% cell_style="split"
match_all('[a-z]?', ['', 'b', 'xy'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### nombre d'occurrences dans un intervalle : `..{n,m}`

# %% [markdown]
# * `a{3}` : exactement 3 occurrences de `a`
# * `a{3,6}` : entre 3 et 6 occurrences (inclusivement)
# * `a{3,}` : au moins 3 occurrences
# * `a{,3}` : au plus 3 occurrences

# %% cell_style="center"
match_all('(ab){1,3}', ['', 'ab', 'abab', 'ababab', 'ababababababab'])

# %% cell_style="center"
match_all('(ab){,3}', ['', 'ab', 'abab', 'ababab', 'ababababababab'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### classes de caractères

# %% [markdown] slideshow={"slide_type": ""}
# raccourcis qui filtrent **un caractère** dans une classe  
# définis en fonction de la configuration de l'OS en termes de langue
#
# * `\s` (pour Space) : exactement un caractère de séparation (typiquement Espace, Tabulation, Newline)
# * `\w` (pour Word) : exactement un caractère alphabétique ou numérique
# * `\d` (pour Digit) : un chiffre
# * `\S`, `\W` et `\D` : les complémentaires

# %% cell_style="split"
match_all('\w+', ['eFç0', 'été', ' ta98'])

# %% cell_style="split"
match_all('\s?\w+', ['eFç0', 'été', ' ta98'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### groupe nommé : `(?P<name>..)`

# %% [markdown] slideshow={"slide_type": ""}
# * le même effet que les groupes anonymes créés avec les `()`
# * mais on peut retrouver le contenu depuis le nom du groupe
# * plutôt que le rang (numéro) du groupe
#   * qui peut rapidement devenir une notion fragile / peu maintenable

# %% cell_style="center"
# groupes nommés
pattern = "(?P<variable>[a-z]+)=(?P<valeur>[a-z0-9]+)"

string = "foo=barbar99"

match = re.match(pattern, string)
match

# %% cell_style="split"
match.group('variable')

# %% cell_style="split"
match.group('valeur')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### début et fin de chaine : `^` et `$`

# %% cell_style="center"
match_all('ab|cd', ['ab', 'abcd'])

# %%
# pour forcer la chaine à matcher jusqu'au bout
# on ajoute un $ 
match_all('(ab|cd)$', ['ab', 'abcd'])

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### plusieurs occurrences du même groupe : `(?P=name)`

# %% [markdown] slideshow={"slide_type": ""} tags=["level_intermediate"]
# on peut spécifier qu'un groupe doit apparaître plusieurs fois

# %% tags=["level_intermediate"]
# la deuxième occurrence de <nom> doit être la même que la première
pattern = '(?P<nom>\w+).*(?P=nom)'

string1 = 'Jean again Jean'
string2 = 'Jean nope Pierre'
string3 = 'assez comme ça'

match_all(pattern, [string1, string2, string3])

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour aller plus loin

# %% [markdown] slideshow={"slide_type": ""}
# * beaucoup d'autres possibilités
#
# * testeurs en ligne  
#   <https://pythex.org>  
#   <https://regex101.com/> (bien choisir Python)
#
# * un peu de détente, avec ce jeu de mots croisés basé sur les regexps 
#   <https://regexcrossword.com>  
#   commencer [par le tutorial](https://regexcrossword.com/challenges/tutorial/puzzles/1)
#
# * tour complet de la syntaxe des regexps  
#   <https://docs.python.org/3/library/re.html#regular-expression-syntax>
