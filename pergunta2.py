def fibonacci(numero):
    
    a, b = 0, 1
    
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    
    return False


numero = int(input("Informe um número para verificar se pertence a sequência de Fibonacci: "))


if fibonacci(numero):
    print(f'O número {numero} pertence a sequência de Fibonacci')
else:
    print(f'O número {numero} não pertence a sequência de Fibonacci')