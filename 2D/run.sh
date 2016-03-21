#!/usr/bin/bash

# directory with scripts
HOME=/Users/Lexi/Documents/Ohern_2016/vicsek_model/2D

N=$1
eta=$2
r=$3

echo "N =" $1
echo "eta =" $2
echo "r =" $3


# make directory for current simulation
# mkdir simulation
cd simulation/

# save coordinates for every time step
# mkdir coordinates/
cd coordinates

# run vicsek simulation
python $HOME/vicsek2d.py $N $eta $r 

# make folder for plots
cd ..
mkdir plots
cd plots/

# plot coordinates
python $HOME/plot2d.py