NOTEBOOKS = $(shell git ls-files [0-9]*.{py,md})

all: book

include Makefile.style

include Makefile.norm

book:
	jupyter-book build .

.PHONY: all book
