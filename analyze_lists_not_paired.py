#!/usr/bin/env python 
#ryan g. coleman ryangc@mail.med.upenn.edu


import pdb, sys, string, math
import random #for pvalue tests
import statistics 

def analyzelists(fileNames, numTests=1000000):
  '''somehow these files encode 2 matching lists. either one file with 2 columns
  or 2 files with one column each. or something.
  if there is only one value for one list, replicate it to the length of the
  other one.'''
  lists = [[],[]]
  for fileCount, fileName in enumerate(fileNames):
    for line in open(fileName, 'r'):
      tokens = string.split(string.strip(line))
      if len(tokens) == 1:
        lists[fileCount].append(float(tokens[0]))
      else:
        for tokenCount, token in enumerate(tokens):
          lists[tokenCount].append(float(token))
  diffMean, pVal1, pVal2 = statistics.pvalueDiffMeansLazy(lists[0], lists[1], \
      numTests)  
  cohenD = statistics.cohenEffectSize(lists[0], lists[1])
  print "mean1, mean2, diffMean, pVal1, pVal2, cohenD"
  print statistics.computeMean(lists[0]), statistics.computeMean(lists[1]), \
      diffMean, pVal1, pVal2, cohenD

#this is main
if -1 != string.find(sys.argv[0], "analyze_lists_not_paired.py"): 
  if len(sys.argv) > 1:
    analyzelists(sys.argv[1:])
