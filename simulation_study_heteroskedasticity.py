# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:36:10 2023

@author: manfr
"""

import numpy as np
import numpy.linalg as la
# for ploting
import matplotlib.pyplot as plt
# for econometric modells (OLS)
import statsmodels.api as sm
# for quantiles
import scipy.stats as stats

#first birthday
bd_1 = 0803
#second birthday
bd_2 = 2507
group_seed = bd_1 ∗ bd_2
#seed for the random generator
rng = np.random.default_rng(group_seed)
