# odeio essa questao
import random
r1, r2, r3 = [], [], []  # armazenando R1 R2 R3 em uma lista
Falha = []
'''x = 0
y = 0
z = 0'''
for i in range(10000000):
    # usando a funçao choices do random e a weights que sao como os 'pesos'
    x = random.choices(['M1', 'M2', 'Falha'], weights=[6, 3, 1])
    if x == ['M1']:  # se x for igual a M3 dependendo do weights rodara um dos 3 da lista
        # a funçao weights indica  a probabilidade de repetiçao para cada elemento
        y = random.choices(['M3', 'M4', 'Falha'], weights=[5, 3, 2])
        if y == ['M3']:
            z = random.choices(['Destino', 'Falha'], weights=[9,1])
            if z == ['Destino']:
                r1.append(1)  # ira adicionar 1 a lista do R!
            else:
                Falha.append(1)
        elif y == ['M4']: #repetindo as mesmas coisas com as outras variaveis usando if else e elif
            z = random.choices(['Destino', 'Falha'], weights=[8,2])
            if z == ['Destino']:
                r2.append(1)
            else:
                Falha.append(1)
        else:
            Falha.append(1)  
    elif x == ['M2']:
        y = random.choices(['M5','Falha'],weights=[9.5,0.5])
        if y == ['M5']:
            z = random.choices(['Destino','Falha'],weights=[8.5,1.5])
            if y == ['Destino']:
                r3.append(1)
            else:
                Falha.append(1)
        else:
            Falha.append(1)

    else:
        Falha.append(1) 


print('Envios dos 10 milhoes de pacotes')
print(f'{sum(r1)} Chegaram pela rota 1')       
print(f'{sum(r2)} Chegaram pela rota 2') 
print(f'{sum(r3)} Chegaram pela rota 3') 
print(f'{sum(Falha)} Nao chegaram') 