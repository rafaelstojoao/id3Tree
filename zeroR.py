import csv

class zeroR:
    def __init__(self):
        self.datasetName    = ""
        self.dataset        = []
        self.attClass       = -1
        self.attNames       = []
        self.allClasses     = []
        self.dictClasses    = {}
        self.model          = {}


    def setattClass(self,indexClass):
        self.attNames=indexClass
        return


    def loadData(self,nameDataset):
        with open(nameDataset, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.dataset = list(reader)
            self.attNames = reader.fieldnames
        return

    def setClasses(self):  # quantas classes possui?
        for linha in self.dataset:
            self.allClasses.append(linha[self.attNames[self.attClass]])

            if (linha[self.attNames[self.attClass]]) not in self.dictClasses:
                self.dictClasses.update({ linha[self.attNames[self.attClass]]:1} )

            else:
                self.dictClasses[linha[self.attNames[self.attClass]]] += 1
        return

    def generateModel(self):
        # Using the most frequent class to generate a model
        maxi = max(self.dictClasses, key=self.dictClasses.get)
        print("Model: \n ",self.attNames[self.attClass],"=>",maxi)



if __name__ == '__main__':
    zz= zeroR()
    zz.setattClass(4)
    zz.loadData('datasetPlayTenis.csv')
    zz.setClasses()
    zz.generateModel()
    print(zz.dictClasses)




