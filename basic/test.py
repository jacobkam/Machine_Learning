#!/bin/python2
##-*- coding: utf-8 -*-
##===============================================================================
##
##          FILE: test.py
##
##         USAGE: python2 test.py
##
##   DESCRIPTION: 
##
##       OPTIONS: ---
##  REQUIREMENTS: ---
##         NOTES: ---
##        AUTHOR: Jingxin Fu
##       VERSION: 1.0
## Creation Date: 21-02-2017
## Last Modified: Thu Mar 23 15:10:45 2017
##===============================================================================
import models

def main():
    ## cookie problem
    hypothesis_cookie = ['Bow 1','Bow 2']
    cookie_instance = models.Cookie(hypothesis_cookie)
    testData = ['vanilla']
    for cookie in testData:
        cookie_instance.Update(cookie)
    
    cookie_instance.Print()
    
    ## train prpblem
    train = models.Train(1000)
    train.Update(60)
    train.Plot(title='Train',xlab='number of Trians',ylab='Probabiliries')


if __name__ == "__main__":
    main()
