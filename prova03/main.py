"""[LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número.
Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso."""

num_fix = 7
tentativas = 3

while tentativas > 0:
    palpite = int(input(f"Você tem {tentativas} tentativas. Qual é o seu palpite? "))

    if palpite == num_fix:
        print('Seu palpite está correto!')
        break
    else:
        tentativas -= 1
        print('Você errou! Tente novamente')

else:
    print('Não foi dessa vez! Tente novamente mais tarde, acredito que na próxima você acerta!')