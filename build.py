#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

os.system("rm main.4ct")
os.system("rm main.4tc")
os.system("rm main.dvi")
os.system("rm main.idv")

os.system("rm main.aux")
os.system("rm main.bbl")
os.system("rm main.blg")
os.system("rm main.out")
os.system("rm main.out")
os.system("rm main.out")


# english

os.system("pdflatex main.tex")
os.system("bibtex main")
os.system("pdflatex main.tex")
os.system("pdflatex main.tex")

os.system("open main.pdf")



#html


os.system('htlatex main.tex "html,word" \'symbol/!\' "-cvalidate"')


#cleanup

os.system("rm main.4ct")
os.system("rm main.4tc")
os.system("rm main.dvi")
os.system("rm main.idv")


os.system("rm main.aux")
os.system("rm main.bbl")
os.system("rm main.blg")
os.system("rm main.out")
os.system("rm main.out")
os.system("rm main.out")