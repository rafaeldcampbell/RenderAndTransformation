import numpy as np
from numpy import dot
import math

class Transformation:
    def __init__(self):
        print("inicio")

    @staticmethod
    def matrixShearX(x, vector):
        '''Realiza uma operação de cisalhamento na horizontal, usando as coordenadas de Vector e X como fator.'''
        print("*** Multiplicação de cisalhamento horizontal do vértice", vector.lable)
        matrixShearX = np.array([[1, x, 0, 0],
                                 [0, 1, 0, 0], 
                                 [0, 0, 1, 0], 
                                 [0, 0, 0, 1]])
        matrixVector = np.array([[vector.x],
                                 [vector.y], 
                                 [vector.z], 
                                 [1]])
        matrixResult = dot(matrixShearX, matrixVector)
        #Transformation.printMatrixMultiplication(matrixResult, matrixShearX, matrixVector)
        vector.x = matrixResult[0][0]
        vector.y = matrixResult[1][0]
        vector.z = matrixResult[2][0]
        return {"x": vector.x, "y": vector.y, "z": vector.z}
    
    @staticmethod
    def matrixShearY(x, vector):
        '''Realiza uma operação de cisalhamento na vertical, usando as coordenadas de Vector e X como fator.'''
        print("*** Multiplicação de cisalhamento vertical do vértice", vector.lable)
        matrixShearY = np.array([[1, 0, 0, 0],
                                 [x, 1, 0, 0], 
                                 [0, 0, 1, 0], 
                                 [0, 0, 0, 1]])
        matrixVector = np.array([[vector.x],
                                 [vector.y], 
                                 [vector.z], 
                                 [1]])
        matrixResult = dot(matrixShearY, matrixVector)
        #Transformation.printMatrixMultiplication(matrixResult, matrixShearY, matrixVector)
        vector.x = matrixResult[0][0]
        vector.y = matrixResult[1][0]
        vector.z = matrixResult[2][0]
        return {"x": vector.x, "y": vector.y, "z": vector.z}

    @staticmethod
    def matrixTranslationX(dx, vector):
        '''Realiza uma operação de translação na horizontal, usando as coordenadas de Vector e X como distancia.'''
        print("*** Multiplicação de translação horizontal do vértice", vector.lable)
        matrixTranslationX = np.array([[1, 0, 0, dx],
                                       [0, 1, 0, 0],
                                       [0, 0, 1, 0],
                                       [0, 0, 0, 1]])
        matrixVector = np.array([[vector.x],
                                 [vector.y], 
                                 [vector.z], 
                                 [1]])
        matrixResult = dot(matrixTranslationX, matrixVector)
        #Transformation.printMatrixMultiplication(matrixResult, matrixTranslationX, matrixVector)
        vector.x = matrixResult[0][0]
        vector.y = matrixResult[1][0]
        vector.z = matrixResult[2][0]
        return {"x": vector.x, "y": vector.y, "z": vector.z}
    
    @staticmethod
    def matrixTranslationY(dy, vector):
        '''Realiza uma operação de translação na vertical, usando as coordenadas de Vector e X como distancia.'''
        print("*** Multiplicação de translação vertical do vértice", vector.lable)
        matrixTranslationY = np.array([[1, 0, 0, 0],
                                       [0, 1, 0, dy],
                                       [0, 0, 1, 0],
                                       [0, 0, 0, 1]])
        matrixVector = np.array([[vector.x],
                                 [vector.y], 
                                 [vector.z], 
                                 [1]])
        matrixResult = dot(matrixTranslationY, matrixVector)
        #Transformation.printMatrixMultiplication(matrixResult, matrixTranslationY, matrixVector)
        vector.x = matrixResult[0][0]
        vector.y = matrixResult[1][0]
        vector.z = matrixResult[2][0]
        return {"x": vector.x, "y": vector.y, "z": vector.z}

    @staticmethod
    def oblique(vector):
        '''Realiza projeção obliqua '''
        r = math.sqrt(3)
        matrixOblique = np.array([[1,     0,   0, 0],
                                  [0,     1,   0, 0], 
                                  [r/2,   1/2, 0, 0], 
                                  [0,     0,   0, 1]])
        
        l = [vector.x, vector.y, vector.z, 1]
        matrixVector = np.array(l)
        matrixResult = dot(matrixVector, matrixOblique)
        vector.x = matrixResult[0]
        vector.y = matrixResult[1]
        vector.z = matrixResult[2]

        return {"x": vector.x, "y": vector.y, "z": vector.z}

    @staticmethod
    def isometric(vector):
        '''Realiza projeção isometrica'''
        matrixIsometric = np.array([[0.707,  0.408, 0, 0],
                                 [0,      0.816, 0, 0], 
                                 [0.707, -0.408, 0, 0], 
                                 [0,      0,     0, 1]])
        
        matrixVector = np.array([vector.x, vector.y, vector.z, 1])
        matrixResult = dot(matrixVector, matrixIsometric)
        vector.x = matrixResult[0]
        vector.y = matrixResult[1]
        vector.z = matrixResult[2]

        return {"x": vector.x, "y": vector.y, "z": vector.z}

    @staticmethod
    def trimetricX(vector):
        '''Realiza projeção trimétrica em X'''
        matrixTrimetricX = np.array([[1,  0,   0, 0],
                                 [0,  3/4, 0, 0], 
                                 [0, -1/4, 0, 0], 
                                 [0,  0,   0, 1]])
        matrixVector = np.array([vector.x,
                                 vector.y, 
                                 vector.z, 
                                 1])
        matrixResult = dot( matrixVector, matrixTrimetricX)
        vector.x = matrixResult[0]
        vector.y = matrixResult[1]
        vector.z = matrixResult[2]
        return {"x": vector.x, "y": vector.y, "z": vector.z}
        
    @staticmethod
    def trimetricZ(vector):
        '''Realiza projeção trimétrica em Z'''
        matrixTrimetricZ = np.array([[0, 1/4, 0, 0],
                                 [0, 3/4, 0, 0], 
                                 [1, 0,   0, 0], 
                                 [0, 0,   0, 1]])
        matrixVector = np.array([vector.x,
                                 vector.y, 
                                 vector.z, 
                                 1])
        matrixResult = dot( matrixVector, matrixTrimetricZ)
        vector.x = matrixResult[0]
        vector.y = matrixResult[1]
        vector.z = matrixResult[2]
        return {"x": vector.x, "y": vector.y, "z": vector.z}
    
    @staticmethod
    def dimetricXY(vector):
        '''Realiza projeção dimétrica em XY'''
        matrixDimetricXY = np.array([[2/3,  1/12, 0, 0],
                                 [0,    3/4,  0, 0], 
                                 [1/3, -1/6,  0, 0], 
                                 [0,    0,    0, 1]])
        matrixVector = np.array([vector.x,
                                 vector.y, 
                                 vector.z, 
                                 1])
        matrixResult = dot( matrixVector, matrixDimetricXY)
        vector.x = matrixResult[0]
        vector.y = matrixResult[1]
        vector.z = matrixResult[2]
        return {"x": vector.x, "y": vector.y, "z": vector.z}

    @staticmethod
    def dimetricZY(vector):
        '''Realiza projeção dimétrica em ZY'''
        matrixDimetricZY = np.array([[1/3,  1/6,  0, 0],
                                 [0,    3/4,  0, 0], 
                                 [2/3, -1/12, 0, 0], 
                                 [0,    0,    0, 1]])
        matrixVector = np.array([vector.x,
                                 vector.y, 
                                 vector.z, 
                                1])
        matrixResult = dot( matrixVector, matrixDimetricZY)
        vector.x = matrixResult[0]
        vector.y = matrixResult[1]
        vector.z = matrixResult[2]
        return {"x": vector.x, "y": vector.y, "z": vector.z}

    @staticmethod
    def dimetricXZ(vector):
        '''Realiza projeção dimétrica em XZ'''
        matrixDimetricXZ = np.array([[1/2,  1/8,  0, 0],
                                 [0,    3/4,  0, 0], 
                                 [1/2, -3/8,  0, 0], 
                                 [0,    0,    0, 1]])
        matrixVector = np.array([vector.x,
                                 vector.y, 
                                 vector.z, 
                                1])
        matrixResult = dot( matrixVector, matrixDimetricXZ)
        vector.x = matrixResult[0]
        vector.y = matrixResult[1]
        vector.z = matrixResult[2]
        return {"x": vector.x, "y": vector.y, "z": vector.z}

    @staticmethod
    def scale(escala, vector):
        '''Realiza operação de escala em um ou mais eixos simultaneamente.'''
        matrixScale = []
        if(len(escala)==1 and escala[0].isdecimal()): #caso seja definido apenas um valor, aplica a todas as dimensões
            r = float(escala[0])
            matrixScale = np.array([[r,   0,  0, 0],
                                     [0,   r,  0, 0], 
                                     [0,   0,  r, 0], 
                                     [0,   0,  0, 1]])
        else: #caso contrário
            eixos = [1, 1, 1]
            for s in escala: #identifica a dimensão e aplica a transformação
                if "x" in s:
                    eixos[0] = s.strip("x")
                if "y" in s:
                    eixos[1] = s.strip("y")
                if "z" in s:
                    eixos[2] = s.strip("z")
            eixos = [float(s) for s in eixos]

            matrixScale = np.array([[eixos[0],   0,        0,        0],
                                     [0,         eixos[1], 0,        0], 
                                     [0,         0,        eixos[2], 0], 
                                     [0,         0,        0,        1]])
                
        matrixVector = np.array([vector.x,
                                 vector.y, 
                                 vector.z, 
                                1])
        matrixResult = dot(matrixVector, matrixScale)
        Transformation.printMatrixMultiplication(matrixResult.tolist(), matrixScale.tolist(), matrixVector.tolist())
        vector.x = matrixResult[0]
        vector.y = matrixResult[1]
        vector.z = matrixResult[2]
        return {"x": vector.x, "y": vector.y, "z": vector.z}

    @staticmethod
    def printMatrixMultiplication(resultado, transformacao, original):
        '''Imprime operação de multiplicação matricial'''
        for i in range(len(resultado)):
            print(resultado[i], end="\t")
            if(i == len(resultado)/2): print("=", end="\t")
            else: print(" ", end="\t")
            for j in transformacao[i]:
                print(j, end="  ")
            if(i == len(resultado)/2): print("X", end="")
            else: print(" ", end="")
            print("  ", original[i])
        print("\n\n")