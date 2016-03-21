# Vicsek Model


The Vicsek model is a mathematical model that illustrates the collective motion of particles. The dynamics of the particles in them model depend on the particle density and instensity of noise in the system. 


![r1](https://github.com/https://github.com/alsignoriello/vicsek_model/r1.png) ![r2](https://github.com/https://github.com/alsignoriello/vicsek_model/r2.png)



# Equations
![equation](https://github.com/https://github.com/alsignoriello/vicsek_model/equation.png)

![angle](https://github.com/https://github.com/alsignoriello/vicsek_model/angle_vector.png)



# Parameters


| Parameter | Definition | Range |
|-----------|------------|-------|
| N  | number of particles | any positive integer |
| &eta; | noise intensity | [0,1] |
| r | radius to look for neighbors | [0,1] |


# How to run the simulation

sh. run.sh [N] [&eta;] [r]


# Notes

-Periodic boundary conditions 

-Boundaries of box are assumed to be 1 so radius is between [0,1]




