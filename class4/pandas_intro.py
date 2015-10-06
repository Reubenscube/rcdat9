# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:34:31 2015

@author: reubenkarchem
"""

import pandas as pd
pd.read_table('u.user')

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('u.user', sep='|', header=None, names=user_cols, index_col='user_id', dtype={'zip_code':str})
users
