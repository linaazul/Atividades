# Exercício - sistema de perguntas e respostas com Python

import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador_de_acertos = 0
for pergunta in perguntas:

    indice = 0

    print('~~~~~~~~~~~  ( •̀ ω •́ )✧ ~~~~~~~~~~~')

    print(pergunta['Pergunta'])
    print('Opções:')

    for opcao in pergunta['Opções']: # Também podeeria ter usado enumerate
        print(f'{indice}) {opcao}') 
        indice += 1

    resposta = input('Escolha uma opção: ')

    os.system('cls')
    
    try:
        resposta_int = int(resposta)
        if pergunta['Opções'][resposta_int] != pergunta['Resposta']:
            print("Você errou! ╯︿╰ ")
        else:
            print("Você acertou!! ☆: .｡. o(≧▽≦)o .｡.:☆")
            contador_de_acertos += 1
    except IndexError:
        print(f"Dê uma resposta válida, {resposta_int} está fora das opções! (っ °Д °;)っ")
    except ValueError:
        print("NÃOO!!! Você sabe que tem que digitar NÚMEROS NÉ! .·´¯`(>▂<)´¯`·. ")
    except:
        print("Algo deu errado aqui... ops, hihihi ≧ ﹏ ≦")

if contador_de_acertos == 0:
    print("Não foi dessa vez... estude mais NERD. ヽ（≧□≦）ノ")
else:
    print(f"Parabéns, voce conseguiu!! Acertou {contador_de_acertos} de 3 perguntas. Você é demais!!! (/ω＼*)……… (/ω•＼*)")

        
