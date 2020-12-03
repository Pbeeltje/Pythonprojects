# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:24:06 2020

@author: P Beeltje

Russian roulette 6 gun without spinning.

"""
import random
import time

try:
    
    print("Select amount of bullets (1-6): ", end="")
    bullets = int(input())
    pick = 1
    y= 6
    tension = 0
    
    if bullets <7 and int(bullets) > 0:
    
        while bullets !=0:
            pick = random.randint(1, int(y))
            y-=1
            tension+=1
            time.sleep(1.5)
            if tension > 3 and tension <5:
                print("AAAH AAH AAH")
                time.sleep(1)
            if tension == 6: 
                print("... ... .... ...")
                time.sleep(3)
            if pick == 1:
                print("*BANG*")
                break
            else: 
                print("*click*")
            
            bullets-=1
            
            
        if pick != 1:
            time.sleep(0.2)
            print("You made it!")
            
    else: print("Incorrect bullets.")

except ValueError: print("Incorrect bullets.")