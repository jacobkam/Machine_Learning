#!/usr/bin/python2

'''
	gradient descent
'''
import numpy as np
import numdifftools as nd
def partial_function(f___,input,pos,value):
    tmp  = input[pos]
    input[pos] = value
    ret = f___(*input)
    input[pos] = tmp
    return ret

def partial_derivative(f,input):
    ret = np.empty(len(input))
    for i in range(len(input)):
        fg = lambda x:partial_function(f,input,i,x)
        ret[i] = nd.Derivative(fg)(input[i])
    return ret

if __name__ == "__main__":
    f     = lambda x,y: x*x*x+y*y
    input = np.array([1.0,1.0])
    print ('partial_derivative of f() at: '+str(input))
    print (partial_derivative(f,input))
def gradientDescent(paramaters,hypothesis,alpha):
	m = len(paramaters)
	updateParameters = [None]*m
	finalParameters = [None]*m
	while len(paramaters):
		for i in range(0,m):
			updateParameters[i]=paramaters[i] - alpha*
			if updateParameters[i] == paramaters[i]:
				finalParameters[i] = paramaters[i]
				del updateParameters[i]
				del paramaters[i]
		paramaters = updateParameters