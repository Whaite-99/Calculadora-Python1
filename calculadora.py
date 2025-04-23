# Variaveis
num1 = 0
num2 = 0
operação = ''
resultado = 0



while True:
    num1 = float(input('Digite o primeiro número: '))
    operação = input('Digite a operação')
    if operação == 'sair':
        print('saindo da calculadora')
        break 
    num2 =  float(input('Digite o segundo número: '))
    if operação == '+':
        resultado = num1 + num2
    elif operação == '-':
        resultado = num1 - num2
    elif operação == '*':
        resultado = num1 * num2
    elif operação == '/':
        resultado = num1 / num2
    else:
        print('Operação inválida')
        resultado = 0
    print('Resultado é:', resultado)
