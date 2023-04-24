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
#     title: 'Exercice: Taylor'
# ---

# %% [markdown]
# # TP: Taylor illustré

# %% [markdown]
# ## exercice

# %% [markdown]
# En guise d'application de ce qu'on a vu jusqu'ici, je vous invite à réaliser une visualisation
# du théorème de Taylor; je vous renvoie à votre cours d'analyse, [ou à wikipedia](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Taylor) pour une présentation détaillée de ce théorème, mais ce que nous en retenons se résume à ceci.
#
#
# On peut approximer une fonction "suffisamment régulière" - disons $C^\infty$ pour fixer les idées - par un polynôme d'ordre $n$, dont les coefficients dépendent uniquement des $n$ dérivées successives au voisinage d'un point :
#
# $$f_n(x) = \sum_{i=0}^{n}\frac{f^{(i)}(0).x^i}{i!}$$
#
# Sans perte de généralité nous avons ici fixé le point de référence comme étant égal à 0, il suffit de translater $f$ par changement de variable pour se ramener à ce cas-là.
#
# Le théorème de Taylor nous dit que la suite de fonctions $(f_n)$ converge vers $f$.

# %% [markdown]
# On pourrait penser - c'était mon cas la première fois que j'ai entendu parler de ce théorème - que l'approximation est valable **au voisinage de 0** seulement; si on pense en particulier à **sinus**, on peut accepter l'idée que ça va nous donner une période autour de 0 peut-être.
#
# En fait, c'est réellement bluffant de voir que ça marche vraiment incroyablement bien et loin.

# %% [markdown]
# ## mon implémentation

# %% [markdown]
# Je commence par vous montrer **seulement le résultat** de l'implémentation que j'ai faite.
#
# Pour calculer les dérivées successives j'utilise la librairie `autograd`.
#
# Ce code est relativement générique, vous pouvez visualiser l'approximation de Taylor avec une fonction que vous passez en paramètre - qui doit avoir tout de même la bonne propriété d'être vectorisée, et d'utiliser la couche `numpy` exposée par `autograd` :

# %% [markdown]
# **ATTENTION** c'est crucial d'**importer `autograd.numpy`** et pas le `numpy` "de base"

# %%
# to compute derivatives
import autograd
import autograd.numpy as np

# %% [markdown]
# Sinon pour les autres dépendances, j'ai utilisé les `ipywidgets` et `bokeh`

# %%
from math import factorial

from ipywidgets import interact, IntSlider, Layout

# %%
from bokeh.plotting import figure, show
from bokeh.io import push_notebook, output_notebook

output_notebook()


# %% [markdown]
# ### la classe `Taylor`

# %% [markdown]
# J'ai défini une classe `Taylor`, je ne vous montre pas le code, je vais vous inviter à en écrire une vous même

# %% hide_input=false
from taylor import Taylor


# %% [markdown]
# ### sinus

# %% [markdown]
# Ma classe `Taylor` s'utilise comme ceci : d'abord on crée une instance à partir d'une fonction
# et d'un domaine, i.e. l'intervalle des X qui nous intéresse.

# %%
# between -4π and 4π
DOMAIN = np.linspace(-4*np.pi, 4*np.pi, 250)

# an instance
sinus_animator = Taylor(np.sin, DOMAIN)

# %% [markdown]
# **Remarquez bien** qu'ici la fonction que je passe au constructeur est **en réalité `autograd.numpy.sin`** et non pas `numpy.sin`, vu la façon dont on a défini notre symbole `np` lors des imports (et ça ne marcherait pas du tout avec `numpy.sin`).

# %% [markdown]
# Ensuite on crée un `ipywidget` qui va nous permettre de choisir le degré $n$; dans le cas de **sinus**, qui est **impaire**, les degrés **intéressants** sont **impairs**.

# %%
# the widget to select a degree
sinus_widget = IntSlider(
   min=1, max=33, step=2,        # sinus being odd we skip even degrees
   layout=Layout(width='100%'))  # more convenient with the whole page width

# %% [markdown]
# Pour lancer l'interaction, on n'a plus qu'à :
#
# * afficher le diagramme avec la méthode `display()`; on a besoin pour cela de préciser les bornes en Y, qui resteront constantes au cours de l'animation (sinon la visualisation est vilaine)
#
# puis lancer l'interaction en passant en paramètre le widget qui choisit le degré, ce qui donne :

# %%
# fixed limits in Y
sinus_animator.display((-1.5, 1.5))

sinus_animator.interact(sinus_widget)

# %% [markdown]
# ### cosinus

# %% [markdown]
# La même chose avec cosinus nous donnerait ceci :

# %%
# allows to select a degree
sinus_widget = IntSlider(
   min=0, max=34, step=2,      # only even degrees
   layout=Layout(width='100%'))

### ready to go
sinus_animator = Taylor(np.cos, DOMAIN)
sinus_animator.display((-1.5, 1.5))
sinus_animator.interact(sinus_widget)

# %% [markdown]
# ### exponentielle

# %%
# allows to select a degree
exp_widget = IntSlider(min=0, max=17,
   layout=Layout(width='100%'))

### ready to go
exp_animator = Taylor(np.exp, np.linspace(-1, 10, 200))
exp_animator.display((-15_000, 25000))
exp_animator.interact(exp_widget)

# %% [markdown]
# ## quelques indices

# %% [markdown]
# ### affichage

# %% [markdown]
# Ici j'ai utilisé `bokeh`, mais on peut tout à fait arriver à quelque chose de similaire avec `matplotlib` sans aucun doute

# %% [markdown]
# ### conception

# %% [markdown]
# Ma classe `Taylor` s'inspire très exactement de la technique décrite dans le Complément #6 "Autres bibliothèques de visualisation", et notamment la classe `Animation`, modulo quelques renommages.

# %% [markdown]
# ### calcul de dérivées avec `autograd`

# %% [markdown]
# La seule fonction que j'ai utilisée de la bibliothèque `autograd` est `grad` :

# %%
from autograd import grad

# %%
# dans le cas de sinus par exemple
# les dérivées successives en 0 se retrouvent comme ceci
f = np.sin  # à nouveau cette fonction est autograd.numpy.sin
f(0.)

# %% cell_style="split"
# ordre 1
f1 = grad(f)
f1(0.)

# %% cell_style="split"
# ordre 2
f2 = grad(f1)
f2(0.)


# %% [markdown]
# ## votre implémentation

# %% [markdown]
# Je vous invite à écrire votre propre implémentation, qui se comporte en gros comme notre classe `Taylor`.
#
# Vous pouvez naturellement simplifier autant que vous le souhaitez, ou modifier la signature comme vous le sentez (pensez alors à modifier aussi la cellule de test).
#
# À titre indicatif ma classe `Taylor` fait environ 30 lignes de code utile, i.e. sans compter les lignes blanches, les docstrings et les commentaires.

# %%
# à vous de jouer

class MyTaylor:
    def __init__(self, function, domain):
        ...
    def display(self, y_range):
        # là on veut créer le dessin original, c'est à dire
        # la figure, la courbe de f qui ne chagera plus,
        # et la courbe approchée avec disons n=0 (donc y=f(0))
        ...
    def _update(self, n):
        # modifier la courbe approximative avec Taylor à l'ordre n
        # je vous recommande de créer cette méthode privée
        # pour pouvoir l'appeler dans interact()
        ...
    def interact(self, widget):
        # là clairement il va y avoir un appel à 
        # interact() de ipywidgets
        print("inactive for now")


# %%
# testing MyTaylor on cosinus

sinus_widget = IntSlider(
   min=0, max=34, step=2,      # only even degrees
   layout=Layout(width='100%'))

### ready to go
sinus_animator = MyTaylor(np.cos, DOMAIN)
sinus_animator.display((-1.5, 1.5))
sinus_animator.interact(sinus_widget)
