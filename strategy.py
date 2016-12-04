
from carrom import Pocket,BaseCoin,line_distance_coin
import math

POCKETS = [Pocket((32.2581, 32.2581)), Pocket((967.7419 , 32.2581)), Pocket((32.2581 , 967.7419)), Pocket((967.7419 , 967.7419))]
FRONT_POCKETS = [Pocket((967.7419 , 32.2581)), Pocket((967.7419 , 967.7419))]
strikerx = 193.5454

def initail_strategy(coins):
    coins_size = len(coins)
    print("Inside the initail_strategy")
    red = coins[0]
    
    if coins_size < 19:
        return False
    
    if (red.x >= 499.5 and red.x <= 500.5) and (red.y >= 499.5 and red.y <= 500.5):
         return 193.5454, 10000, 45
     
    for pocket in FRONT_POCKETS:
        angle_counter = 0
        for coin in coins:
            if coin.color == 'black':
                continue
            angle, hitable_point = coin.target_to_pocket(pocket)
            if math.fabs(angle) > 44 and math.fabs(angle) < 46:
                angle_counter += 1
            
            if angle_counter >= 4:
                print("We have got the linear position", pocket.y)
     
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
    
    print('change_in_y_right', change_in_y_right)
    print('change_in_y_left', change_in_y_left)
    
    if change_in_y_left > 5 and (change_in_y_left < change_in_y_right or change_in_y_right == 0) and change_in_y_left < 20:
        print("Left Side Hit")
        return second_white_coin.y - 25, 10000, 90
    
    if change_in_y_right > 5 and (change_in_y_right < change_in_y_left or change_in_y_left == 0) and change_in_y_right < 20:
        print("Right Side Hit")
        return second_last_white_coin.y + 25, 10000, 90
    
    return 575, 2000, 90

def find_coin(coins, identifier):
    return [coin for coin in coins if coin.identifier == identifier][0]

def sorted_by_y_position(coins):
    return sorted(coins, key=lambda x: x.y)

def changestrikerposition(strikery):
	if strikery > 806.4516:
		strikery = 806.4516
	if strikery < 193.5484:
		strikery = 193.5484	
	return strikery

def path_finder_coin(test_coin,pocket,coins):
	flag=1
	for coin in coins:
		if coin.x >= test_coin.x-35:
			dist = test_coin.line_distance_coin(pocket, coin)
			if dist <= BaseCoin.RADIUS_COIN*2:
				flag = 0
				break
	if flag==1:
		return 1
	else:
		return 0   

def path_finder_striker(test_coin, hit_points, pocket, coins):
	coppy_coins  = copy.copy(coins)
	if pocket.x == 32.2581:
		if hity < 200 or hitx <460:
			strikery = hity+78
		else:
			strikery = 806.4516
	else :
		if hity > 700 or hitx < 460:
			strikery = hity-78
		else:
			strikery = 194
	strikery = changestrikerposition(strikery)
	while (1):
		strike_flag = 1
		for coin in coins:
			if coin['x'] > 120 and test_coin['x'] < coin['x']:
				dist = line_distance_coin({'x':strikerx,'y':strikery}, hit_points, coppy_coins)
				if dist <= (2*BaseCoin.RADIUS_STRIKER):
					strike_flag = 0
					break
		if strike_flag == 1 and strikery >=193.5484 and strikery <=806.4516 :
			return strikery
		elif pocket.x == 32.2581 and strike_flag == 0 and (strikery > hity+60 and strikery < 806.4516):
			strikery +=55
		elif pocket.x== 967.7419 and strike_flag == 0 and (strikery < hity-60 and strikery > 193.5484):
			strikery -= 55
		else:
			break
	return 0

def direct_hit(coins):
	coppy_coins = copy.copy(coins)
	for coin in coins:
		for pocket in FRONT_POCKETS:
			path_coin = path_finder_coin(coin, pocket, coppy_coins)
			if path == 1:
				angle, hit_points = target_to_pocket(coin, pocket)
				strikery = path_finder_striker(coin, hit_points, pocket, coppy_coins)
				if strikery != 0:
					###hit it sdfhgjhdjgjdfgkjxfg





	return 