#!/usr/bin/python
##-*- coding: utf-8 -*-
##===============================================================================
##
##          FILE: plot.py
##
##         USAGE: python2 plot.py
##
##   DESCRIPTION: 
##
##       OPTIONS: ---
##  REQUIREMENTS: ---
##         NOTES: ---
##        AUTHOR: Jingxin Fu
##       VERSION: 1.0
## Creation Date: 23-03-2017
## Last Modified: Thu Mar 23 15:09:17 2017
##===============================================================================
import numpy as np
import matplotlib.pyplot as plt

def histPlot(x,y,title,xlab,ylab,file='./plots/'):
    fig,ax1 = plt.subplots(1,1)
    ax1.plot(np.array(x),np.array(y))
    ax1.set_xlabel(xlab)
    ax1.set_ylabel(ylab)
    plt.savefig(file+title+'.png')
