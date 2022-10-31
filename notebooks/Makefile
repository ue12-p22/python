NOTEBOOKS = $(shell git ls-files [0-9]*)

all: book

include Makefile.style

include Makefile.norm

include Makefile.marp

########## BOOK
book:
	jupyter-book build .
