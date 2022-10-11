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
#     title: streamlit
# ---

# %% [markdown]
# # streamlit

# %% [markdown]
# Pour finir, je mentionne rapidement [la librairie `streamlit`](https://streamlit.io).
#
# Elle est un peu atypique, en ce sens qu'elle permet de construire en Python des applications purement web (sans besoin d'installer les notebooks)

# %% [markdown]
# ## Modèle de calcul

# %% [markdown]
# Une application streamlit se présente sous la forme d'un calcul séquentiel, qui va être **entièrement ré-exécuté** à chaque changement de paramètre.
#
# Commençons par un exemple simple

# %%
# !cat streamlit-sinus.py

# %% [markdown]
# ## Pour installer

# %% [markdown]
# Sans surprise, avec `pip install streamlit`

# %% [markdown]
# ## Pour l'exécuter

# %% [markdown]
# on tape dans le terminal
# ```
# streamlit run streamlit-sinus.py
# ```

# %% [markdown]
# ## Démo 1

# %% [markdown]
# Dans ce code, j'utilise 3 appels à des fonctions de streamlit
#
# * `st.slider` pour pouvoir entrer le paramètre `freq`
# * `st.selectbox` pour pouvoir entrer le paramètre `amplitude`
# * `st.pyplot` pour afficher une figure matplotlib

# %% [markdown]
# *&lt;démo&gt;*

# %% [markdown]
# ## Démo 2

# %% [markdown]
# ```
# streamlit run streamlit-taylor.py
# ```
#
# *&lt;démo&gt;*

# %% [markdown]
# ## Avantages
#
# * Surtout et avant tout je pense, on obtient très simplement une application Web **très facile à installer** (notamment pas besoin de Jupyter et tout ça); cette techno se prête donc très bien à la réalisation de *dashboards*
#
# * Le modèle de calcul a un gros avantage, il a tendance à beaucoup simplifier la conception; dans les autres modèles, dès que c'est un peu compliqué on a souvent besoin, pour être efficace, de traiter différemment l'initialisation et les mises à jour; ici pas besoin de s'embêter avec ça
#
# * Pour les cas où on va, par exemple, chercher des données sur Internet: si le chargement dure plusieurs secondes ou plus, on ne veut pas avoir à attendre ce délai à chaque exécution du script (puisqu'on passe son temps à le faire...);
# pour ces cas d'usage il y a un mécanisme de cache très facile à utiliser

# %% [markdown]
# ## Inconvénients
#
# * Le modèle de calcul ne se prête pas à toutes les applications
# * Peut avoir tendance à n'être pas suffisamment efficace

# %% [markdown]
# ## Galerie
#
# Pour un aperçu plus vaste des possibilités
#
# https://streamlit.io/gallery
