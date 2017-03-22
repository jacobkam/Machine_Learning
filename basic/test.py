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
## Last Modified: Tue Feb 21 20:43:04 2017
##===============================================================================
import models

def main():
    hypothesis_cookie = ['Bow 1','Bow 2']
    cookie_instance = models.Cookie(hypothesis_cookie)
    testData = ['vanilla']
    for cookie in testData:
        cookie_instance.Update(cookie)
    
    cookie_instance.Print()

if __name__ == "__main__":
    main()
