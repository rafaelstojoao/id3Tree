
class Atributos:
    def __init__(self):
        self.qtdValores = 0
        self.listaValores = []


    def entropy(self):
       for val in outlook:
            print(val)


    def setQuantidadeValores(self,atributo):
        valores = []
        for val in atributo:
            if val not in valores:
                valores.append(val)
                self.qtdValores+=1

    def getQuantidadeValores(self):
        return self.qtdValores


    def setValores(self, atributo):
         for val in atributo:
            if val not in self.listaValores:
                self.listaValores.append(val)

    def getValores(self):
        return self.listaValores


    def entropy(self):



at = Atributos()
outlook = ['rainy','sunny','rainy','rainy','sunny','overcast','rainy']


at.setQuantidadeValores(outlook)
print(at.getQuantidadeValores())

at.setValores(outlook)
print(at.getValores())




