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
#number = (input("Qual número deseja elevar ao quadrado? "))
#def potenciaQuadrada(numero = 5):
    
#    if number == '':
#        print(pow(numero,2))
#    else:
#        print(pow(number, 2))

## Escreva uma função que receba como parâmetro uma temperatura em graus Fahrenheit e converta para graus Celsius.
def temperatureConverter(fTemp):
    fTemp = int(input("Para converter em °C. Insira o valor em °F: "))
    cTemp = (fTemp - 32)/1.8
    return cTemp

cToFTemp = temperatureConverter(fTemp = int)
print(f'{cToFTemp:.1f}°C')

## Escreva uma função que receba dois parâmetros. O primeiro será uma palavra, se ela for quadrado deverá calcular o quadrado do número passado como segundo parâmetro. Se a palavra for cubo deverá realizar o calculo do cubo do número passado.

def potenciacao(quadrado, cubo):
    recebendoValores = input("Qual potenciação escolhes? 'quadrado' ou 'cubo?' ")
    if recebendoValores == 'quadrado':
        quadrado = pow(recebendoValores, 2)
    elif recebendoValores == 'cubo':
        cubo = pow(recebendoValores, 3)
    print(quadrado or cubo)
    