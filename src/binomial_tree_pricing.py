import numpy as np
import math as m
from enum import Enum

"""
"""
class ExerciseType(object):
    EUROPEAN = 'European'
    AMERICAN = 'American'

class OptionType(object):
    CALL = 'Call'
    PUT = 'Put'

class Option:
    def __init__(self, spot, strike, _up, _down, rate, num_steps, optionType, optionExercise):
        self.spot = spot
        self.strike = strike
        self._up = _up
        self._down = _down
        self._yield = rate
        self.rate = 1 + (self._yield/100)/12
        self.prob_up = (self.rate - self._down) / (self._up - self._down)
        self.prob_down = 1 - self.prob_up
        self.num_steps = num_steps
        self.optionType = optionType
        self.optionExercise = optionExercise
    
    def binomial_pricer(self):
        stock_price = np.zeros((self.num_steps + 1, self.num_steps + 1) ) #[[0]*(self.num_steps + 1) for i in range(self.num_steps + 1)] # initialisation of stock price 2D array
        stock_price[0,0] = self.spot
        pay_off = np.zeros((self.num_steps + 1, self.num_steps + 1))
        for i in range(1, self.num_steps + 1):
            #stock_price[i, 0] = stock_price[i - 1, 0]*self._up # up node
            for j in range(0, i + 1):
               #stock_price[i, j] = stock_price[i - 1, j - 1]*self._down # down node
               stock_price[i, j] = self.spot*m.pow(self._up, i-j)*m.pow(self._down, j) # stock price
                # initialisation of pay off 2D array
          #[[0]*(self.num_steps + 1) for i in range(self.num_steps + 1)] 

        for i in range(self.num_steps + 1): # pay off for final nodes at maturity
             if self.optionType == OptionType.CALL:
                 pay_off[self.num_steps, i] = max(stock_price[self.num_steps, i] - self.strike, 0)
                 #pay_off[i][self.num_steps] = max(stock_price[i][self.num_steps] - self.strike, 0)
             else:
                 pay_off[self.num_steps, i] = max(self.strike - stock_price[self.num_steps, i], 0) 
                #pay_off[i][self.num_steps + 1] = max(self.strike - stock_price[i][self.num_steps + 1], 0.0)
        # backward recursion for option price

        for i in range(self.num_steps - 1, -1, -1):
            for j in range(i + 1):
                if self.optionExercise == ExerciseType.EUROPEAN:
                    pay_off[i, j] = (1 / self.rate)*(self.prob_up*pay_off[i + 1, j] + self.prob_down*pay_off[i + 1,j + 1])
                elif self.optionExercise == ExerciseType.AMERICAN:
                    if self.optionType == OptionType.CALL:
                        pay_off[i, j] = max(stock_price[i, j] - self.strike, (1 / self.rate)*(self.prob_up*pay_off[i + 1, j] + self.prob_down*pay_off[i + 1, j+ 1]))
                    else:
                        pay_off[i, j] = max(self.strike - stock_price[i, j]  , (1 / self.rate)*(self.prob_up*pay_off[i + 1, j] + self.prob_down*pay_off[i + 1, j + 1]))    
        return pay_off[0, 0]

