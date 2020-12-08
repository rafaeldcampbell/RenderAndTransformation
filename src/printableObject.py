# Via Python local
import sys
import getopt
from vpython import *
from enum import Enum
from elements import *
from estructuredObject import *
from color import Color
import copy
import os
import time

originalRange = 1

# GlowScript 3.0 VPython

class printableObject():
    def __init__(self, vertexFile, faceFile):
        self.estructureObject = EstructuredObject(vertexFile, faceFile)
        self.drawLights()
        self.triangleList = []
        self.quadList = []
        self.vertexsList = list(self.estructureObject.vertexDict.values())
        self.vertexDictDefault = copy.deepcopy(self.estructureObject.vertexDict)

    def getTriangleFromFace(self, face, col, faceId):
        '''Recebe uma face e uma cor, retornando um triângulo'''
        a = vertex(pos=vec(face.vertexs[0].x, face.vertexs[0].y, face.vertexs[0].z), color=col)
        b = vertex(pos=vec(face.vertexs[1].x, face.vertexs[1].y, face.vertexs[1].z), color=col)
        c = vertex(pos=vec(face.vertexs[2].x, face.vertexs[2].y, face.vertexs[2].z), color=col)
        return triangle(v0=a, v1=b, v2=c, my_id=faceId)

    def getQuadFromFace(self, face, col, faceId):
        '''Recebe uma face e uma cor, retornando um quadrado'''
        a = vertex(pos=vec(face.vertexs[0].x, face.vertexs[0].y, face.vertexs[0].z), color=col)
        b = vertex(pos=vec(face.vertexs[1].x, face.vertexs[1].y, face.vertexs[1].z), color=col)
        c = vertex(pos=vec(face.vertexs[2].x, face.vertexs[2].y, face.vertexs[2].z), color=col)
        d = vertex(pos=vec(face.vertexs[3].x, face.vertexs[3].y, face.vertexs[3].z), color=col)
        return quad(v0=a, v1=b, v2=c, v3=d, my_id=faceId)

    def drawObject(self):
        '''Desenha o objeto interno com base em sua lista de faces, retornando a lista de triangulos ou quadrados'''
        faces = list(self.estructureObject.faceDict.values())
        print(faces[0].typeOfFace)
        if (faces[0].typeOfFace == "triangulo"):
            for i in range(len(faces)-1, -1, -1):
                face = faces[i]
                self.triangleList.append(self.getTriangleFromFace(
                                        face, 
                                        Color.convert_hex_to_rgbdecimal(face.color), 
                                        list(self.estructureObject.faceDict.keys())[faces.index(face)]
                                        ))
        elif (faces[0].typeOfFace == "quadrado"):
            for i in range(len(faces)-1, -1, -1):
                face = faces[i]
                self.quadList.append(self.getQuadFromFace(
                                        face, 
                                        Color.convert_hex_to_rgbdecimal(face.color), 
                                        list(self.estructureObject.faceDict.keys())[faces.index(face)]
                                        ))
    
    def drawLights(self):
        '''Ajusta luzes em vários pontos, para reduzir efeito de luz focal'''
        scene.lights = []
        #face frontal
        distant_light(direction=vector( 0.22,  0.44,  0.88), color=color.gray(0.2))
        distant_light(direction=vector( 0,  0.22,  0.44), color=color.gray(0.2))
        distant_light(direction=vector( 0,  0,  0.22), color=color.gray(0.2))
        distant_light(direction=vector( 0.88, 0.22,  0.44), color=color.gray(0.2))
        distant_light(direction=vector( 0.44, 0,  0.22), color=color.gray(0.2))
        distant_light(direction=vector( 0.22, 0,  0), color=color.gray(0.2))
        distant_light(direction=vector( 0.44, 0.88, 0.22), color=color.gray(0.2))
        distant_light(direction=vector( 0.22, 0.44, 0), color=color.gray(0.2))
        distant_light(direction=vector( 0, 0.22, 0), color=color.gray(0.2))
        #face traseira
        distant_light(direction=vector( -0.22,  -0.44,  -0.88), color=color.gray(0.2))
        distant_light(direction=vector( -0,  -0.22,  -0.44), color=color.gray(0.2))
        distant_light(direction=vector( -0,  -0,  -0.22), color=color.gray(0.2))
        distant_light(direction=vector( -0.88, -0.22,  -0.44), color=color.gray(0.2))
        distant_light(direction=vector( -0.44, -0,  -0.22), color=color.gray(0.2))
        distant_light(direction=vector( -0.22, -0,  -0), color=color.gray(0.2))
        distant_light(direction=vector( -0.44, -0.88, -0.22), color=color.gray(0.2))
        distant_light(direction=vector( -0.22, -0.44, -0), color=color.gray(0.2))
        distant_light(direction=vector( -0, -0.22, -0), color=color.gray(0.2))

    def shearX(self, n):
        '''Faz o cisalhamento horizontal'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].shearX(n)
    
    def shearY(self, n):
        '''Faz o cisalhamento vertical'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].shearY(n)

    def moveY(self, n):
        '''Faz uma translação na vertical'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].translationY(n)

    def moveX(self, n):
        '''Faz uma translação na horizontal'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].translationX(n)

    def oblique(self):
        '''Faz o cisalhamento horizontal'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].oblique()

    def isometric(self):
        '''Faz o cisalhamento horizontal'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].isometric()
    
    def trimetricX(self):
        '''Faz o cisalhamento horizontal'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].trimetricX()
    
    def trimetricZ(self):
        '''Faz o cisalhamento horizontal'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].trimetricZ()
    
    def dimetricXY(self):
        '''Faz o cisalhamento horizontal'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].dimetricXY()
    
    def dimetricZY(self):
        '''Faz o cisalhamento horizontal'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].dimetricZY()
    
    def dimetricXZ(self):
        '''Faz o cisalhamento horizontal'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].dimetricXZ()

    def scale(self, escala):
        '''Faz mudança de escala'''
        for i in range(len(self.vertexsList)):
            x = self.vertexsList[i].scale(escala)

    def setDefaultState(self):
        for k in self.estructureObject.vertexDict.keys():
            self.estructureObject.vertexDict[k].x = self.vertexDictDefault[k].x
            self.estructureObject.vertexDict[k].y = self.vertexDictDefault[k].y
            self.estructureObject.vertexDict[k].z = self.vertexDictDefault[k].z
            
    def update(self):
        '''Atualiza a imagem na tela com base nos valores do objeto estruturado atual'''
        faces = self.estructureObject.faceDict
        for i in range(len(self.triangleList)):
            estructuredFaces = faces[self.triangleList[i].my_id]
            for j in range(len(estructuredFaces.vertexs)):
                posXYZ = estructuredFaces.vertexs[j].getXYZ()
                self.triangleList[i].vs[j].pos = vec(posXYZ[0], posXYZ[1], posXYZ[2])
                
    def animation(self, totalScale, step, totalTime, opt):
        '''Iniciar animaçao do obejto'''
        print("***Inicio da animaçao***")
        timeStep = totalTime / (2*step) #define o tempo de espera em cada step
        scaleStep = (totalScale-1) / step #define a variação de escala (com relação ao original) para cada step
        for i in range(0,step):
            currentStepScale = (scaleStep * i) + 1
            aux = str(currentStepScale)+"y"
            self.scale(aux.split())
            self.isometric()
            self.update()
            self.setDefaultState()
            time.sleep(timeStep)
            if(opt == "s"):
                input()
        for i in range(step-1,-1,-1):
            currentStepScale = (scaleStep * i) + 1
            aux = str(currentStepScale)+"y"
            self.scale(aux.split())
            self.isometric()
            self.update()
            self.setDefaultState()
            time.sleep(timeStep)
            if(opt == "s"):
                input()
        print("Fim da animaçao")

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths  # Self-explanatory.

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main(argv):
    scene=canvas(title='Cenário padrão',x=0,y=0,width=1200,height=550)
    global originalRange
    originalRange = scene.range
    files = menuInicial()
    objImpresso = printableObject(files["v"], files["f"])
    objImpresso.drawObject()
    opt = 1
    while(opt != 0):
        opt = int(menu(objImpresso, scene))
    scene.title = "Feche a janela ou use Ctrl+W para sair"
    scene.delete() #deleta os objetos e o cenário


    

def menuInicial():
    ''' Observa os objetos definidos na pasta \objetos e pergunta ao usuário qual deles deve ser desenhado.'''
    
    dir = "./objetos"
    objetos = os.listdir(dir)
    print("\nEscolha o objeto a ser desenhado\n")
    for i in range(len(objetos)): #imprime opções em tela
        print("{} - {}".format(i, objetos[i]))
    print("Opção:", end="")

    obj = input() #recupera a opção escolhida
    while (not(obj.isdecimal()) or int(obj)<0 or int(obj)>len(objetos)): #trata entradas inválidas
        print("\nTente novamente!\n")
        for i in range(len(objetos)):
            print("{} - {}".format(i, objetos[i]))
        print("Opção:", end="")
        obj = input()

    dir = dir+"/"+objetos[int(obj)]
    filePaths = get_filepaths(dir) #recupera diretório com base no objeto escolhido
    files={}
    if "Vertex" in filePaths[0]:
        files["v"] = filePaths[0]
        files["f"] = filePaths[1]
    else:
        files["v"] = filePaths[1]
        files["f"] = filePaths[0]
    clear()
    return files
    
def menu(casa, scene):
    print("\nEscolha uma opção:\n1 - Cisalhamento\n2 - Translação\n3 - Fazer uma projeção\n4 - Mudança de escala\n5 - Iniciar animacao do objeto\n6 - Voltar ao original\n0 - Sair\nOpção:", end="")
    opt = input()
    print()
    if(not opt.isdecimal()):
        print("Tente novamente!")
        return -1
    opt = int(opt)
    if(opt == 1):
        try:
            shear(casa)
        except:
            print("Tente novamente!")
            return -1
        return 1
    if(opt == 2):
        try:
            translation(casa)
        except:
            print("Tente novamente!")
            return -1
        return 2
    if(opt == 3):
        try:
            projection(casa)
        except:
            print("Tente novamente!")
            return -1
        return 3
    if(opt == 4):
        try:
            scale(casa)
        except:
            print("Tente novamente!")
            return -1
        return 4
    if(opt == 5):
        scale = input("Entre com a escala desejada em Y: ")
        frames = input("Entre com o numero de frames: ")
        timeStep = input("Entre com tempo total em segundos: ")
        opt = input("Deseja executar frame a frame (s/n)? ")
        try:
            casa.isometric() #projea
            casa.update()
            scale = float(scale)
            frames = int(frames)
            timeStep = int(timeStep)
            scene.userzoom = False #desativa o zoom manual
            scene.userspin = False #desativa a rotação manual
            for i in range(2, int(scale)+2): #efeito de zoom out
                scene.range = originalRange * i
                casa.update
                time.sleep(0.2)
            
            casa.setDefaultState() #volta ao estado original
            casa.animation(scale, frames, timeStep, opt) #realiza escala 10y em 100 quadros ao longo de 10 segundos

            for i in range(int(scale)+1, 1, -1): #efeito de zoom in
                scene.range = originalRange * i
                casa.update
                time.sleep(0.2)
        except:
            print("Tente novamente!")
            return -1
        scene.userzoom = True #reativa o zoom manual
        scene.userspin = True #reativa a rotação manual
        casa.setDefaultState()
        return 5
    if(opt == 6):
        casa.setDefaultState()
        casa.update()
        return 6
    if(opt != 0):
        return -1 #opção indisponivel
    return 0 #sair

def projection(casa):
    print("\n1 - obliquo 30 graus\n2 - trimetrica |X| = 1 tetaX = 30\n3 - trimetrica |Z| = 1 tetaX = 30\n4 - dimetrica X=Y e tetaX = 30\n5 - dimetrica Z=Y e tetax = 30\n6 - dimetrica X=Z e tetaX = 30\n7 - Isometrica\n8 - Voltar\nOpção:", end="")
    opt = input()
    print()
    if(not opt.isdecimal()):
        print("Tente novamente!")
        return -1
    opt = int(opt)
    if(opt == 1):
        try:
            casa.oblique()
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 1
    if(opt == 2):
        try:
            casa.trimetricX()
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 2
    if(opt == 3):
        try:
            casa.trimetricZ()
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 5
    if(opt == 4):
        try:
            casa.dimetricXY()
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 4
    if(opt == 5):
        try:
            casa.dimetricZY()
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 5
    if(opt == 6):
        try:
            casa.dimetricXZ()
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 6
    if(opt == 7):
        try:
            casa.isometric()
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 7
    if(opt != 0):
        return -1 #opção indisponivel
    return 0 #sair

def scale(casa):
    print("\nPara fazer a mudança de escalas, digite apenas um número caso queira alterar todas de uma vez\nou escreva o numero concatenado com o eixo para fazer a mudança apenas naquele eixo")
    print("\nExemplo:\nDigite \"100\"      para alterar a escala de todos os eixos simultaneamente\nDigite \"100x 20y\" para alterar a escala em X e Y")
    print("\n0 - Voltar\nOpção:", end="")
    opt = input()
    print()
    if(opt != "0" and len(opt)>0):
        try:
            casa.scale(opt.split())
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 1
    return 0 #sair

def shear(casa):
    print("\n1 - Cisalhamento horizontal\n2 - Cisalhamento vertical\n0 - Voltar\nOpção:", end="")
    opt = input()
    print()
    if(not opt.isdecimal()):
        print("Tente novamente!")
        return -1
    opt = int(opt)
    if(opt == 1):
        print("Digite um fator: ")
        factor = input()
        try:
            casa.shearX(float(factor))
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 1
    if(opt == 2):
        print("Digite um fator: ")
        factor = input()
        try:
            casa.shearY(float(factor))
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 2
    if(opt != 0):
        return -1 #opção indisponivel
    return 0 #sair
    
def translation(casa):
    print("\n1 - Translação horizontal\n2 - Translação vertical\n0 - Voltar\nOpção:", end="")
    opt = input()
    print()
    if(not opt.isdecimal()):
        print("Tente novamente!")
        return -1
    opt = int(opt)
    if(opt == 1):
        print("Digite uma distancia: ")
        dist = input()
        try:
            casa.moveX(float(dist))
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 3
    if(opt == 2):
        print("Digite uma distancia: ")
        dist = input()
        try:
            casa.moveY(float(dist))
            casa.update()
        except:
            print("Tente novamente!")
            return -1
        return 4
    if(opt != 0):
        return -1 #opção indisponivel
    return 0 #sair


if __name__ == "__main__":
    main(sys.argv[1:])