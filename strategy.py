from __future__ import division
from carrom import Pocket
import math
from sympy.geometry import *

POCKETS = [Pocket((32.2581, 32.2581)), Pocket((967.7419 , 32.2581)), Pocket((32.2581 , 967.7419)), Pocket((967.7419 , 967.7419))]
FRONT_POCKETS = [Pocket((967.7419 , 32.2581)), Pocket((967.7419 , 967.7419))]

def initail_strategy(coins):
    coins_size = len(coins)
    print("Inside the initail_strategy")
    red = coins[0]
    if coins_size < 19:
        return False
    
    if (red.x >= 499.9 and red.x <= 500.1) and (red.y >= 499.9 and red.y <= 500.1):
        return 194, 10000, 45
    
    sorted_by_y = sorted_by_y_position(coins)
    
    first_coin = sorted_by_y[0]
    last_coin  = sorted_by_y[coins_size-1]
    second_white_coin = None
    second_last_white_coin = None
    if first_coin.color == 'white':
        for coin in sorted_by_y:
            if coin.color != 'white' or coin == first_coin:
                continue
            second_white_coin = coin
            break
    
    if last_coin.color == 'white':
        for coin in sorted_by_y:
            if coin.color != 'white' or coin == last_coin:
                continue
            second_last_white_coin = coin
            
    change_in_y_left = 0
    change_in_y_right = 0
    if first_coin.color == 'white':
        change_in_y_left = second_white_coin.y - first_coin.y
        
    if last_coin.color == 'white':
        change_in_y_right = last_coin.y - second_last_white_coin.y
    
    if change_in_y_left > 5 and (change_in_y_left < change_in_y_right or change_in_y_right == 0) and change_in_y_left < 20:
        print("Left Side Hit")
        return second_white_coin.y - 25, 10000, 90
    
    if change_in_y_right > 5 and (change_in_y_right < change_in_y_left or change_in_y_left == 0) and change_in_y_right < 20:
        print("Right Side Hit")
        return second_last_white_coin.y + 25, 10000, 90
    
    return 575, 1000, 90

def find_coin(coins, identifier):
    return [coin for coin in coins if coin.identifier == identifier][0]

def sorted_by_y_position(coins):
    return sorted(coins, key=lambda x: x.y)

def sorted_by_x_position(coins):
    return sorted(coins, key=lambda x: x.x)
    
    