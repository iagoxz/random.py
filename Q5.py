import random
velo_max = int(input('Digite a velocidade do seu navio: '))
carga_max = int(input('Digite a carga do seu navio (min 1000t max 3000t): '))
conteiners = []

while len(conteiners) < 50:
    pesos = random.randint (1,100)
    if sum(conteiners) >= carga_max:
        break
    elif sum(conteiners) > carga_max: 
        conteiners.pop() #funçao pop
    else:
        conteiners.append(pesos)

velo_removida = (velo_max*20)/100
velocidade_final= velo_max - (sum(conteiners)) / 100

while velocidade_final < velo_removida:
    conteiners.remove(max(conteiners)) #funçao max
    velocidade_final = velo_max - (sum(conteiners))

distancia = 5840.85 / velocidade_final

print('A quantidade de conteiners é {}'.format(len(conteiners)))
print('A carga total do seu navio e {}'.format(sum(conteiners)))
print(velo_removida)
print('A velocidade atual do seu navio por conta do peso é de {}'.format(velocidade_final))
print('O tempo de viagem ate lisboa e de {:.2f}'.format(distancia))