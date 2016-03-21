# Vicsek Model


The Vicsek model is a mathematical model that illustrates the collective motion of particles. The dynamics of the particles in them model depend on the particle density and instensity of noise in the system. Every particle in the model is initialized with a random angle &theta; between [-&pi;, &pi;]. At every time step, the particle will find all of its neighbor particles, defined as any particle within a specified radius r. It will average its angle vector with all of its neighbors. The particle will then move in the direction of the new angle plus a random perturbation. The instensity of the random perturbation is defined by &eta;.


<img src="https://github.com/alsignoriello/vicsek_model/blob/master/images/r1.jpg" style="float: left;" height="350" width="400"><img src="https://github.com/alsignoriello/vicsek_model/blob/master/images/r2.jpg" style="float: right;" height="350" width="400">


Vicsek, T., Czirók, A., Ben-Jacob, E., Cohen, I. & Shochet, O. Novel Type of Phase Transition in a System of Self-Driven Particles. Phys. Rev. Lett. 75, 1226–1229 (1995).

# Equations

v&#770;(t + 1) = < v&#770;(t) ><sub> r </sub>  + &eta;&#770;

&eta;&#770; = (cos &theta;, sin &theta; )



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

-Boundaries of box are assumed to be 1



# Requirements

numpy (1.8.1)

matplotlib (1.3.1)



