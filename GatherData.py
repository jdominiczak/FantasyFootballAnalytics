# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:50:36 2015

@author: jdomini6
"""

import FFToday
import FantasyPros
import Fox
import CBS
import pandas as pd


#FFTpreds = FFToday.getAllProjections("5")
FPpreds = FantasyPros.getAllProjections("5")
FoxPreds = Fox.getAllProjections("5")
CBSPreds = CBS.getAllProjections("5")

data = pd.concat([FPpreds, FoxPreds, CBSPreds], ignore_index=False)
data.fillna("0", inplace=True)
for col in data.columns:
    data[col] = data[col].astype('str')
    