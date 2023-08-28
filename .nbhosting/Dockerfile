# --------
FROM nbhosting/minimal-notebook

# NOTE
# we cannot use jupyter nbextension enable/disable
# because this is no longer available under nb7
# for the record we used to have these 2:
# && jupyter nbextension enable hide_input/main \
# && jupyter nbextension install --py k3d \
RUN true \
 && pip install -U nb-courselevels \
 && pip install -U nbautoeval \
 && pip install -U ipythontutor \
 && pip install rise \
 && pip install numpy pandas matplotlib chart_studio bokeh k3d autograd \
 && apt-get install -y graphviz && pip install graphviz \
 && pip install pylint \
 && pip install aiohttp \ 
 && true
