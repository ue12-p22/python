---
marp: true
markdown.marp.enableHtml: true
theme: base
backgroundImage: url('https://marp.app/assets/hero-background.svg')
color: #44f
header: IC P22 - AP Python
footer: 'cours Python ![height:40px](media/logo-python.svg)'
# tmp
paginate: true
---

<style>
@import url('https://fonts.googleapis.com/css?family=Patrick+Hand|Patrick+Hand+SC');

section {
    font-family: "Patrick Hand", Verdana;
    font-size: xxx-large;
}

section::after {
  content: 'Page ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}

</style>

 <!-- # les fonctions ![height:100px](media/logo-python.svg) */ -->

# <!-- fit -->les fonctions ![height:100px](media/logo-python.svg)

<!-- _backgroundImage: url("media/background-functions.png") -->
<!-- backgroundColor: rgba(255,0,0,128) -->

---
<!-- paginate: true -->

## <!-- fit -->plan: les (bonnes) bases
1. les paramètres et arguments
2. les *closures*
3. les *générateurs*
4. les outils de la librairie Python
5. des fontions partout (brain teaser)

---

# <!-- fit --> les (bonnes) bases

---

## <!-- fit --> les paramètres et arguments

---
<!-- _color: 8f44 -->
### bases

pour créer une fonction Python:

```python
def add(x, y):
    return x + y
```

cette fonction accepte deux **paramètres** `x` et `y` et retourne leur somme

---
### bases (suite)
<!-- _color: #a44 -->
<!-- _fontSize: xx-large -->

on doit l'appeller avec **autant** d'arguments qu'elle attend de paramètres

```python
In []: add(1, 2)
Out[]: 3
```

car sinon **boom**

```python
In [2]: add(1)
TypeError: add() missing 1 required positional argument: 'y'
```

ou encore
```python
In [4]: add(1, 2, 3)
TypeError: add() takes 2 positional arguments but 3 were given
```

---
<style>
    font-size: x-large;
</style>

## arguments nommés

## nombre variable d'arguments (suite)
## valeurs par défaut
## wildcard *args
## wildcard *
## wildcard **kwds

---
# <!--fit--> closures

---

## termes clos ou pas

```python
def sum_and_prod(x, y, z):
    def prod():
        return y * z
    return x + prod()
```

---
## encore mieux

```python
def product_with(x):
    def _inner(y):
        return x * y
    return _inner
```

---
## lambda

```python
def product_with(x):
    return lambda y: x + y
```

exercice...

---
# <!--fit--> les générateurs

---
```python
def count():
    for i in range(1, 4):
        yield i
```

exercices...

---
rappel: les expressions génératrices

```python
odds = (2*x+1 for x in range(4))
for o in odds:
    print(o)
```

---
# <!--fit--> les outils standard

de la lib Python

---
## `map` & `filter`
## `all` & `any
## `partial`
## divers `itertools`

* `product`
* `permutations`
* `combinations`

exercice: le jeu de cartes

---
# <!--fit--> lambda calcul

des fonctions partout

---

## règles du jeu
## Church numerals
## successeur, addition multiplication, soustraction
## booléens, if/then/else
