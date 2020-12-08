from vpython import vec
from color import Color
from enum import Enum

cores = {"red" : vec(1,0,0),"yellow" : vec(1,1,0),"black" : vec(0,0,0),"green" : vec (0,1,0), "orange" : vec(1,0.6,0),  "white" : vec(1,1,1),"blue" : vec(0,0,1),"cyan" : vec(0,1,1),"purple" : vec(0.4,0.2,0.6), "magenta" : vec(1,0,1)}

color = Color("#ffffff")
print(color)
color.change_color_from_hex("#ff00ff")
print(color)
# for key in cores:
#     print(key, end=" ")
#     color.change_color_from_vec(cores[key])
#     print(color)

