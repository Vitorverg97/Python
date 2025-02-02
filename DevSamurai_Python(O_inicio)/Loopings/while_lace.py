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

## Faça um programa que calcule o fatorial de um número fornecido pelo usuário, por exemplo: Cinco fatorial = 5! = 5*4*3*2*1 = 120

numero_fat = int(input("Insira um número inteiro, para obter o fatorial: "))
fatorial = numero_fat
while numero_fat >=2:
    fatorial = fatorial * (numero_fat - 1)
    numero_fat -=1
print(f"O fatorial é {fatorial}.")

## Faça um programa que simule um cofre, ele terá uma senha pré-definida. A cada tentativa errada o programa deverá mostrar a mensagem: Senha incorreta. Tente novamente. Se ele acertar a senha o programa deverá mostrar a mensagem: Senha correta. Acesso concedido.

senha = '777'
tentativas = 3

while tentativas > 0:
    cofre_pessoal = input("Digite a senha que contém 3 números: ")
    
    if cofre_pessoal == senha:
        print("Senha correta. Acesso concedido.")
        break
    
    tentativas -= 1
    
    if tentativas == 0: 
        print("Limite de tentativas excedido. Tente novamente mais tarde.")
    
    else :
        print(f"Senha incorreta. Tente novamente.({tentativas} tentativas restantes)")
