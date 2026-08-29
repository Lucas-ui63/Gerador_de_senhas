num1 = float(input('Digite o primeiro numero: '))
operador = input('Digite o operador (+, -, *, /): ')
num2 = float(input('Digite o segundo numero: '))

if operador == '+':
    resultado = num1 + num2
elif operador == '-':    
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 == 0:
        print('Nao se divide por zero, tente novamente.')
    else:   
        resultado = num1 / num2

print(f'O resultado da operação é: {resultado}')