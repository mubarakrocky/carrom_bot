'''
Created on 02-Oct-2016

@author: mubarak
'''
from sympy import *
import math
from sympy.geometry import *

if __name__ == '__main__':
    pass


class BaseCoin:
    RADIUS = 25
    
    def __init__(self, color, identifier, coordinate):
        self.color = color
        self.x, self.y = coordinate
        self.center = Point(self.x, self.y)
        self.identifier = identifier
        
    def target_to_pocket(self, pocket):
        line = self.__get_the_line(pocket)
        slope = line.slope
        
        new_x = self.x + (BaseCoin.RADIUS * math.cos(slope))
        new_y = self.y + (BaseCoin.RADIUS * math.sin(slope))
        print(slope)
        print(new_x)
        print(new_y)
        
    def hitable_point(self, line):
        "TODO"
        
            
    def reset_coord(self, coordinate):
        self.x, self.y = coordinate
        
    def __get_the_line(self, pocket):
        return Line(pocket.center, self.center)
    
    
        
        

class Pocket:
    def __init__(self, coordinate):
        self.x, self.y = coordinate
        self.center = Point(self.x, self.y)
        
        