import csv
import math
import atributo


atClass = 4
entropiaS = 0.0
valores =[]
ganhoAtrib = {}
classesPossiveis = 0

arr_Atributes = []

with open('datasetPlayTenis.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    dataset = list(reader)
    nomesAtributos = reader.fieldnames


def getQtdValoresClasses():    # quantas classes possui?
    classesDistintas = []
    todasclasses = []
    for linha in dataset:
        todasclasses.append(linha[nomesAtributos[atClass]])
        if (linha[nomesAtributos[atClass]]) not in classesDistintas:
            classesDistintas.append(linha[nomesAtributos[atClass]])
    return classesDistintas, todasclasses


def entropiasistema():  # Calcular a entropia geral
    entropiaS = 0.0
    classesDistintas, todasclasses = getQtdValoresClasses()
    cl_qtdPorClasso =[]
    for i in range(len(classesDistintas)):
        cl_qtdPorClasso.append(todasclasses.count(classesDistintas[i]))
        entropiaS -= (cl_qtdPorClasso[i]/len(dataset))*math.log(cl_qtdPorClasso[i]/len(dataset),2)
    return round(entropiaS,4)



def getGanhoAtributo(indice,classesPossiveis,entropiaSistema): # para cada atributo do indice pegar as possibiliades
    possibilidades = []
    todasPossibilidades = []
    poss_qtdPor = []
    amostraPossibPorClasse = []

    ganhoAtributo = entropiaSistema

    for linha in dataset:
        todasPossibilidades.append(linha[nomesAtributos[indice]])
        if (linha[nomesAtributos[indice]]) not in possibilidades:
            possibilidades.append(linha[nomesAtributos[indice]])



    for valorAtributo in possibilidades: #para cada possibilidade que o atributo pode assumir
        poss_qtdPor.append(todasPossibilidades.count(valorAtributo))
        #para cada uma das possibilidades do atributo, calcular a entropia de acordo com as classes possíveis
        #quantos registros existem de cada classe para esse valor do atributo?
        print("\n Valor do atributo: ", valorAtributo)
        registrosPorValorAtributo = []
        amostraPossibPorClasse = []
        entropiaAtrib = 0.0
        prob =0.0

        for linha in dataset: #para cada linha da base de dados
            if(linha[nomesAtributos[indice]] == valorAtributo): # se o atributo selecionado é = possibilidade
                registrosPorValorAtributo.append(linha[nomesAtributos[atClass]])

        cont = 0
        for c in classesPossiveis:
            amostraPossibPorClasse.append(float(registrosPorValorAtributo.count(c)))
            print(amostraPossibPorClasse[cont]," Contagen Classe: ",c)
            if(amostraPossibPorClasse[cont] == 0):
                prob = 0.0

            else: # entropiaAtrib -= round((amostraPossibPorClasse[cont] / len(dataset)) * math.log(amostraPossibPorClasse[cont] / len(dataset), 2),4)
                prob = amostraPossibPorClasse[cont] / len(registrosPorValorAtributo)
                entropiaAtrib -= round(prob * math.log(prob, 2),3)
            cont+=1
        ganhoAtributo -= len(registrosPorValorAtributo) / len(dataset) * entropiaAtrib
    return ganhoAtributo

# para cada uma das possibilidades calcular a entropia
# calcular o ganho




classesPossiveis, null = getQtdValoresClasses()
entropiaS = entropiasistema()
print(entropiaS)

#apos calcular a entropia do sistema agora temos que ver o ganho de cada um dos atributos.
#ganhoAtrib = entropiaSistema - probYes*entropiaAtrib - probNo*entropiaAtrib
for i in range(len(nomesAtributos)):


    at = atributo.Atributo(nomesAtributos[i])

    if(i != atClass):
        print('ATRIBUTO: ',nomesAtributos[i])
        ganhoAtrib.update({nomesAtributos[i]:round(getGanhoAtributo(i,classesPossiveis,entropiaS),3)})
        print("Ganho de informação do atributo:",ganhoAtrib[nomesAtributos[i]])
        at.informationGain = round(getGanhoAtributo(i,classesPossiveis,entropiaS),3)
    else:
        at.isitclass = True
        at.setClasses(dataset)

    arr_Atributes.append(at)



atributoMaiorGanho = max(ganhoAtrib, key=ganhoAtrib.get)
print("O atributo com maior ganho de informação é: ",atributoMaiorGanho,ganhoAtrib[atributoMaiorGanho])

listaAtributosJaConsiderados = []
listaAtributosJaConsiderados.append(atributoMaiorGanho)

print(listaAtributosJaConsiderados)

#para cada possibilidade do artributo selecionado, construir uma subdata e repetir o processo.
# Outlook sunny:

# for val in atributo_i.valores:
