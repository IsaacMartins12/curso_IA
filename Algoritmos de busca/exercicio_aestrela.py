import numpy as np

class Aestrela :
    def __init__ (self,objetivo) :
        self.objetivo = objetivo
        self.encontrado = False
        
    def buscar (self, atual) :
        print('-------')
        print('Atual : {}'.format(atual.rotulo))
        atual.visitado = True
        
        if atual == self.objetivo :
           self.encontrado = True 
        else :
           vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
           for adjacente in atual.adjacentes:
               if adjacente.vertice.visitado == False :
                   adjacente.vertice.visitado = True
                   vetor_ordenado.insere(adjacente)
           vetor_ordenado.imprime()
           
           if vetor_ordenado.valores[0] != None :
              self.buscar(vetor_ordenado.valores[0].vertice)



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
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo


class Grafo :
    porto_uniao = Vertice('Porto União',203)   
    paulo_frontin = Vertice('Paulo Frontin',172)   
    canoinhas = Vertice('Canoinhas',141) 
    tres_barras = Vertice ('Três Barras',131)  
    sao_mateus_do_sul = Vertice ('São Mateus do Sul',123) 
    irati = Vertice('Irati',139) 
    curitiba = Vertice('Curitiba',0) 
    palmeira = Vertice('Palmeira',159) 
    mafra = Vertice('Mafra',94) 
    campo_largo = Vertice ('Campo Largo',27) 
    bolsa_nova = Vertice ('Bolsa Nova',41) 
    lapa = Vertice ('Lapa',74) 
    tijucas_do_sul = Vertice ('Tijucas do Sul',56) 
    araucaria = Vertice('Araucária',23) 
    sao_jose_dos_pinhais = Vertice('São josé dos pinhais',13) 
    contenda = Vertice('Contenda',39) 

    # Adiciona cidades vizinhas de Porto União
   
    porto_uniao.adiciona_adjacente(Adjacente(paulo_frontin,46))
    porto_uniao.adiciona_adjacente(Adjacente(sao_mateus_do_sul,87))
    porto_uniao.adiciona_adjacente(Adjacente(canoinhas,78))
   
    # Adiciona cidades vizinhas de Paulo Frotin
   
    paulo_frontin.adiciona_adjacente(Adjacente(irati,75))
    paulo_frontin.adiciona_adjacente(Adjacente(porto_uniao,46))
   
    # Adiciona cidades vizinhas de canoinhas
   
    canoinhas.adiciona_adjacente(Adjacente(tres_barras,12))
    canoinhas.adiciona_adjacente(Adjacente(mafra,66))
    canoinhas.adiciona_adjacente(Adjacente(porto_uniao,78))

     
    # Adiciona cidades vizinhas de Três Barras
   
    tres_barras.adiciona_adjacente(Adjacente(sao_mateus_do_sul,43))
    tres_barras.adiciona_adjacente(Adjacente(canoinhas,12))
    
    # Adiciona cidades vizinhas de São Mateus do Sul
    
    sao_mateus_do_sul.adiciona_adjacente(Adjacente(tres_barras,43))
    sao_mateus_do_sul.adiciona_adjacente(Adjacente(porto_uniao,87))
    sao_mateus_do_sul.adiciona_adjacente(Adjacente(lapa,60))
    sao_mateus_do_sul.adiciona_adjacente(Adjacente(irati,57))
    sao_mateus_do_sul.adiciona_adjacente(Adjacente(palmeira,77))
   
    # Adiciona cidades vizinhas de irati
   
    irati.adiciona_adjacente(Adjacente(paulo_frontin,75))
    irati.adiciona_adjacente(Adjacente(palmeira,75))
   
    # Adiciona cidades vizinhas de Curitiba
   
    curitiba.adiciona_adjacente(Adjacente(araucaria,37))
    curitiba.adiciona_adjacente(Adjacente(bolsa_nova,51))
    curitiba.adiciona_adjacente(Adjacente(sao_jose_dos_pinhais,15))
    curitiba.adiciona_adjacente(Adjacente(campo_largo,29))

   
    # Adiciona cidades vizinhas de Palmeira
   
    palmeira.adiciona_adjacente(Adjacente(irati,75))
    palmeira.adiciona_adjacente(Adjacente(sao_mateus_do_sul,77))
    palmeira.adiciona_adjacente(Adjacente(campo_largo,55))
   
    # Adiciona cidades vizinhas de Mafra
   
    mafra.adiciona_adjacente(Adjacente(lapa,57))
    mafra.adiciona_adjacente(Adjacente(canoinhas,66))
    mafra.adiciona_adjacente(Adjacente(tijucas_do_sul,99))
   
    #Adiciona cidades vizinhas de Campo Largo
   
    campo_largo.adiciona_adjacente(Adjacente(bolsa_nova,22))
    campo_largo.adiciona_adjacente(Adjacente(palmeira,55))
    campo_largo.adiciona_adjacente(Adjacente(curitiba,29))
   
    #Adiciona cidades vizinhas de Bolsa Nova
   
    bolsa_nova.adiciona_adjacente(Adjacente(campo_largo,22))
    bolsa_nova.adiciona_adjacente(Adjacente(contenda,19))
    bolsa_nova.adiciona_adjacente(Adjacente(curitiba,51))
   
    #Adiciona cidades vizinhas de Lapa
   
    lapa.adiciona_adjacente(Adjacente(contenda,26))
    lapa.adiciona_adjacente(Adjacente(sao_mateus_do_sul,60))
    lapa.adiciona_adjacente(Adjacente(mafra,57))
   
    #Adiciona cidades vizinhas de Tijucas do Sul
   
    tijucas_do_sul.adiciona_adjacente(Adjacente(mafra,99))
    tijucas_do_sul.adiciona_adjacente(Adjacente(sao_jose_dos_pinhais,49))
   
    #Adiciona cidades vizinhas de Araucária
   
    araucaria.adiciona_adjacente(Adjacente(contenda,18))
    araucaria.adiciona_adjacente(Adjacente(curitiba,37))
   
    #Adiciona cidades vizinhas de São josé dos pinhais
   
    sao_jose_dos_pinhais.adiciona_adjacente(Adjacente(curitiba,15))
    sao_jose_dos_pinhais.adiciona_adjacente(Adjacente(tijucas_do_sul,49))
   
    #Adiciona cidades vizinhas de Contenda
   
    contenda.adiciona_adjacente(Adjacente(bolsa_nova,19))
    contenda.adiciona_adjacente(Adjacente(lapa,26))
    contenda.adiciona_adjacente(Adjacente(araucaria,18))


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
                print(i,' - ',self.valores[i].vertice.rotulo, ' - ',self.valores[i].custo, ' - ' , self.valores[i].vertice.distancia_objetivo , ' - ' , self.valores[i].distancia_aestrela)
               
    def insere (self,adjacente) :
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade atingida')
            return
   
        posicao = 0
        for i in range (self.ultima_posicao + 1) :
          posicao = i
          if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela : break
          if i == self.ultima_posicao :
              posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao :
           self.valores[x+1] = self.valores[x]
           x = x - 1
           
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1
      

grafo = Grafo()
vetor = VetorOrdenado(3)

vetor.insere(grafo.porto_uniao.adjacentes[0])
vetor.insere(grafo.porto_uniao.adjacentes[1])
vetor.insere(grafo.porto_uniao.adjacentes[2])

busca_aestrela = Aestrela(grafo.curitiba)
busca_aestrela.buscar(grafo.porto_uniao)


