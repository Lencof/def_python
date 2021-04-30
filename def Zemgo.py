# __Author__ __Lencof__
# def Zemgo.py

import os # use os 
import sys

# create def Zemgo():
def Zemgo():
    short_list = [1, 2, 3] # your text
while True:
    value = input('Position [Lencof to quit?] ') # your text
    if value == 'Lencof': # your text
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position) # your text
    except Exception as other:
        print('Something else broke:', other) # your text

Zemgo() # Close
