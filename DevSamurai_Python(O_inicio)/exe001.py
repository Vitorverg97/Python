# Execício sobre operadores e funções Biult-in

## Calcule a soma dos números do 10 ao 14.

lista1 = [10, 11, 12, 13, 14]

sum(lista1)
print(sum)

## Calcule a média entre os números 10, 15, 20.

lista2 = [10, 15, 20]

avg = sum(lista2)/3
print(avg)

## Calcule a média PONDERADA entre duas notas de 0 a 10

nota1 = input("Insira o valor da nota nº 1:")
peso1 = input("Insira o valor do peso referente a nota nº 1:")
nota2 = input("Insira o valor da nota nº 2:")
peso2 = input("Insira o valor do peso referente a nota nº 1:")
nota1.isdigit()
peso1.isdigit()
nota2.isdigit()
peso2.isdigit()
avgPonderada = ((nota1*peso1) + (nota2*peso2))/(peso1+peso2)

print(avgPonderada)

## Qual é o menor preço desta lista?

precos = [100.20, 34.90, 31,50, 18.95]

min(precos)
print(min)

# Fim