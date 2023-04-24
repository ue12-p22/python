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
#     title: Animations interactives avec matplotlib
#   version: '3.0'
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# <span><img src="media/inria-25-alpha.png"/></span>
# </div>

# %% [markdown]
# # Animations interactives avec `matplotlib`

# %% [markdown]
# ## Complément - niveau avancé

# %% [markdown]
# Nous allons voir dans ce notebook comment créer une animation avec matplotlib et tirer parti des *widgets* dans un notebook pour rendre ces animations interactives.
#
# Ce sera l'occasion de décortiquer un exemple un peu sophistiqué, où l'utilisation d'un générateur permet de rendre l'implémentation plus propre et plus élégante.

# %% [markdown]
# **Vocabulaire**  
#
# * dans le notebook précédent on a parlé de notebooks **interactifs**: il s'agit de créer une visualisation qui **réagisse** aux actions utilisateur
# * ici on va parler entre autres d'**animations**: il s'agit de faire une visualisation qui **bouge toute seule**
#
# les deux notions sont voisines - dans les deux cas par exemple on va faire bouger la phase d'une sinusoïde - mais c'est important de bien les distinguer, car les mécanismes pour les fabriquer sont différents

# %% [markdown]
# ### Le sujet

# %% [markdown]
# En guise d'illustration, nous allons créer :
#
# * une animation matplotlib : disons que l'on veut faire défiler horizontalement une sinusoïde ;
# * un widget interactif : disons que l'on veut pouvoir changer la vitesse de défilement.

# %% [markdown]
# ### Les outils

# %% [markdown]
# Pour fabriquer cela nous aurons besoin principalement :
#
# * de la librairie d'animation de matplotlib, et spécifiquement le sous-package `animation`,
# * et des widgets du module `ipywidgets`.

# %%
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# %%
from IPython.display import display as display_widget
from ipywidgets import IntSlider

# %% [markdown]
# ### La logique

# %% [markdown]
# Dans un notebook précédent nous avions abordé la fonction `interact`, de la librairie `ipywidgets`, qui nous permettait d'appeler interactivement une fonction avec des arguments choisis interactivement via une série de widgets.
#
# Si on essaie d'utiliser `interact` pour faire des animations, l'effet visuel, qui revient à effacer/recalculer une visualisation à chaque changement de valeur des entrées, donne un rendu peu agréable à l'oeil.
#
# C'est pourquoi ici la logique va être un petit peu différente :
#
# * c'est une fonction native de `matplotlib` qui implémente la boucle principale, en travaillant sur un objet `Figure`,
# * et lorsqu'on va vouloir rendre notre animation interactive, le widget sera utilisé uniquement pour modifier une variable python ;
# * pour simplifier notre code, l'échange d'informations entre ces deux morceaux se fait le plus simplement possible, via une variable globale. 
#
# Bien entendu cette dernière pratique n'est pas recommandée dans du code de production, et le lecteur intéressé est invité à améliorer ce point.

# %% [markdown]
# ### Animation non interactive et basique

# %% [markdown]
# Pour commencer nous allons voir comment utiliser `matplotlib.animation` sans interactivité. 
#
# Cette version est inspirée du [tutorial matplotlib sur les animations](https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/), qui montre d'ailleurs d'autres animations plus complexes et convaincantes, comme le double pendule par exemple.

# %% [markdown]
# Mais avant tout choisissons ce mode de rendu :

# %%
# %matplotlib notebook

# %% [markdown]
# Nous allons utiliser la fonction `animation.FuncAnimation`; celle-ci s'attend à recevoir en argument, principalement :
#
# * une figure
# * un ensemble de frames
# * et une fonction d'affichage
#
# La logique est que à intervalles réguliers, `FuncAnimation` va
# * itérer sur les frames (en appelant next())
# * et passer cela à la fonction d'affichage
#
# Dans notre cas, nous allons créer une bonne fois un objet `line1` (de type `matplotlib.lines.Line2D`), qui sera modifié à chaque frame par la fonction d'affichage

# %% [markdown]
# ##### Version basique dite *tout-en-un*

# %%
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# on commence par créer une figure; 
figure1 = plt.figure(figsize=(4, 2))

# en général pour une animation 
# il est important de fixer les bornes en x et en y 
# pour ne pas avoir d'artefacts de changement d'échelle
# pendant l'animation
ax1 = plt.axes(xlim=(0, 2), ylim=(-1.5, 1.5))

# on crée aussi un plot vide qui va être modifié à chaque frame
line1, = ax1.plot([], [], linewidth=2)

# la vitesse de défilement
speed = 1

# une globale; c'est vilain !
offset = 0.

# la fonction qui calcule et affiche chaque frame
def compute_and_display(n):
    global offset
    offset += speed / 100
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - offset))
    line1.set_data(x, y)


# la fonction magique pour animer une figure

# ici frames=50 est interprété comme range(50)
# à chaque cycle, on itère sur frames() et le résultat
# - donc ici un entier - est passé à compute_and_display
# c'est pourquoi cette dernière prend un paramètre n
anim = animation.FuncAnimation(figure1, 
                               func=compute_and_display, 
                               frames=50, repeat=False,
                               # blit=True est une optimisation graphique 
                               # pour ne rafficher que le nécessaire
                               interval=40, blit=True)
plt.show()

# %% [markdown]
# ### Séparation calcul et affichage

# %% [markdown]
# On voit qu'on a appelé `FuncAnimation` avec `frames=50` et `interval=40` (ms); ce qui correspond donc à 25 images par seconde, soit une durée de deux secondes.
#
# Profitons-en pour voir tout de suite une amélioration possible. 
# Il serait souhaitable de séparer :
#
# * d'une part la logique du calcul - ou de l'acquisition, si on voulait par exemple faire du postprocessing temps réel d'images vidéo,
# * et d'autre part l'affichage à proprement parler.

# %% [markdown]
# Pour cela, remarquez que le paramètre `frames` est documenté comme pouvant être **un itérateur**. La logique en fait à l'oeuvre dans `FuncAnimation` est que 
#
# * `frames` est un itérateur qui va énumérer des données,
# * à chaque frame cet itérateur est avancé avec `next()`, et son retour est passé à la fonction d'affichage.
#
# En guise de commodité, lorsqu'on passe comme ci-dessus `frames=200`, la fonction transforme cela en `frames=range(200)`. C'est pourquoi d'ailleurs il est important que `compute_and_display` accepte un paramètre unique, même si nous n'en avons pas eu besoin.

# %% [markdown]
# Cette constatation nous amène à une deuxième version, en concevant un **générateur** pour le calcul, qui est passé à `FuncAnimation` comme paramètre `frames`.

# %% [markdown]
# ##### Version non interactive, mais avec séparation calcul / affichage

# %%
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

figure2 = plt.figure(figsize=(4, 2))
ax2 = plt.axes(xlim=(0, 2), ylim=(-1.5, 1.5))
line2, = ax2.plot([], [], linewidth=2)

# la vitesse de défilement
speed = 1

# remarquez qu'on n'a plus besoin de globale ici
# une locale dans le générateur est bien plus propre

# la logique du calcul est conçue comme un générateur
def compute():
    offset = 0.
    # nous sommes dans un générateur, il n'y a pas 
    # de contre-indication à tourner indéfiniment
    while True:
        offset += speed / 100
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - offset))
        # on décide de retourner un tuple X, Y
        # qui est passé tel-quel à l'affichage
        yield x, y 

# la fonction qui affiche
# le paramètre frame correspond exactement 
# à la sortie de compute()
def display(frame):
    # on retrouve nos deux éléments x et y
    x, y = frame
    # il n'y a plus qu'à les afficher
    line2.set_data(x, y)
    return line2,


anim = animation.FuncAnimation(figure2,
                               func=display,
                               frames=compute(),
                               interval=40, blit=True)
plt.show()

# %% [markdown]
# Cette fois l'animation ne se termine jamais, mais dans le notebook vous pouvez cliquer le bouton bleu en haut à droite de la figure pour la faire cesser.

# %% [markdown]
# ### Avec interactivité

# %% [markdown]
# Pour rendre ceci interactif, nous allons simplement ajouter un widget qui nous permettra de régler la vitesse de défilement.

# %% [markdown]
# ##### Version interactive avec widget pour choisir la vitesse

# %%
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

from IPython.display import display as display_widget
from ipywidgets import IntSlider

figure3 = plt.figure(figsize=(4, 2))
ax3 = plt.axes(xlim=(0, 2), ylim=(-1.5, 1.5))
line3, = ax3.plot([], [], linewidth=2)

# un widget pour choisir la vitesse de défilement
speed_slider = IntSlider(min=1, max=10, value=3,
                         description="Vitesse:")

def compute():
    offset = 0.
    # nous sommes dans un générateur, il n'y a pas 
    # de contrindication à tourner indéfiniment
    while True:
        # on accède à la vitesse via le widget
        offset += speed_slider.value / 100
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - offset))
        # on décide de retourner un tuple X, Y
        # qui est passé tel-quel à l'affichage
        yield x, y 

# la fonction qui affiche
def display(frame):
    # on retrouve nos deux éléments x et y
    x, y = frame
    # il n'y a plus qu'à les afficher
    line3.set_data(x, y)
    return line3,


anim = animation.FuncAnimation(figure3,
                               func=display,
                               frames=compute(),
                               interval=40, blit=True)

display_widget(speed_slider)
plt.show()

# %% [markdown]
# ### Conclusion

# %% [markdown]
# Avec une approche de programmation plus traditionnelle, on pourrait penser avoir besoin de recourir à plusieurs *threads* pour implémenter ce genre de visualisation interactive.
#
# En effet, vous remarquerez que dans cette dernière version, en termes de parallèlisme, on peut avoir l'impression que 3 choses ont lieu principalement en même temps :
#
# * la logique de calcul, qui en substance est décrite comme un unique `while True:`,
# * la logique d'affichage, qui est cadencée par `FuncAnimation`,
# * et la logique interactive, qui gère le widget sur interaction de l'utilisateur.
#
# Le point à retenir ici est que, grâce à la fois au générateur et au notebook, on n'a pas du tout besoin de gérer soi-même cet aspect de programmation parallèle.

# %% [markdown]
# ### Pour en savoir plus
#
# Voyez : 
#
# * [la documentation du module `animation`](https://matplotlib.org/api/animation_api.html),
# * ainsi que [le tutoriel dont on s'est inspiré pour ce notebook](https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/), surtout pour voir d'autres animations plus élaborées.
