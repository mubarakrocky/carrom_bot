'''
Created on 02-Oct-2016

@author: mubarak
'''
from __future__ import division
from sympy import *
import math
from sympy.geometry import *



class BaseCoin:
    RADIUS_COIN=25
    RADIUS_STRIKER=30
    RADIUS_TOTAL = 55
    
    def __init__(self, color, identifier, coordinate):
        self.color = color
        self.x, self.y = coordinate
        self.center = Point(self.x, self.y)
        self.identifier = identifier
        
    def target_to_pocket(self, pocket):
        line = self.__get_the_line(pocket)
        slope = line.slope
        y_multipier = 1
        if self.y < pocket.y and self.x < pocket.x:
            y_multipier = -1
        
        if self.y > pocket.y and self.x < pocket.x:
            y_multipier = -1
        
        new_x = self.x + (BaseCoin.RADIUS_TOTAL * math.cos(slope.p/slope.q)) * y_multipier
        new_y = self.y + (BaseCoin.RADIUS_TOTAL * math.sin(slope.p/slope.q)) * y_multipier
        angle = math.degrees(math.atan(slope.p/slope.q))
#         print('slope', self.identifier, slope.p/slope.q)
        print("angle", self.identifier, angle)
        return angle, (new_x, new_y)
        
    def hitable_point(self, line):
        "TODO"
            
    def reset_coord(self, coordinate):
        self.x, self.y = coordinate
        
    def __get_the_line(self, pocket):
        return Line(pocket.center, self.center)

def line_distance_coin(test_coin, pocket, coin):
    diffx = pocket.x-test_coin.x
    diffy = pocket.y-test_coin.y
    denominator = math.sqrt(math.pow(diffy,2)+math.pow(diffx,2))
    numerator = abs(diffy*coin.x-diffx*coin.y+pocket.x*test_coin.y-pocket.y*test_coin.x)
    dist = numerator/float(denominator)
    return dist
    
    
        
        

class Pocket:
    def __init__(self, coordinate):
        self.x, self.y = coordinate
        self.center = Point(self.x, self.y)
        
        