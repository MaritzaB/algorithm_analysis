all:
	reports/t01_stable_matching.pdf

.PHONY: \
	all \
	clean \
	format \
	reports \
	tests

define renderLatexandBibtex
    cd $(<D) && pdflatex $(<F)
	cd $(<D) && bibtex $(subst .tex,,$(<F))
	cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)
endef

define renderLatex
    cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)
endef

reports/t01_stable_matching.pdf: reports/t01_stable_matching.tex
	$(renderLatex)

reports/t02_asymptotic_order_of_growth.pdf: reports/t02_asymptotic_order_of_growth.tex
	$(renderLatex)

reports/t03_graphs.pdf: reports/t03_graphs.tex
	$(renderLatex)

figures:
	mkdir --parents reports/tables
	mkdir --parents reports/figures
	python3 src/plotter.py

clean:
	rm --force --recursive reports/pythontex*
	rm --force reports/*.aux
	rm --force reports/*.bbl
	rm --force reports/*.blg
	rm --force reports/*.log
	rm --force reports/*.out
	rm --force reports/*.pdf
	rm --force reports/*.toc
	rm --force reports/*.pytxcode

format:
	black --line-length 100 src/*.py

linter:
	$(call lint, src)
	$(call lint, tests)

tests:
	pytest --verbose tests/