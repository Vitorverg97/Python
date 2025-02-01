##_Estrtura_##
# While condicao:
#   comandos1
#   comandos2

# O laço while repete até que uma condição seja atendida, exemplo:
## Contador de números (Number Counter)

numero = 0
while numero <= 10:
    print(numero)
    numero += 1 # Forma abreviada da expressão: numero = numero + 1
print ('Acabou o loop while.')

## Contador de números com input (Number Counter with input)

numero_max = int(input('Insira o número que deseja contar: '))
NUMERO_INIT = 0

while NUMERO_INIT <= numero_max:
    print(NUMERO_INIT)
    NUMERO_INIT += 1
print('Fim da contagem.')

#___EXERCISE___#
