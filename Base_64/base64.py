###-------------base64-----------###

""" Test Body"""

import cmprs 
import math

x = input ("type your method:")
x = str(x)

xr = 64000

""".........separate function.............."""
'''e = cmprs.separate(x,xr)
print ('\n',e,'\n\n')'''

""".........encode's function..............."""
y = cmprs.encode(x)
print ("encode :",y , '\n')
print ("lenght of encode :",len(y),'\n')

R_T = math.tan(xr)
print (R_T)

""".........decode's function.............."""
z = cmprs.decode(y)
print ("decode :",z)
G = math.cos(xr)
print (G)
""".........compress function..............."""

x = open.file('fire.mp4',r)

x = str(x)

