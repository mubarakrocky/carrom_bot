from socket_client import *
import sys
from player import Player

if len(sys.argv) != 4:
    raise ValueError('The Program Accepts 3 Parameters. 1 -> Player (1/2). 2 -> Game Key. 3 -> Player Key')

player_id = sys.argv[1]
if player_id != '1' and player_id != '2':
    raise ValueError('Player ID should be 1 or 2')

player = Player(player_id)

start(player, sys.argv[2], sys.argv[3])