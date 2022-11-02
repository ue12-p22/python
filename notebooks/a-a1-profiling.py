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
#     title: profiling et al
# ---

# %% [markdown]
# # Étude de performances

# %% [markdown]
# imaginons que vous venez d'écrire un code magnifique pour résoudre le Rubik's cube ou calculer la quadrature de la Tour Eiffel, ou peu importe
#
# bon, le code marche, il retourne bien les bonnes valeurs; sauf que c'est mou, le programme se traîne et n'en finit pas de mouliner, alors que vous avez le sentiment que ça devrait aller beaucoup plus vite que ça

# %% [markdown]
# dans ces cas-là, le premier réflexe, c'est de commencer par une petite analyse introspective
#
# * **ça devrait être quoi en principe la complexité ?**  
#   ça vaut toujours la peine de s'arrêter 5 minutes pour ré-évaluer, sur le code présent et non pas sur la version d'il y a deux semaines, la complexité théorique du code  
#   en n'oubliant pas de prendre en compte les spécificités des types de données qu'on a choisies; rappelez-vous le cours, et regardez bien toutes les fois où vous balayez toute une liste (on vous bassine depuis le début du cours sur le fait que les recherches dans une liste sont en O(n)); assurez-vous de bien utiliser des ensembles si vous avez beaucoup de recherches à faire, ce genre de choses
#
# * **est-ce que cette complexité théorique est bien confirmée par l'expérience ?**  
#   par exemple si vous attendez à un algo quadratique, est-ce que de multiplier la taille des entrées par 3 ou par 10, ça provoque un allongement dans un rapport 9 ou 100 ?

# %% [markdown]
# c'est important de faire cette analyse, et de ne pas se jeter immédiatement dans le profiling
#
# mais clairement avec juste un cerveau ça n'est pas forcément trivial de tout prendre en compte, surtout lorsqu'on utilise des librairies tierces qui fonctionnent on ne sait pas toujours exactement comment

# %% [markdown]
# ## c'est quoi le *profiling* ?

# %% [markdown]
# du coup, pour pouvoir faire une analyse basée sur des faits objectifs, il existe une technique, le *profiling* donc, qui repose sur une idée relativement simple.
#
# dans le cas de Python, le code est interprété; ça signifie que c'est l'interpréteur qui se charge de faire avancer le programme; et si on lui demande gentiment, on peut faire en sorte qu'il enregistre les événements du type *appel de fonction*, avec l'instant où ça se passe.

# %% [markdown] tags=["level_intermediate"]
# pour information, on appelle cette méthode le *profiling* déterministe, car tous les événements sont pris en compte;
# avec les langages compilés comme C++, on est obligé d'utiliser une approche statistique, qui consiste à échantillonner à intervalle régulier l'état de la pile d'exécution; mais peu importe..

# %% [markdown]
# ## en pratique : `cProfile`

# %% [markdown]
# pour commencer on va utiliser un script simplissime qui est celui-ci  
# (souvenez-vous que les commandes avec un `!` sont à destination **du terminal** et pas de Python)

# %%
# ! cat fibo.py

# %% [markdown]
# ### lancer en mode *profiling*

# %% [markdown]
# si vous devez ne retenir qu'une chose pour la mise en pratique, c'est que pour un programme qui se lance comme ceci

# %%
# ! python fibo.py 32

# %% [markdown]
# alors vous pouvez le lancer en mode profiling en invoquant le module `cProfile` comme ceci

# %%
# il suffit d'ajouter le '-m cProfile' 

# ! python -m cProfile fibo.py 32

# %% [markdown]
# ### comment lire le résultat

# %% [markdown]
# en gros, on y trouve une ligne par fonction appelée dans le programme 
#
# dans notre premier exemple trivialissime, nous n'avons défini que deux fonctions `fibo` et `main`; (il y a toujours un peu de bruit, des fonctions appelées par l'interpréteur, à ignorer) 
#
# pour chaque fonction on va trouver
#
# * `ncalls` : le nombre de fois que la fonction a été appelée
# * `tottime` : le **temps CPU** pendant laquelle **la fonction a eu le CPU**
# * `cumtime` : le **temps CPU** pendant laquelle **la fonction ou une fonction appelée par elle**, a eu le CPU
#
# ainsi dans notre exemple, la fonction `main` a un `cumtime` quasi égal
# à celui de `fibo` (parce que pendant tout le temps on est dans `fibo`,
# on est aussi indirectement dans `main`) , mais un temps "en propre"
# quasi nul

# %% [markdown] tags=["level_intermediate"]
# notez la subtilité, ici on **parle de temps CPU, pas de temps ressenti**
#
# c'est quoi la différence, me direz-vous ? 
#
# imaginez une fonction qui attend un paquet en provenance du réseau
#
# le temps ressenti (en anglais on parle de *wallclock time*) c'est basé sur l'heure usuelle; on va mesurer le temps ressenti comme la différence entre l'heure à laquelle la fonction commence son travail et celle où elle le finit; si le paquet réseau met 1 s à arriver, le temps ressenti pour exécuter la fonction c'est 1s
#
# le temps CPU au contraire, c'est lié au nombre de cycles pendant lesquels la fonction a le CPU, et dans notre cas ça va être plutôt quelque chose d'un ordre de grandeur largement inférieur à la milliseconde

# %% [markdown]
# ### trier le résultat

# %% [markdown]
# pour trier selon une colonne, on ajoute encore l'option `-s`, (s comme
# *sort* évidemment)

# %%
# pour trier selon le nombre d'appels - la colonne 'ncalls' 

# ! python -m cProfile -s ncalls fibo.py 32

# %% [markdown]
# ### comment s'en servir

# %% [markdown]
# dans un cas réel, ce n'est pas `ncalls` qui nous intéresse le plus, et souvent la découverte la plus intéressante est faite en triant selon la colonne `tottime`, la fonction qui mange le plus de CPU

# %% [markdown]
# ## *right tool for the job*

# %% [markdown]
# juste pour bien préciser le vocabulaire, on a vu pendant le cours plusieurs techniques qui sont bien distinctes, qu'il faut savoir utiliser à bon escient
#
# * le ***debugging*** c'est l'art de passer d'un premier jet à un code qui marche vraiment; dit autrement, il s'agit  de trouver où et/ou pourquoi un programme ne fait pas tout à fait exactement ce qu'on voudrait  
#   pour cette phase, on peut soit a) instrumenter manuellement le code en ajoutant des `print()`, ou b) faire tourner le programme sous un debugger - par exemple sous vs-code - qui au prix d'un peu de setup et d'apprentissage, est un outil bien plus puissant pour gérer les *breakpoint* à la souris, exécuter le programme pas à pas tout en inspectant la valeur des variables, etc...
#
# * le ***benchmarking***, qui consiste à mesurer très finement le temps d'exécution d'un fragment de code  
#   pour ça on a rencontré déjà le module `timeit`, avec comme compagnons les *magic* Jupyter en `%timeit` et `%%timeit`
#
# * le ***profiling***, qui consiste à observer le programme en cours d'exécution, pour créer des statistiques, et ultimement déterminer la partie de code la plus sollicitée, en vue d'optimiser le code  
#   pour ça on utilise les outils vus plus haut, comme `cProfile`
#
# * le ***test*** : on veut avoir une info de synthèse sur le bon comportement du code dans idéalement un grand nombre de situtations - *the more the better*
#
#   pour ça on utilise des outils comme `pytest`; l'objectif ici étant de donner **une synthèse** sur le plus grand nombre possible de tests, ces outils sont *mal adaptés* au debugging; dit autrement, lorsqu'un test échoue on est censé retourner à la case *debug*

# %% [markdown]
# ## *see also*

# %% [markdown]
# la documentation standard Python [sur le profiling](https://docs.python.org/3/library/profile.html)  
# il y a notamment toute une API pour utiliser le profiler

# %% [markdown] tags=["level_intermediate"]
# cet article très intéressant vous parle des alternatives à `cProfile`
#
# <https://pythonspeed.com/articles/beyond-cprofile/>
