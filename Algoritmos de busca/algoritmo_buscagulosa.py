import numpy as np

class Gulosa :
    def __init__ (self,objetivo) :
      self.objetivo = objetivo
      self.encontrado = False
     
    def buscar(self, atual):
        print('-----------')
        print('Atual : {}'.format(atual.rotulo))
        atual.visitado = True
       
        if atual == self.objetivo :
            self.encontrado = True
        else :
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
              if adjacente.vertice.visitado == False :
                  adjacente.vertice.visitado == True
                  vetor_ordenado.insere(adjacente.vertice)
            vetor_ordenado.imprime()
            if vetor_ordenado.valores[0] != None :
                self.buscar(vetor_ordenado.valores[0])
             
class Vertice :
    def __init__(self,rotulo,distancia_objetivo) :
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []
       
    def adiciona_adjacente(self,adjacente) :
        self.adjacentes.append(adjacente)
   
    def mostra_adjacentes(self) :
        for i in self.adjacentes :
         print(i.vertice.rotulo , i.custo)

class Adjacente:
    def __init__(self,vertice,custo) :
        self.vertice = vertice
        self.custo = custo


class Grafo :
    arad = Vertice('Arad',360)
    zerind = Vertice('Zerind',374)
    oradea = Vertice('Oradea',380)
    sibiu = Vertice ('Sibiu',253)
    timisoara = Vertice ('Timisoara',329)
    lugoj = Vertice('Lugoj',244)
    mehadia = Vertice('Medahia',241)
    dobreta = Vertice('Dobreta',242)
    craiova = Vertice('Craiova',160)
    rimnicu = Vertice ('Rimincu',193)
    fagaras = Vertice ('Fagaras',178)
    pitesti = Vertice ('Pitesti',98)
    bucharest = Vertice ('Bucharest',0)
    giurgiu = Vertice('giurgiu',77)
   
    # Adiciona cidades vizinhas de Arad
   
    arad.adiciona_adjacente(Adjacente(zerind,75))
    arad.adiciona_adjacente(Adjacente(sibiu,140))
    arad.adiciona_adjacente(Adjacente(timisoara,118))
   
    # Adiciona cidades vizinhas de Zerind
   
    zerind.adiciona_adjacente(Adjacente(arad,75))
    zerind.adiciona_adjacente(Adjacente(oradea,71))
     
    # Adiciona cidades vizinhas de oradea
   
    oradea.adiciona_adjacente(Adjacente(zerind,71))
    oradea.adiciona_adjacente(Adjacente(sibiu,151))
   
    # Adiciona cidades vizinhas de sibiu
   
    sibiu.adiciona_adjacente(Adjacente(arad,140))
    sibiu.adiciona_adjacente(Adjacente(rimnicu,80))
    sibiu.adiciona_adjacente(Adjacente(fagaras,99))
    sibiu.adiciona_adjacente(Adjacente(oradea,151))
   
    # Adiciona cidades vizinhas de timisoara
   
    timisoara.adiciona_adjacente(Adjacente(arad,118))
    timisoara.adiciona_adjacente(Adjacente(lugoj,111))
   
    # Adiciona cidades vizinhas de lugoj
   
    lugoj.adiciona_adjacente(Adjacente(timisoara,111))
    lugoj.adiciona_adjacente(Adjacente(mehadia,70))
   
    # Adiciona cidades vizinhas de mehadia
   
    mehadia.adiciona_adjacente(Adjacente(lugoj,70))
    mehadia.adiciona_adjacente(Adjacente(dobreta,75))
   
    #Adiciona cidades vizinhas de dobreta
   
    dobreta.adiciona_adjacente(Adjacente(mehadia,75))
    dobreta.adiciona_adjacente(Adjacente(craiova,120))
   
    #Adiciona cidades vizinhas de craiova
   
    craiova.adiciona_adjacente(Adjacente(rimnicu,97))
    craiova.adiciona_adjacente(Adjacente(pitesti,138))
    craiova.adiciona_adjacente(Adjacente(dobreta,120))
   
    #Adiciona cidades vizinhas de rimnicu
   
    rimnicu.adiciona_adjacente(Adjacente(sibiu,80))
    rimnicu.adiciona_adjacente(Adjacente(craiova,146))
    rimnicu.adiciona_adjacente(Adjacente(pitesti,97))
   
    #Adiciona cidades vizinhas de fagaras
   
    fagaras.adiciona_adjacente(Adjacente(sibiu,99))
    fagaras.adiciona_adjacente(Adjacente(bucharest,211))
   
    #Adiciona cidades vizinhas de pitesti
   
    pitesti.adiciona_adjacente(Adjacente(rimnicu,97))
    pitesti.adiciona_adjacente(Adjacente(bucharest,101))
    pitesti.adiciona_adjacente(Adjacente(craiova,138))
   
    #Adiciona cidades vizinhas de bucharest
   
    bucharest.adiciona_adjacente(Adjacente(pitesti,101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu,90))
    bucharest.adiciona_adjacente(Adjacente(fagaras,211))
   
    #Adiciona cidades vizinhas de girgiu
   
    giurgiu.adiciona_adjacente(Adjacente(bucharest,90))


class VetorOrdenado :
   
    def __init__(self,capacidade) :
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade ,dtype = object)
       
       
    def imprime(self) :
        if self.ultima_posicao == -1 :
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao+1) :
                print(i,' - ',self.valores[i].rotulo, ' - ',self.valores[i].distancia_objetivo)
               
    def insere (self,vertice) :
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade atingida')
            return
   
        posicao = 0
        for i in range (self.ultima_posicao + 1) :
          posicao = i
          if self.valores[i].distancia_objetivo > vertice.distancia_objetivo :
            break
          if i == self.ultima_posicao :
              posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao :
           self.valores[x+1] = self.valores[x]
           x = x - 1
           
        self.valores[posicao] = vertice
        self.ultima_posicao += 1
 
 
grafo = Grafo()

vetor = VetorOrdenado(5)

vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.insere(grafo.lugoj)

busca_gulosa = Gulosa(grafo.bucharest)

busca_gulosa.buscar(grafo.arad)
