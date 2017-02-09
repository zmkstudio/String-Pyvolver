# String-Pyvolver
Using an evolutionary algorithm coupled with methods of genetic programming, this python program evolves a random string into my name over a series of generations.

This code is a work in progress as I explore genetic programming and experiment with different evolutionary techniques.

# Crossover
The crossover method implemented in the code generates a random parent string for the existing string to "crossover" with and produce a child.
The DNA of the existing string that is used for crossover is determined by the beginning of the string to a randomly chosen position in the string.
The randomly generated parent's shared DNA becomes the randomly chosen position to the end of the parent's string.
For example, if the strings "banana" and "orange" are the strings undergoing crossover and the randomly chosen position is '4', the child will be "banage".

# Testing
2/19/2017

Employing the combination of crossover and mutation, the program took 20,000-30,000 generations to properly evolve my name.
The program fell to 3,000-4,000 generations upon omitting crossover and only applying mutation.
