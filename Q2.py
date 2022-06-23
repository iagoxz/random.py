#Questao 2 simulando 0 lançamento de 3 dados
import random

usuario = int(input('Digite um numero de 1 a 6: '))
lançamentos = [] #lista vazia para o lançamentos dos dados
acertos = [] #lista para o numero de acertos do usuario

for j in range (3): #usando um for dentro do outro como visto em saula de aula
    for i in range(j):
        dados = random.randint(1,6) #usando randint para randomizar o lançamento dos dados
        lançamentos.append(dados)
        if dados == usuario: 
            acertos.append(1) #se o numero dos dados for igual o do usuario a funçao append ira adicinar 1 a lista

print("Os numeros do dado foram{}".format(lançamentos))
resultado = sum(acertos) #usando a funçao sum para somar os elementos da lista
if resultado == 0:
    print("Que pena, Voce nao acertou nenhum dado, Boa sorte na proxima!!!")
elif resultado == 1:
    print("UAU, voce acertou um dado, mas isto pode melhorar nao e mesmo?")
elif resultado == 2:
    print("Que sorte!!! Voce acertou dois dados!")
elif resultado == 3:
    print("O impossivel aconteceu voce acertou tres dados!!!!")
