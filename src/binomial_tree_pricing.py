from math import exp
import math
import time

import numpy as np

OptionType = enum(EUROPEAN='european', AMERICAN='american')
ExerciseType = enum(CALL='call', PUT='put')

DEFAULT_BINOMIAL_TREE_NUM_STEPS = 10

   def binomial_tree(opt_type, S0, strike, up, down, yield num_steps=None):
        self.opt_type = opt_type
        self.S0 = S0
        self._yield = 1 + (yield/100)/12 
        self.strike = strike
        self.up = up
        self.down = down
       val_num_steps = num_steps or DEFAULT_BINOMIAL_TREE_NUM_STEPS
       self.prob_up = (self._yield - self.down) / (self.up - down)
       self.prob_down = 1 - self.prob_up
       val = np.asarray([0.0 for i in xrange(val_num_steps + 1)]) # initialisation
       val = np.asarray([np.maximum(self.S0 * self.up**j * self.down**(val_num_steps + 1) - self.strike, 0.0)) for j in xrange(val_num_steps + 1)]
       for i in xrange(val_num_steps - 1, -1 -1):
           val = np.asarray([(1/self._yield) * ((self.up * val[i + 1][j + 1]) + self.down * val[i + 1][j] for j in xrange(i + 1)]))
               
      return val[0][0]



        

