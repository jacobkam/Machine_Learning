#!/bin/python2
##-*- coding: utf-8 -*-
##===============================================================================
##
##          FILE: basic.py
##
##         USAGE: python2 basic.py
##
##   DESCRIPTION: A class for basic bayesian model
##
##       OPTIONS: ---
##  REQUIREMENTS: ---
##         NOTES: ---
##        AUTHOR: Jingxin Fu
##       VERSION: 1.0
## Creation Date: 21-02-2017
## Last Modified: Thu Mar 23 15:10:00 2017
##===============================================================================
import plot

class _basic():
    # initialize a dictionary for storing hypothesis and its probability
    def __init__(self):
        self.dic= {}
        self.hist={}
    
    # initialize the prior probabilitiese
    def PriorProb(self,x,freq):
        self.dic[x] = freq
    
    # calculate total number of the hypothesis  
    def total(self):
        return sum(self.dic.values())

    # normalize the probabilities among hypothesis 
    def normalize(self):
        Total = self.total()
        if Total == 0:
            raise ValueError('Total probability is zero!')
        factor = 1.0/Total
        for hypo in self.dic.keys():
            self.dic[hypo] *= factor 
    def mutiple(self,hypo,factor):
        self.dic[hypo] = self.dic.get(hypo,0) * factor
    # below: fot hist plot
    ## count occurrence times of each key
    def incr(self,key,term=1):
        self.hist[key] = self.hist.get(key,0) + term

    # print result
    def Print(self):
        for hypo,prob in self.dic.items():
            print str(hypo) + ":" + "%f"%(prob)

    def Plot(self,title,xlab,ylab):
        x = []
        y = []
        for key,value in self.dic.iteritems():
            x.append(key)
            y.append(value)
        
        plot.histPlot(x,y,title,xlab,ylab)


class Suite(_basic):

    # input pripor probabilities distribution
    def __init__(self,hypothesis):
        _basic.__init__(self)
        self.priorDistr(hypothesis)
        self.normalize()
    
    # Update the probabilities
    def Update(self,ins):
        for hypo in self.dic.keys():
            like = self.Likelihood(hypo,ins)
            self.mutiple(hypo,like)
        self.normalize()
    
    

