from math import trunc
from vpython import vec

class Color():
    red = vec(1,0,0)
    yellow = vec(1,1,0)
    black = vec(0,0,0)
    green = vec (0,1,0)
    orange = vec(1,0.6,0)
    white = vec(1,1,1)
    blue = vec(0,0,1)
    cyan = vec(0,1,1)
    purple = vec(0.4,0.2,0.6)
    magenta = vec(1,0,1)
    
    @staticmethod
    def convert_hex_to_rgbdecimal(colorhex):
        colorhex = colorhex.lstrip('#')
        colorrgb = tuple(int(colorhex[i:i+2], 16)/255 for i in (0, 2, 4))
        return vec(colorrgb[0], colorrgb[1], colorrgb[2])

    def __init__(self, hexValue = "FFFFFF"):
        self.change_color_from_hex(hexValue)
    
    def hex_to_rgb(cls):
        hexValue = cls.hexValue.lstrip('#')
        return tuple(int(hexValue[i:i+2], 16) for i in (0, 2, 4))

    def rgb_normalized(cls):
        value = list(cls.rgb)
        fact = 100
        for i in range(3):
            value[i] /= 255
            value[i] = trunc(value[i]*fact)/fact
        return tuple(value)
    
    def rgb_normalized_to_vec(cls):
        return vec(cls.rgbNormalized[0], cls.rgbNormalized[1], cls.rgbNormalized[2])
    
    def rgb_unormalized(cls):
        value = list(cls.rgbNormalized)
        
        for i in range(3):
            value[i]*=255
        cls.rgb = tuple(value)
    
    def vec_to_tuple(cls):
        cls.rgbNormalized = (cls.vec.x, cls.vec.y, cls.vec.z)
    
    def rgb_to_hex(cls):
        cls.hexValue = '#%02x%02x%02x' % (int(cls.rgb[0]), int(cls.rgb[1]), int(cls.rgb[2]))
    
    def change_color_from_vec(self, vec):
        self.vec = vec
        self.vec_to_tuple()
        self.rgb_unormalized()
        self.rgb_to_hex()
    
    def change_color_from_hex(self, hexValue):
        self.hexValue = hexValue
        self.rgb = self.hex_to_rgb()
        self.rgbNormalized = self.rgb_normalized()
        self.vec = self.rgb_normalized_to_vec()
        
    def __str__(self):
        return str(self.hexValue) + " " + str(self.rgb) + " " + str(self.rgbNormalized) + " " + str(self.vec)