# Trabalhando com if, elif e else
# A condicional "if" e suas semelantes funcionam com validando as condições implicitamente como (TRUE ou FALSE)

## Exemplo

### Criando um programa que verifica se está quente, agradável ou frio em (°C)

temp = int(input("Insert the teperature in °C: "))
if temp >= 40:
    print('It is warm.')
elif temp >= 30:
    print('It is fine.')
else : # temp <= 30
    print('It is cold.')
