# __Author__ __Lencof__
# def Named.py

import os 
import sys

# create def Named():
def Named():
    short_list = [1, 2, 3] # your figures
while True:
    value = input('Position [q to quit?] ') # your text
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position) # your text
    except Exception as other:
        print('Something else broke:', other) # your text

Named() # Close
