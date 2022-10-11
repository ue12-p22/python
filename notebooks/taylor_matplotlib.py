# -*- coding: utf-8 -*-
# +
from autograd import grad
from IPython.display import display
from matplotlib import pyplot as plt
from matplotlib import animation
from math import factorial
from ipywidgets import interact, IntSlider, FloatSlider, Layout

import autograd.numpy as np

# %matplotlib notebook
# -

class MyTaylor:
    def __init__(self, function, domain: np.ndarray):
        self._function = function
        self._domain = domain
        self._approx_line = None
        self._point = None

    def display(self, y_range):
        self.figure = plt.figure()
        # Ici on trace la fonction d'intérêt
        plt.plot(self._domain, self._function(self._domain), lw=2., c='b')
        # et la courbe approchée 
        self._approx_line,  = plt.plot([], [], lw=2., c='orange')
        # puis le point où est fait l'approximation
        self._point, = plt.plot([], [], 'o', c='orange', ms=10.)
        #on trace la grille et tout
        plt.ylim(y_range)
        plt.grid(True,which="both", linestyle='--')
        
    def _update(self, frame):
        # modifier la courbe approximative avec Taylor à l'ordre n
        # je vous recommande de créer cette méthode privée
        # pour pouvoir l'appeler dans interact()

        n, a = frame
        
        # On commence avec tableau rempli de la valeur de la fonction en a
        yapprox = np.full_like(self._domain, self._function(a))

        # On construit notre approximation
        derivative = self._function
        for i in range(1, n+1):
            derivative = grad(derivative)
            ## ici on transforme factorial(i) en flottant car sinon ça plante quand 
            ## factorial(i) dépasse 2^64 (ça arrive entre 20! et 21!)
            yapprox += derivative(a)*((self._domain-a)**i)/float(factorial(i))

        self._approx_line.set_data(self._domain, yapprox)
        self._point.set_data(a, self._function(a))
        return self._approx_line, self._point
        
    def interact(self, widget_order, widget_pos):
        
        def compute():
            # Ici la fonction génératrice pour récupérer les
            # valeurs des widgets.
            while True:
                yield widget_order.value, widget_pos.value
        
        # On affiche les sliders
        display(widget_order)
        display(widget_pos)

        ## Il faut renvoyer l'animation pour que tout fonctionne ;)  
        return animation.FuncAnimation(self.figure,
                               func=self._update,
                               frames=compute(),
                               interval=40, blit=True)


# +
DOMAIN = np.linspace(-4.*np.pi, 4.*np.pi, 1000)

sinus_widget = IntSlider(
   min=1, max=34, step=2, value=0,     # only even degrees
   layout=Layout(width='100%'))

pos_widget = FloatSlider(
   min=DOMAIN[0], max=DOMAIN[-1], step=(DOMAIN[-1]-DOMAIN[0])/100., # 100 points
   layout=Layout(width='100%'))

anim = MyTaylor(function=np.sin, domain=DOMAIN)

anim.display(y_range=(-1.1, 1.1))

anim.interact(sinus_widget, pos_widget)

# -




