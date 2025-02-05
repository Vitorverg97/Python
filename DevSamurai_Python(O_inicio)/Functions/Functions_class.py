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

