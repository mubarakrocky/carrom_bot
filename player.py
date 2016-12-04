from carrom import BaseCoin
from strategy import *
import time

class Player():
    
    def __init__(self, kind):
        self.kind = kind
        self.y_range = 193.5484, 806.4516
        if kind == '1':
            self.x = 153.2258
        else:
            self.x = 846.7742
        
    def coins_factory(self, coins):
        self.coins_objects = []
        for coin in coins:
            if coin['id'] == 's1':
                continue
            coin_x = coin['x']
            coin_y = coin['y']
            if self.kind == '2':
                coin_x = 1000 - coin['x']
                coin_y = 1000 - coin['y']
            self.coins_objects.append(BaseCoin(coin['type'], coin['id'], (coin_x, coin_y)))
        self.__sort()
        
    def process(self, socket):
        print("====== coins ======")
        print(map(lambda x: (x.color, x.identifier, x.x, x.y), self.coins_objects))
        strategies = self.get_strategies()
        for strategy in strategies:
            hits = strategy(self.coins_objects)
            if(type(hits) != tuple):
                continue
            print("Got Hit ===>", hits)
            time.sleep(5)
            socket.emit('player_input', {'position': hits[0], 'force': hits[1], 'angle': hits[2]})
            break
        
    def get_strategies(self):
        return [ initail_strategy, direct_hit ]
        
    def __sort(self):
        self.coins_objects = sorted(self.coins_objects, key = self.__sort_operator)
    
    def __sort_operator(self, coin):
        if coin.color == 'black':
            return 3
        elif coin.color == 'white':
            return 2
        elif coin.color == 'red':
            return 1
        else:
            return 10
            