This repo was completed as part of the Advanced Topics in Artificial Intelligence subject taught at the Queensland University of Technology. 

The good old wumpus world game: in this repo, an intelligence agent is programmed to navigate through a mxn grid consisting of one wumpus, n pit(s) until it finds the pile of gold or run into the wumpus/pit and die. 

The locations of the wumpus and the pit(s) are generated randomly at every turn. And the agent is completely unaware of this setting. However, if the agent's current location is right next to a room with a pit, it will "feel" a breeze". Also, if the agent's current location is right to a room with the wumpus, it will "feel" and odour. 

The agent is to use these environmental cues to navigate through the maze, find the room with the pile of gold and win the game. 

This repo comes with two approach: 

- The logic approach: the agent simply "remembers" the path that it has went through. If the agent runs into a room with either a breeze or an odour, it backtracks the path one room and randomly select another path. This repeats until the agent find the room with the gold, or until it has no other option to go. 

This algorithm is written in the logic_based_move.py file. 

- The logic approach: the agents use the environment information that it has collect to "weight" the chance that a reachable room has a pit or the wumpus, and move to the room with the lowest posibility and/or below a risk threshold.  

This algorithm is written in the file. 

Probabilistic approached led to much higher survival rate compared to logic-based approach. Detailed results can be found in the report. 
