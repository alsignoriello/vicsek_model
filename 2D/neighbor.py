#!/usr/bin/python
import numpy as np
from geometry import *


# returns a list of indices for all neighbors
# includes itself as a neighor so it will be included in average
def get_neighbors(particles, r, x0, y0):

	neighbors = []

	for j,(x1,y1) in enumerate(particles):
		dist = euclidean_distance(x0, y0, x1, y1)

		if dist < r:
			neighbors.append(j)

	return neighbors


# average unit vectors for all angles
# return average angle 
def get_average(thetas, neighbors):
	
	n_neighbors = len(neighbors)
	avg_vector = np.zeros(2)

	for index in neighbors:
		theta = thetas[index,0]
		theta_vec = angle_2_vector(theta)
		avg_vector += theta_vec

	avg_vector = avg_vector / n_neighbors

	return avg_vector




