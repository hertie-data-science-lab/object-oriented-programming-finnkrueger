# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Hannah
"""

from abc import ABCMeta, abstractmethod
import numpy as np
import random

class Creature(metaclass=ABCMeta):
    def __init__(self,index):
        self.index = index
    

    def move(self):
        return self.index + (random.randint(-1,1))
    
    def move_class(ind):
        return ind + (random.randint(-1,1))


Creature_1 = Creature(1)
Creature_1.move()
        
class Bear(Creature):
    def __init__(self):
        pass

Bear.move_class(2)
        
class Fish(Creature):
    pass
