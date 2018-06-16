# jeu-de-labyrinthe

This is a labyrinth game project developped for the Open Classrooms course "Apprenez à programmer en Python"

There are two scenarios for the game (cartes):
- facile (easy)
- prison (prission)

The player is a robot identified with the symbol "X", the obstacles are the "O" symbols, the gates are "." and the exit of the labyrinth is "U"

The player moves with the following commands:
- N : up
- S : down
- O : lef
- E : right
These commands can also be used followed by a number to move the robot several positions. For example:

S3

this command moves the robot 3 positions down

"Q" is to quit the game

In order to execute the game, place yourself into the folder of the project and execute in the command line:
>python roboc.py