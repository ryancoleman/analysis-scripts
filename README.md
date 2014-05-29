analysis-scripts
================

[![doi](https://zenodo.org/badge/3853/ryancoleman/analysis-scripts.png)](http://dx.doi.org/10.5281/zenodo.10216)

Some simple scripts for analyzing lists of data, both paired &amp; unpaired. 

Input files are just lists of numbers, one per line

analyze_lists.py	list1.txt list2.txt

analyze_lists_not_paired.py	list1.txt list2.txt

Output is non-parametric p-values, cohen D effect size values (parametric), and statistical power.

Thinking of adding a non-parametric effect like U/n1n2 via 
http://core.ecu.edu/psyc/wuenschk/docs30/Nonparametric-EffectSize.docx
http://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U

Would love comments on this


The p-value computation was used in: 

Ryan G. Coleman, Kim A. Sharp. Shape and evolution of thermostable 
protein structure. Proteins: Structure, Function, and Bioinformatics. 
78(2). pp. 420-433. 1 February 2010. 
http://dx.doi.org/10.1002/prot.22558

The p-value computation & Cohen Effect Size was used in:
SAMPL4 & DOCK3. 7: lessons for automated docking procedures
RG Coleman, T Sterling, DR Weiss
Journal of computer-aided molecular design
http://link.springer.com/article/10.1007/s10822-014-9722-6


