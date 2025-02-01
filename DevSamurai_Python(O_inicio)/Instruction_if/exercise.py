# Exercício de fixação

# Fazer um programa que recebe do usuário duas notas de zero a dez e escreva na tela (Você está aprovado. Parabéns), se a média das duas notas for maior que sete.

def avarage ():
    Rate1 = float(input('Insira a primeira nota avaliativa: '))
    Rate2 = float(input('Insira a segunda nota avaliativa: '))
    avg = (Rate1 + Rate2)/2
    if avg >= 7:
        print(f"Você está aprovado com média: {avg}")
    elif avg > 5 and avg < 7 :
        print(f'Você está de recuperação com média: {avg}')
    else :
        print(f'Você está reprovado com média: {avg}')

avarage()
# Ainda no mesmo exemplo da média, mas usando como condição: se a média for maior que cinco e menor que sete escreva na tela (Você está de recuperação.)