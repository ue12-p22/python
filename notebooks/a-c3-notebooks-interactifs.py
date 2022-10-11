# -*- coding: utf-8 -*-
# ---
# jupyter:
#   ipub:
#     sphinx:
#       toggle_input: true
#       toggle_input_all: true
#       toggle_output: true
#       toggle_output_all: true
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
#     title: Notebooks interactifs
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# <span><img src="media/inria-25-alpha.png"/></span>
# </div>

# %% [markdown]
# # Notebooks interactifs

# %% [markdown]
# Voyons quelques techniques qui permettent de rendre vos notebooks un peu plus interactifs

# %% [markdown]
# ## `%matplotlib notebook`

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# La bonne façon de créer un graphique matplotlib c'est avec la formule magique suivante :

# %%
# il y a plusieurs sorties possibles pour matplotlib
# et du coup pour choisir la sortie 'notebook':
# %matplotlib notebook

# %% [markdown]
# Avec ce réglage, il y a pas mal de possibilités qui sont très pratiques :
#
# * pour commencer on peut changer la taille de la courbe en cliquant sur le petit coin visible en bas à droite de la figure ![](media/matplotlib-resize.png)
# * les courbes apparaissent avec un barre d'outils en dessous; entraînez-vous à utiliser par exemple **l'outil de zoom**, pour agrandir et vous déplacer dans la courbe ![](media/matplotlib-navigate.png)

# %% [markdown]
# À titre d'exercice, sur cette courbe le **nombre d'or** correspond à une des racines du polynôme  
# à vous de trouver sa valeur avec une précision de, disons, $10^{-5}$
#

# %%
plt.figure(figsize=(2, 2))
X = np.linspace(-2, 2)
ZERO = X * 0
def golden(x):
    return x**2 - x - 1
plt.plot(X, golden(X));
plt.plot(X, ZERO);

# %% [markdown]
# **attention piège**
#
# * confirmez la précision de votre résultat en le réinjectant dans `golden()`
# * comparez avec la valeur exacte du nombre d'or qui est de $\frac{1+\sqrt{5}}{2}$
# * la méthode est-elle satisfaisante, et sinon que faire pour l'améliorer ?
# * **indice**: revoyez le comportement de `np.linspace`

# %% [markdown]
# ## Une visualisation interactive simple : `interact`

# %% [markdown]
# Lorsqu'on explore un sujet, bien souvent on commence par une visualisation un peu grossière, puis ensuite on fait bouger un peu les paramètres.
#
# Mais ça peut devenir rapidement fastidieux de créer des dizaines de visualisation, qui en plus prennent de la place.

# %% [markdown]
# Pour améliorer cela, on préfère créer une seule figure, avec des boutons ou autres gadgets interactifs pour faire varier nos paramètres. Ici nous allons commencer par animer la fonction sinus, avec par exemple un **bouton pour régler la fréquence**. 
#
# Pour cela nous allons utiliser **la fonction `interact`** ; c'est un utilitaire qui fait partie de l'écosystème des notebooks, et plus précisément du module `ipywidgets` :

# %%
from ipywidgets import interact


# %% [markdown] slideshow={"slide_type": "-"}
# Dans un premier temps, j'écris une fonction qui prend en paramètre la fréquence, et qui dessine la fonction sinus sur un intervalle fixe de 0. à $4\pi$ :

# %% slideshow={"slide_type": "slide"}
def sinus(freq):
    X = np.linspace(0., 4*np.pi, 200)
    Y = np.sin(freq*X)
    # needed with %matplotlib notebook
    # to avoid superposition with previous calls
    plt.clf()
    plt.plot(X, Y)


# %% [markdown]
# C'est ma brique de base; juste pour vérifier, je peux l'appeler plusieurs fois de suite avec des paramètres différents

# %% cell_style="split"
plt.figure(figsize=(3, 2))
sinus(1)

# %% cell_style="split"
plt.figure(figsize=(3, 2))
sinus(0.5)

# %% [markdown]
# Maintenant, plutôt que de tracer individuellement les courbes une à une, j'utilise `interact` qui va m'afficher une réglette pour changer le paramètre `freq`. Ça se présente comme ceci :

# %%
# je change maintenant la taille des visualisations
plt.rcParams["figure.figsize"] = (8, 4)

# %%
plt.figure()
interact(sinus, freq=(0.5, 10., 0.25));

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Mécanisme d'`interact`

# %% [markdown]
# La fonction `interact` s'attend à recevoir :
#
# * en **premier argument** : une fonction `f` ;
# * et ensuite autant d'**arguments nommés** supplémentaires que de paramètres attendus par `f`.

# %% [markdown]
# Donc ici
#
# * comme la fonction `sinus` attend **un paramètre** nommé `freq`
# * on appelle `interact` **avec deux paramètre**
#   * le premier étant `sinus`
#   * et le deuxième indiquant dans quel intervalle faire varier le paramètre `freq`

# %% [markdown]
# ### Les objets `Slider`

# %% [markdown]
# Chacun des arguments à `interact` (en plus de la fonction) correspond à un objet de type `Slider` (dans la ménagerie de `ipywidget`). Ici en passant juste le tuple `(0.5, 10., 0.25)` j'utilise un raccourci pour dire que je veux pouvoir régler le paramètre `freq` sur une plage allant de `0.5` à `10` avec un pas de `0.25`.

# %% [markdown]
# Mon premier exemple avec `interact` est en réalité équivalent à ceci :

# %%
from ipywidgets import FloatSlider

# %%
# essentiellement équivalent à la version ci-dessus
# sauf pour la valeur initiale de freq
plt.figure()
interact(sinus, freq=FloatSlider(min=0.5, max=10., step=0.25));

# %% [markdown]
# Mais en utilisant la forme bavarde, je peux choisir davantage d'options, comme notamment :
#
# * mettre `continuous_update = False` ; l'effet de ce réglage, c'est que l'on met à jour la figure seulement lorsque je lâche la réglette (c'est utile lorsque les calculs sont un peu lents)
# * mettre `value=1.` pour choisir la valeur initiale :

# %%
# exactement équivalent à la version ci-dessus
# sauf qu'on ne redessine que lorsque la réglette
# est relâchée
plt.figure()
interact(sinus, freq=FloatSlider(min=0.5, max=10., 
                                 step=0.25, value=1.,
                                 continuous_update=False));


# %% [markdown]
# ### Plusieurs paramètres

# %% [markdown]
# Voyons tout de suite un exemple avec **deux paramètres**, je vais écrire maintenant une fonction qui me permet de changer aussi la phase :

# %%
def sinus2(freq, phase):
    X = np.linspace(0., 4*np.pi, 200)
    Y = np.sin(freq*(X+phase))
    plt.clf()
    plt.plot(X, Y)


# %% [markdown]
# Et donc maintenant je passe à `interact` un **troisième argument** :

# %%
plt.figure()
interact(sinus2,
         freq=FloatSlider(min=0.5, max=10., step=0.5,
                          continuous_update=False),
         phase=FloatSlider(min=0., max=2*np.pi, step=np.pi/6),
        );

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Bouche-trou : `fixed`

# %% [markdown]
# Si j'ai une fonction qui prend plus de paramètres que je ne veux montrer de réglettes, je peux fixer un des paramètres  par exemple comme ceci :

# %%
from ipywidgets import fixed

# %%
# avec une fonction à deux paramètres,
# je peux en fixer un, et n'avoir qu'une réglette
# pour fixer celui qui est libre
plt.figure()
interact(sinus2, 
         freq=fixed(1.),
         phase=FloatSlider(min=0., max=2*np.pi, step=np.pi/6),
        );

# %% [markdown] tags=["level_intermediate"]
# ### `interact` comme un décorateur

# %% [markdown] tags=["level_intermediate"]
# Pour les geeks, signalons qu'on peut aussi utiliser `interact` **comme un décorateur**, c'est-à-dire écrire en une seule passe

# %% tags=["level_intermediate"]
plt.figure()

@interact(freq=FloatSlider(min=0.5, max=10., step=0.5),
          phase=FloatSlider(min=0., max=2*np.pi, step=np.pi/6))
def anonymous(freq, phase):
    X = np.linspace(0., 4*np.pi, 200)
    Y = np.sin(freq*(X+phase))
    plt.clf()
    plt.plot(X, Y)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Widgets

# %% [markdown]
# Il existe toute une famille de widgets, dont `FloatSlider` est l'exemple le plus courant, mais vous pouvez aussi :
#
# * créer des radio bouton pour entrer un paramètre booléen ;
# * ou une saisie de texte pour entre un paramètre de type `str` ;
# * ou une liste à choix multiples…
#
# Bref, vous pouvez créer une mini interface-utilisateur avec des objets graphiques simples choisis dans une palette assez complète pour ce type d'application.
#
# Voyez [les détails complets sur `readthedocs.io`](http://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)

# %% slideshow={"slide_type": "slide"}
# de même qu'un tuple était ci-dessus un raccourci pour un FloatSlider
# une liste ou un dictionnaire est transformé(e) en un Dropdown
plt.figure()
interact(sinus, 
         freq={'rapide': 10., 'moyenne': 1., 'lente': 0.1});

# %% [markdown] slideshow={"slide_type": "slide"}
# Voyez la [liste complète des widgets ici](http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html).

# %% [markdown]
# ### Dashboards et Layouts

# %% [markdown]
# Lorsqu'on a besoin de faire une interface un peu plus soignée, on peut créer sa propre disposition de boutons et autres réglages.

# %% [markdown]
# Pour cela on utilise plutôt la fonction `interactive_output()`, qui attend toujours **deux** paramètres:
#
# * d'abord la fonction principale, comme pour `interact`
# * puis **un dictionnaire** qui associe à chaque nom de paramètre un widget interactif
#
# L'avantage est qu'avec cette API nous allons pouvoir agir sur la position des différents widgets
#
# Voyons cela tout de suite sur un exemple

# %%
# les widgets pour construire le tableau de bord
from ipywidgets import (interactive_output,
                        IntSlider, Dropdown, Layout, HBox, VBox, Text)
from IPython.display import display


# %% slideshow={"slide_type": "subslide"}
# une fonction sinus à 4 réglages

def sinus4(freq, phase, amplitude, domain):

    X = np.linspace(0., domain*np.pi, 500)
    Y = amplitude * np.sin(freq*(X+phase))
    # comme on va régler l'amplitude, on fixe l'échelle en Y
    plt.clf()
    plt.ylim(-5, 5)
    plt.plot(X, Y)


# %% cell_style="center"
def my_dashboard():
    """
    create and display a dashboard
    return a dictionary name->widget 
    suitable for interactive_output
    """
    # dashboard pieces as widgets
    l_75 = Layout(width='75%')
    l_50 = Layout(width='50%')
    l_25 = Layout(width='25%')

    w_freq = Dropdown(options=list(range(1, 10)),
                      value = 1,
                      description = "fréquence",
                      layout=l_50)
    w_phase = FloatSlider(min=0., max = 2*np.pi, step=np.pi/12,
                          description="phase",
                          value=0., layout=l_75)
    w_amplitude = Dropdown(options={"micro" : .3,
                                    "mini" : .1,
                                    "normal" : 2.,
                                    "grand" : 3.,
                                    "énorme" : 5.},
                           value = 3.,
                           description = "amplitude",
                           layout = l_25)
    w_domain = IntSlider(min=1, max=10, description="dom. n * π", layout=l_50)

    # make up a dashboard
    dashboard = VBox([HBox([w_amplitude, w_phase]),
                      HBox([w_domain, w_freq]),
                     ])
    display(dashboard)
    return dict(freq=w_freq, phase=w_phase,
                amplitude=w_amplitude, domain=w_domain)


# %% [markdown]
# *****
# Avec tout ceci en place on peut montrer un dialogue interactif pour changer tous les paramètres de sinus4.

# %%
# interactively call sinus4
# attention il reste un bug:
# au tout début rien ne s'affiche,
# il faut faire bouger au moins un réglage
plt.figure()
interactive_output(sinus4, my_dashboard())

# %% [markdown]
# ## Voir aussi
#
# pour davantage de détails sur sur les différentes sorties disponibles de matplotlib, et le mode dit 'interactif' avec `plt.ion()`, voir
#
# https://matplotlib.org/stable/users/explain/interactive.html#interactive-figures

# %% [markdown]
# Je vous signale enfin un [exemple de notebook publié par la célèbre revue *Nature*](http://www.nature.com/news/ipython-interactive-demo-7.21492), qui pourra vous donner une idée de ce qu'il est possible de faire avec un notebook interactif. Interactif dans le sens où on peut faire varier les paramètres d'une expérience et voir l'impact du changement se refléter immédiatement sur la visualisation.
#
# Comme il n'est malheureusement plus actif en ligne semble-t-il, 
# je vous invite à le faire marcher localement à partir [de la version sur github ici](https://github.com/jupyter/nature-demo).
