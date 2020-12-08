import numpy as np
from numpy import dot
from transformation import Transformation

class Vertex:
    def __init__(self, lable, x, y, z):
        self.lable = lable
        self.x = x
        self.y = y
        self.z = z

    def invert(self):
        if (self.x > 0):
            self.x *= -1

    def normalize(self):
        if (self.x < 0):
            self.x *= -1

    def getXYZ(self):
        return (self.x, self.y, self.z)

    def shearX(self, number):
        Transformation.matrixShearX(number, self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def shearY(self, number):
        Transformation.matrixShearY(number, self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def translationX(self, number):
        Transformation.matrixTranslationX(number, self)
        return {"x": self.x, "y": self.y, "z": self.z}
    
    def translationY(self, number):
        Transformation.matrixTranslationY(number, self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def oblique(self):
        Transformation.oblique(self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def isometric(self):
        Transformation.isometric(self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def trimetricX(self):
        Transformation.trimetricX(self)
        return {"x": self.x, "y": self.y, "z": self.z}
    
    def trimetricZ(self):
        Transformation.trimetricZ(self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def dimetricXY(self):
        Transformation.dimetricXY(self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def dimetricZY(self):
        Transformation.dimetricZY(self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def dimetricXZ(self):
        Transformation.dimetricXZ(self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def scale(self, escala):
        Transformation.scale(escala, self)
        return {"x": self.x, "y": self.y, "z": self.z}

    def __str__(self):
        return self.lable+ "= ("+ str(self.x) + ","+ str(self.y)+ ","+ str(self.z)+ ")"

class Face:
    def __init__(self, lable, color, *vertex):
        self.lable = lable
        self.vertexs = vertex
        self.color = color
        self.typeOfFace = "triangulo" if len(vertex)==3 else "quadrado"

    def invert(self):
        for v in self.vertexs:
            v.invert()

    def normalize(self):
        for v in self.vertexs:
            v.normalize()

    def getVertex(self):
        return vex(self.vertexs)

    def __str__(self):
        faceDesc = str(self.lable) + "=(" + str(self.vertexs[0])
        for i in range(1, len(self.vertexs)):
            faceDesc = faceDesc + "," + str(self.vertexs[i])
        faceDesc += ") em "+ self.color
        return faceDesc