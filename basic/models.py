#!/bin/python2
##-*- coding: utf-8 -*-
##===============================================================================
##
##          FILE: models.py
##
##         USAGE: python2 models.py
##
##   DESCRIPTION: 
##
##       OPTIONS: ---
##  REQUIREMENTS: ---
##         NOTES: ---
##        AUTHOR: Jingxin Fu
##       VERSION: 1.0
## Creation Date: 21-02-2017
## Last Modified: Wed Mar 22 14:41:13 2017
##===============================================================================
import basic 

class Cookie(basic.Suite):
    def __init__(self,hypothesis):
        basic.Suite.__init__(self,hypothesis)
        self.data_cookie = {"Bow 1":dict(vanilla=30,chocolate=10),
                            "Bow 2":dict(vanilla=20,chocolate=20)
                            }

    def priorDistr(self,hypothesis):
        for hypo in hypothesis:
            self.PriorProb(hypo,1)

    def Likelihood(self,hypo,ins):
        like = self.data_cookie[hypo][ins]
        #considering the condition that does not supply cookie when taken out
        #self.data_cookie[hypo][ins] -= 1
        return like

class Die(basic.Suite):
    """docstring for Die"""
    def __init__(self,hypothesis):
        basic.Suite.__init__(self,hypothesis)

    def priorDistr(self,hypothesis):
        for hypo in hypothesis:
            self.PriorProb(hypo,1)

# class Train(basic.Suite):
#     def Likelihood(self,hypo,ins):
