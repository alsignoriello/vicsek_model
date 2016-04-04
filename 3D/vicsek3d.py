#!/usr/bin/python
import numpy as np
from geometry3d import *
from neighbor import *
import sys


# number of particles
N = int(sys.argv[1])

# noise intensity
eta = float(sys.argv[2])

# neighbor radius
r = float(sys.argv[3])

# time step
delta_t = 0.05

# Maximum time
t = 0.
T = 10.

# Generate random particle coordinations
# particles[i,0] = x
# particles[i,1] = y
particles = np.random.uniform(0,1,size=(N,3))

# initialize random angles in 3D
rand_vecs = np.zeros((N,3))
for i in range(0,N):
	vec = rand_vector()
	rand_vecs[i,:] = vec


# Run until time ends
while t < T:
	print t
	
	# save coordinates & angle vectors
	output = np.concatenate((particles,rand_vecs),axis=1)
	np.savetxt("simulation1/%.2f.txt" % t, output)


	for i,(x,y,z) in enumerate(particles):

		# get neighbor indices for current particle
		neighbors = get_neighbors(particles, r, x, y, z)

		# get average theta vector
		avg = get_average(rand_vecs, neighbors)

		# get noise vector
		noise = eta * rand_vector()

		# move to new position 
		particles[i,:] += delta_t * (avg + noise)

		# get new angle vector
		rand_vecs[i] = avg + noise

		# assure correct boundaries (xmax,ymax) = (1,1)
		if particles[i,0] < 0:
			particles[i,0] = 1 + particles[i,0]

		if particles[i,0] > 1:
			particles[i,0] = particles[i,0] - 1

		if particles[i,1] < 0:
			particles[i,1] = 1 + particles[i,1]

		if particles[i,1] > 1:
			particles[i,1] = particles[i,1] - 1

		if particles[i,2] < 0:
			particles[i,2] = 1 + particles[i,2]

		if particles[i,2] > 1:
			particles[i,2] = particles[i,2] - 1

	# new time step
	t += delta_t


