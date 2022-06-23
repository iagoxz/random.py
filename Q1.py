# JOKENPÔ
import random
Usuario = int(input('''Opçoes 
    [1] Pedra
    [2] Papel 
    [3] Tesoura
    Qual sua escolha?: ''')) #opçoes de escolha do usuario

opçoes = ('Pedra','Papel', 'Tesoura') #usando uma tupla para armazenar as opçoes
maquina = (random.randint(1, 3)) #escolha aleatoria da maquina usando randint (biblioteca de numeros inteiros do random)

print('Voce escolheu {}'.format(opçoes[Usuario-1])) #usando print formatado e substituindo a variavel usuario pelas opçoes
print('A maquina escolheu {}'.format(opçoes[maquina-1]))

if maquina == 2  and Usuario == 1  or maquina ==3 and Usuario == 2 or maquina == 1 and Usuario == 3:
    print('Voce Perdeu!!, Tente novamente')


elif maquina == 2  and Usuario == 3  or maquina == 3  and Usuario == 1 or maquina == 1 and Usuario == 2:
    print('Voce venceu a maquina!!! Parabens')

elif Usuario == maquina:
    print('Voces empataram!!!')