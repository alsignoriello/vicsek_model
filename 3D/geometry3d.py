#!/usr/bin/python
import numpy as np 
from math import atan2, pi, sin, cos, sqrt


# generate random angle theta between -pi - pi
def rand_vector():		
	theta = np.random.uniform(0,2*pi)
	z = np.random.uniform(-1,1)
	x = cos(theta) * sqrt(1 - z**2)
	y = sin(theta) * sqrt(1 - z**2)
	return np.array([x,y,z])

# Unit vector
def unit_vector(v1, v2):
	vector = v1 - v2
	dist = euclidean_distance(v1[0],v1[1],v1[2],v2[0],v2[1],v2[2])
	uv = vector / dist
	return uv

# Euclidean distance between (x,y,z) coordinates
def euclidean_distance(x1, y1, z1, x2, y2, z2):
	return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1-z2)**2)