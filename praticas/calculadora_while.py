# calculadora com while
while True:
    n1 = input('digite um número: ')
    n2 = input('digite outro número: ')
    operador = input('digite a operação que deseja fazer (+-/*): ')
    
    numeros_valid = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(n1)
        num_2_float = float(n2)
        numeros_valid = True
        
    except Exception as error:
        
       numeros_valid = None
       
    operadores_permitidos = '+-/*'
    
    if numeros_valid is None: 
        print('Um ou ambos dos números digitados não são validos.')
        continue
    
    if operador not in operadores_permitidos:
        print('operador invalido.')
        continue
    
    if len(operador) > 1:
        print('diogite apenas um operador')
        continue
    print('realizando sua conta, confira o resultado abaixo:')
    
    if operador == '+':
        print(f'A soma de {num_1_float} + {num_2_float} é igual:', num_1_float + num_2_float)
        
    elif operador == '-':
        print(f'A subtração de {num_1_float} - {num_2_float} é igual:', num_1_float - num_2_float)
        
    elif operador == '/':
        print(f'A divisão de {num_1_float} / {num_2_float} é igual:', num_1_float / num_2_float)
    
    elif operador == '*':
        print(f'A multiplicação de {num_1_float} * {num_2_float} é igual:', num_1_float * num_2_float)
        
    else:
        print('nunca chegou aqui')
    sair = input('Digite "s" para sair /ou "n" para continuar: ').lower().startswith('s')
    
    if sair is True: 
        break