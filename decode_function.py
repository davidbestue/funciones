# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:56:24 2019

@author: David Bestue
"""

## Functionsfor pupulation vector

#### Input:
# List of activiy of neuron

#### Output:
# Preferred angle in 0-360 degrees

import numpy as np

def decode(RE):
    N=len(RE)
    R = []
    angles = np.arange(0,N)*2*np.pi/N
    R=np.dot(RE,np.exp(1j*angles)) / N
    angle = np.angle(R)
    if angle < 0:
        angle +=2*np.pi 
    return np.degrees(angle)


## Example:
#### For all the positive activity it is correct from 0-360    
#### For all the negative values, activity in the oppoiste quadrant --> q1:q3;  q2:q4

##q1
#p = [-18,-400,-105]
#q1=[0 for i in range(50)]
#q2=[0 for i in range(307)]
#n_activity = q1 +p +q2
#decode(n_activity)
#
##q2
#p = [-18,-400,-105]
#q1=[0 for i in range(100)]
#q2=[0 for i in range(257)]
#n_activity = q1 +p +q2
#decode(n_activity)
##
##
##q3
#p = [-18,-400,-105]
#q1=[0 for i in range(200)]
#q2=[0 for i in range(157)]
#n_activity = q1 +p +q2
#decode(n_activity)
#
##q4
#p = [-18,-400,-105]
#q1=[0 for i in range(300)]
#q2=[0 for i in range(57)]
#n_activity = q1 +p +q2
#decode(n_activity)


