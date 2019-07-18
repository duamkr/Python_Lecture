# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 00:49:47 2019

@author: OH
"""

korean, english, math, science = map(int, input().split()) 
print(korean >= 90 and english > 80 and math > 85 and science >= 80)