from math import factorial

import autograd
import autograd.numpy as np

from ipywidgets import interact

from bokeh.plotting import figure, show
from bokeh.io import push_notebook

class Taylor:
    """
    provides an animated view of Taylor approximation
    where one can change the degree interactively

    Taylor is applied on X=0, translate as needed
    """

    def __init__(self, function, domain):
        self.function = function
        self.domain = domain

    def display(self, y_range):
        """
        create initial drawing with degree=0

        Parameters:
          y_range: a (ymin, ymax) tuple
            for the animation to run smoothly, we need to display
            all Taylor degrees with a fixed y-axis range
        """
        # create figure
        x_range = (self.domain[0], self.domain[-1])
        self.figure = figure(title=self.function.__name__,
                             x_range=x_range, y_range=y_range,
                            plot_width=900)

        # each of the 2 curves is a bokeh line object
        self.figure.line(self.domain, self.function(self.domain), color='green')
        # store this in an attribute so _update can do its job
        self.line_approx = self.figure.line(
            self.domain, self._approximated(0), color='red', line_width=2)

        # needed so that push_notebook can do its job down the road
        self.handle = show(self.figure, notebook_handle=True)


    def _approximated(self, degree):
        """
        Computes and returns the Y array, the images of the domain
        through Taylor approximation

        Parameters:
          degree: the degree for Taylor approximation
        """
        # initialize with a constant f(0)
        # 0 * self.domain allows to create an array
        # with the right length
        result = 0 * self.domain + self.function(0.)
        # f'
        derivative = autograd.grad(self.function)
        for n in range(1, degree+1):
            # the term in f(n)(x)/n!
            result += derivative(0.)/factorial(n) * self.domain**n
            # next-order derivative
            derivative = autograd.grad(derivative)
        return result


    def _update(self, degree):
        # update the second curve only, of course
        # the 2 magic lines for bokeh updates
        self.line_approx.data_source.data['y'] = self._approximated(degree)
        push_notebook(handle=self.handle)


    def interact(self, degree_widget):
        """
        Parameters:
          degree_widget: a ipywidget, typically an IntSlider
            styled at your convenience
        """
        interact(lambda degree: self._update(degree), degree=degree_widget)
