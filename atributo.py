

class Atributo:

    def __init__(self, parName):
        self.values = []
        self.informationGain = 0.0
        self.name = parName
        self.subdataset = []
        self.isitclass = False


    def setinformationGain(self,parinfoGain):
        self.informationGain = parinfoGain
        return

    def setvalues(self,parArrayvalues):
        self.values = parArrayvalues
        return

    def insertValue(self,parvalue):
        self.values.append(parvalue)
        return

    def setsubdataset(self,pardataset):
        self.subdataset = pardataset
        return

    def getsubdataset(self):
        return self.subdataset

    def getName(self):
        return self.name

    def getInformationGain(self):
        return self.informationGain


    def setClasses(self,fulldataset):  # quantas classes possui?
        classesDistintas = []
        todasclasses = []
        for linha in fulldataset:
            todasclasses.append(linha[self.name])
            if (linha[self.name]) not in classesDistintas:
                classesDistintas.append(linha[self.name])
        self.values = classesDistintas
        return