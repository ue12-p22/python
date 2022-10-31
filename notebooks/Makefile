NOTEBOOKS = $(shell git ls-files [0-9]*)

all: book

include Makefile.style

include Makefile.norm

########## BOOK
book:
	jupyter-book build .
