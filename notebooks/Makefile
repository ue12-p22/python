NOTEBOOKS = $(shell git ls-files [0-9]*.{py,md})

all: book

include Makefile.style

include Makefile.norm

include Makefile.toc

book:
	jupyter-book build .

.PHONY: all book
