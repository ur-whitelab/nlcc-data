import numpy as np

# sides of triangle
a = 5.0
b = 7.0
c = 10.0

# semi perimeter
s = (a+b+c)/2

area = np.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)

area_codex= area_triangle(a,b,c)

# check 
if np.isclose(area, area_codex) == True:
    result = True
else:
    result = False




