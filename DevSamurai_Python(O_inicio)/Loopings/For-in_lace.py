##_Estrtura_##
# for variavel in itens:
#   comandos1
#   comandos2
#   comandos3

# o laço For in percorre valores em um array. Por exemplo:
for diasDaSemana in ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']:
    print(diasDaSemana)
print('FOR_IN atribuiu os elementos para a array "diasDaSemana".')

# Contando números com uma função Built-in 'range()'
#Sequência do 0 ao 10
numerosNaturais = [1,2,3,4,5]
for numerosNaturais in range(10+1):     
    print(numerosNaturais) 

#Sequência do 5 ao 10
for numerosNaturais in range(5,11): 
    print(numerosNaturais) 

#Sequência do 5 ao 20 somando de 5 em 5, bem como uma P.A com quatro termos sendo: A1 = 5; An = 20; q = 5
for numerosNaturais in range(5,21,5): 
    print(numerosNaturais) 

#___EXERCISE___#

## Faça um programa que gere uma tabuada. O programa deverá perguntar ao usuário qual será a tabuada e até qual valor (geramente do inicia-se do 0 ao 10)

tabuada = int(input("Qual tabuada queres? "))
intervalo = int(input("Até qual número será o fim da tabuada? "))

for numero in range(0, intervalo+1):
    print(f"{tabuada} X {numero}= {numero*tabuada}")

## Faça um programa que calcule o enésimo elemento da série de Fibonacci. Lembrando que a série começa da seguinte forma: 1,1,2,3,5,8,13,21,34,55...

n = int(input("Digite qual termo da sequência Fibonacci deve ser mostrado: "))
primeiro = 1
segundo = 1

if n==1 or n==2:
    print('1')

else:
    for _ in range(2,n):
        elemento = primeiro + segundo
        segundo = primeiro
        primeiro = elemento
    print(elemento)
