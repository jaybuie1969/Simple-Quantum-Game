# Simple-Quantum-Game
A very simple quantum computing circuit that can be used as a simple game to demonstrate probability.  If the circuit run returns a zero, the player loses; if it returns a one, the player wins.

I was doing this mainly as a response to a math class project for my fifth-grade son.  He had to create a game where there was a non-equal probability of chance of winning or losing.  I thought it might be fun to do the same thing.

The game uses a single qubit and the name of the game's file, "hth.py" is a hint at what is done to it.  A Hadamard - T - Hadamard series of gates is applied to the qubit.  The details of the computations are left "as an exercise to the student," but to summarize, there is an 85.3% chance of the qubit's final state being a zero and a 14.7% chance of it being a one.  Hint - brush up on your trigonometry identities, because 1 + exp(i * theta) comes into play.
