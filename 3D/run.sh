#!/usr/bin/bash

# directory with scripts
HOME=/Users/Lexi/Documents/Ohern_2016/vicsek_model/3D

N=$1
eta=$2
r=$3

echo "N =" $1
echo "eta =" $2
echo "r =" $3

folder="simulation2"

# # make directory for current simulation
mkdir $folder
cd $folder/

# # save coordinates & thetas for every time step
mkdir particles
cd particles

# # run vicsek simulation
python $HOME/vicsek2d.py $N $eta $r 

# # make folder for plots
cd ..
mkdir plots

# plot coordinates
python $HOME/plot.py $eta