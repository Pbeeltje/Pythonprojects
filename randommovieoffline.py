# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 00:33:06 2020

@author: P Beeltje

picks random movie from excel sheet

"""


from openpyxl import load_workbook


import random

wb = load_workbook('BroMovies.xlsx')

sheet = wb['movies']

count = 0
x = 2

while True:
    cell = 'A'+ str(x)
    if sheet[cell].value is not None:
        count += 1
        x+=1
    else: break

print ('Total Movie Count: ', count)
    

#get random movie title 

cellnum = random.randrange(3, count)
randomMovie = 'A' + str(cellnum)
randomDes = 'H' + str(cellnum)
randomSnr = 'C' + str(cellnum)

print('Entry Number: ', sheet[randomSnr].value)
print('Title: ', sheet[randomMovie].value)
if sheet[randomDes].value is None: print('No Description')
else: print('Description: ', sheet[randomDes].value)

#for cellObj in sheet['A1':'C8']:
#      for cell in cellObj:
#              print(cell.value)
      #print('--- END ---')



