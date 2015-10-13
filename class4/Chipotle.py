# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:41:11 2015

@author: reubenkarchem
"""

with open('chipotle.tsv', 'rU') as f:
    data = []
    for row in f:        
        data.append(row)

    
data[5]