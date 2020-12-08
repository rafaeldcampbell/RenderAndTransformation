from elements import *
import csv

class EstructuredObject:
    def __init__(self, vertexFileName, facesFileName):
        self.vertexFileName = vertexFileName
        self.facesFileName = facesFileName
        self.vertexDict = dict()
        self.faceDict = dict()
        self.getVertexDict()
        self.getFaceDict()
        
    def getVertexDict(self):
        try: #primeiro teste, abre com arquivo definido
            file_csv = open(self.vertexFileName, "r")
        except:
            print("Erro ao abrir arquivo de vértices.")
            return -1
        reader = csv.reader(file_csv, delimiter=",")
        for line in reader:
            self.vertexDict[line[0]] = Vertex(line[0], int(line[1]), int(line[2]), int(line[3]))

    def getFaceDict(self):
        try:#primeiro teste, abre com o arquivo definido
            file_csv = open(self.facesFileName, "r")
        except:
            print("Erro ao abrir arquivo de vértices.")
            return -1
        reader = csv.reader(file_csv, delimiter=",")
        for line in reader:
            if (len(line)==5):
                self.faceDict[line[0]] = Face(line[0], 
                                            line[4] if len(line) > 4 else "FF00FF", #cor padrão
                                            self.vertexDict.get(line[1]),
                                            self.vertexDict.get(line[2]),
                                            self.vertexDict.get(line[3]),
                                            )
            elif (len(line)==6):
                self.faceDict[line[0]] = Face(line[0], 
                                            line[5] if len(line) > 5 else "FF00FF", #cor padrão
                                            self.vertexDict.get(line[1]),
                                            self.vertexDict.get(line[2]),
                                            self.vertexDict.get(line[3]),
                                            self.vertexDict.get(line[4]),
                                            ) 

    def printFaceDict(self):
        for val in self.faceDict.values():
            print(val)

    def printVertexDict(self, dictElement):
        for val in self.vertexDict.values():
            print(val)