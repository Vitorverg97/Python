### Execício sobre operadores e funções Built-in ###

## Calcule a soma dos números do 10 ao 14.
print(sum([10, 11, 12, 13, 14]))

## Calcule a média entre os números 10, 15, 20.
avg = sum([10, 15, 20, 25])/4
print(avg)

## Calcule a média PONDERADA entre duas notas de 0 a 10

# É possível modificar o tipo de dado recebido pelo 'input':
# usando 'int() admitir apenas valores inteiros ANTES do 'input'.
# Utilizando a função 'eval()', que converte o valor APÓS a inserção dos dados.
nota1 = int(input("Insira o valor da nota nº 1:")) 
peso1 = int(input("Insira o valor do peso referente a nota nº 1:"))
nota2 = int(input("Insira o valor da nota nº 2:"))
peso2 = int(input("Insira o valor do peso referente a nota nº 2:"))

avgPonderada = ((nota1*peso1) + (nota2*peso2))/(peso1+peso2)
print(f'A média final é: ${avgPonderada}') # Resultado obitido é do tipo float ex: 0.0
# Caso seja preciso utilizar apenas a parte inteira de uma divisão, opera-se: valor1 // valor2.

## Qual é o menor preço desta lista?
precos = [100.20, 34.90, 31.50, 18.95]
print(min(precos))

## Avalie se o número digitado pelo usuário é par ou impar. O script deve retornar 'True' para par; e 'False' para ímpar.
def verify_odd_even():
    numb = int(input("Insira os números:"))
    if numb%2 == 0:
        return True
    else:
        return False
evenOrOdd = verify_odd_even()
print(evenOrOdd)

## Verifique se o menor preço da lista 'precos[]' é menor que R$20,00.
def verify_minor_20():
    if min(precos) < 20:
        return True
    else:
        return False
print(verify_minor_20())

## Faça um programa que converta temperaturas:  graus Fahrenheit(input do usuário) para graus Celsius(output).
#Considere: C = (5/9) * (F - 32)
def tempeture_converter_F_to_C():
    temperatureInF = float(input("Insira a temperatura em Fahrenheit:"))
    return (5/9) * (temperatureInF - 32)
print(f"A temperatura em Graus °C é:{tempeture_converter_F_to_C():.2f}")
