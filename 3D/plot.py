#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys
from mpl_toolkits.mplot3d import Axes3D
from geometry3d import unit_vector



def plot_vectors(coords, vecs):

	# generate random color for every particle
	colors = ["b", "g", "y", "m", "c", "pink", "purple", "seagreen",
			"salmon", "orange", "paleturquoise", "midnightblue",
			"crimson", "lavender"]

	for i,(x,y,z) in enumerate(coords):

		c = colors[i % len(colors)]

		# plot point
		ax.scatter(x,y,z,color=c,marker=".")

		# # plot tail
		tail = unit_vector(vecs[i,:], np.array([0,0,0]))
		x1 = x - 0.1 * tail[0]
		y1 = y - 0.1 * tail[1]
		z1 = z - 0.1 * tail[2]
		ax.plot([x,x1], [y,y1], [z,z1], color=c)


	return



def save_plot(file, eta):

	# axes between 0 and 1
	ax.set_xlim3d(0, 1)
	ax.set_ylim3d(0, 1)
	ax.set_zlim3d(0, 1)

	# remove tick marks
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])

	# title 
	# plt.title("$\eta$ = %.2f" % eta)

	# save plot
	plt.savefig("plots/%s.jpg" % file)
	plt.close()

	# clear for next plot
	plt.cla()

	return


eta = float(sys.argv[1])


for file in glob.glob("simulation1/*.txt"):
	outfile = file[12:-4]
	print file, outfile
	mat = np.loadtxt(file)
	coords = mat[:,0:3]
	vecs = mat[:,3:]

	# initialize figure
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	# plot vectors
	plot_vectors(coords, vecs)
	save_plot(outfile, eta)








