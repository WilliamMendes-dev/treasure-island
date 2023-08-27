print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo ao Treasure Dungeon!")
print(
    "Nesse jogo, você é um aventureiro em busca de um tesouro escondido no fundo da masmorra. Um dos caminhos te deixará rico! Boa sorte! \n"
)
# Mensagem de game over genérica
game_over = "Informação Inválida. Um buraco se abre e você cai em um poço sem fundo. Game Over"
#primeira encruzilhada 
caminho_1 = input(
    "Você adentra uma masmorra misteriosa. À sua frente há dois caminhos, um para a esquerda e outro para a direita, qual deles você escolhe? (Esquerda / Direita) \n"
).lower()

if caminho_1 == "esquerda":
    print("Você se depara com uma armadilha mortal. Game Over!")
#progresso 1
elif caminho_1 == "direita":
    print(
        "\nSeu caminho é cortado por um grande volume de água. Um barco está ancorado na margem que você se encontra."
    )
    #segunda encruzilhada
    caminho_2 = input(
        "Para realizar a travessia, deseja nadar ou utilizar o barco? (Nadar / Barco) \n"
    ).lower()

    if caminho_2 == "nadar":
        print("Você é atacado por piranhas. Game Over!")
    #progresso 2
    elif caminho_2 == "barco":
        print(
            "\nAo chegar do outro lado, você se depara com um 3 portas fechadas de cores diferentes."
        )
        #terceira encruzilhada
        caminho_3 = input(
            "Qual delas você escolherá? (Vermelha / Amarela / Azul) \n").lower(
            )

        if caminho_3 == "vermelha":
            print("Você é engolido por uma labareda de chamas. Game Over!")
        #venceu o jogo
        elif caminho_3 == "amarela":
            print("Você encontrou uma sala recheada de tesouros. Você Venceu!")
        elif caminho_3 == "azul":
            print(
                "Você abriu o canil dos monstros, eles te devoram. Game Over!")
        else:
            print(game_over)

    else:
        print(game_over)

else:
    print(game_over)
