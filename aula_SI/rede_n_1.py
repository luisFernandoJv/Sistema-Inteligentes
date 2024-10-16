import random
import math 
w = [0, -1]

def f(entrada):
    return 1 if entrada > 0 else -1

taxa = 0.0001

while True:
    x = [random.uniform(-1, 1), random.uniform(-1, 1)]
    esperado = 1 if x[1] > 0 else -1
    
    entrada_total = w[0]*x[0]+w[1]*x[1]
    saida = f(entrada_total)
    
    erro = esperado - saida
    
    if(erro != 0):
        print('errou')
        w[0] += taxa*x[0]*erro
        w[1] += taxa*x[1]*erro
        print('acertou')
        
    print(w)
