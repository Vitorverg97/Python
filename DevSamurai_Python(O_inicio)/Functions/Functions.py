#Funções são códigos que podemos chamar a todo momento no programa. Temos que tomar o cuidado de definir a função antes de chamá-la. 

#Obs: Documentar a função (Docstring) é uma boa prática de programação.

# Função sem retorno e sem passagem de parâmetro
def olaMundo ():
	'Função que imprime um mensagem padrão.'
	print("Olá mundo!")

olaMundo()

# Função sem retorno com passagem de parâmetro
def ola_mundo(name= 'user'):
	'Função que imprime uma mensagem personalizada default'
	print(f"Olá mundo! Meu nome é {name}")

nome = input("Qual é o seu nome? ")
ola_mundo()

#Função com retorno com passagem de parâmetros

def soma(a,b):
    'Função que recebe dois números do usuário e realiza a soma entre eles.'
    
    return a + b
a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))

resultadoSoma = soma(a,b)
print(resultadoSoma)

# __Exercícios__ #

## Escreva uma função que calcule o quadrado do número passado como parâmetro. Se nenhum número for passado use como padrão o número 5.
def potenciaQuadrada(numero = 5):
    'Função que calcula a exponêciação quadrática de um número inserido como parâmetro. A função também conta com um valor default "5".'

    return pow(numero,2)

resultado = potenciaQuadrada(6)
print(f"O resultado é: {resultado}")

## Escreva uma função que receba como parâmetro uma temperatura em graus Fahrenheit e converta para graus Celsius.
def temperatureConverter():
    'Função que converte a temperatura em °F para °C, através do input do usuário'
    
    User_Input = input("Insira o valor em °F, para converter em Graus Celsius: ")
    F_Temp = float(User_Input)
    C_Temp = (F_Temp - 32)/1.8
    return C_Temp

CelsiusConverted = temperatureConverter()
print(f'{CelsiusConverted:.1f}°C')

## Escreva uma função que receba dois parâmetros. O primeiro será uma palavra, se ela for quadrado deverá calcular o quadrado do número passado como segundo parâmetro. Se a palavra for cubo deverá realizar o calculo do cubo do número passado.
def potenciacao():
    'Função que faz o cálculo da potênciação, através da inserção do índiçe (Quadrado ou Cubo) e valor pelo usuário.'
   
    decisao = input("Escolha o índice da potênciação --> 'quadrado' ou 'cubo': ").strip().lower()
    
    if decisao == 'quadrado':
        valor = int(input("Insira o valor que desejas potencializar quadráticamente: "))
        return pow(valor, 2)
    
    elif decisao == 'cubo':
        valor = int(input("Insira o valor que desejas potencializar cúbicamente: "))
        return pow(valor, 3)
    
    else:
        return "Opção inválida. Escolha 'quadrado' ou 'cubo'."
resultadoPot = potenciacao()
print(f'O resultado é: {resultadoPot}')
