#Jogo da Velha
#-*- coding: utf-8 -*-
jogo = 1
while(jogo==1):
    import os
    os.system('cls')
    opcao = 0
    jogador = 1
    e1 = " "
    e2 = " "
    e3 = " "
    e4 = " "
    e5 = " "
    e6 = " "
    e7 = " "
    e8 = " "
    e9 = " "
    linha = 0
    coluna = 0
    partida = 1
    print("       COLUNA")
    print("     1   2   3")
    print("L 1  "+e1+" | "+e2+" | "+e3+"")
    print("I   -----------")
    print("N 2  "+e4+" | "+e5+" | "+e6+"")
    print("H   -----------")
    print("A 3  "+e7+" | "+e8+" | "+e9+"")
    while(partida==1):
        if (jogador==1):
            linha = int(input("JOGADOR 1, escolha uma linha: "))
            coluna = int(input("JOGADOR 1, escolha uma coluna: "))
            import os
            os.system('cls')
            if(linha==1 and coluna==1 and e1==" "):
                e1 = "X"
                jogador=2
            if(linha==1 and coluna==2 and e2==" "):
                e2 = "X"
                jogador=2
            if(linha==1 and coluna==3 and e3==" "):
                e3 = "X"
                jogador=2
            if(linha==2 and coluna==1 and e4==" "):
                e4 = "X"
                jogador=2
            if(linha==2 and coluna==2 and e5==" "):
                e5 = "X"
                jogador=2
            if(linha==2 and coluna==3 and e6==" "):
                e6 = "X"
                jogador=2
            if(linha==3 and coluna==1 and e7==" "):
                e7 = "X"
                jogador=2
            if(linha==3 and coluna==2 and e8==" "):
                e8 = "X"
                jogador=2
            if(linha==3 and coluna==3 and e9==" "):
                e9 = "X"
                jogador=2
            print("       COLUNA")
            print("     1   2   3")
            print("L 1  "+e1+" | "+e2+" | "+e3+"")
            print("I   -----------")
            print("N 2  "+e4+" | "+e5+" | "+e6+"")
            print("H   -----------")
            print("A 3  "+e7+" | "+e8+" | "+e9+"")
        #Verifica se a partida terminou
        if(e1 == e2 == e3 or e1 == e5 == e9 or e1 == e4 == e7):
            if (e1 != " "):
                print("Fim de partida!")
                if (e1 == "X"):
                    print("Vitoria do JOGADOR 1!")
                else:
                    print("Vitoria do JOGADOR 2!")
                opcao = int(input("Para jogar novamente, digite <1>. Para sair do jogo, digite <0>: "))
                if (opcao == 1):
                    partida = 0
                    break
                if (opcao == 0):
                    jogo = 0
                    partida = 0
                    break
        if(e2 == e5 == e8 or e3 == e5 == e7 or e4 == e5 == e6):
            if (e5 != " "):
                print("Fim de partida!")
                if (e5 == "X"):
                    print("Vitoria do JOGADOR 1!")
                else:
                    print("Vitoria do JOGADOR 2!")
                opcao = int(input("Para jogar novamente, digite <1>. Para sair do jogo, digite <0>: "))
                if (opcao == 1):
                    partida = 0
                    break
                if (opcao == 0):
                    jogo = 0
                    partida = 0
                    break
        if(e3 == e6 == e9  or e7 == e8 == e9):
            if (e9 != " "):
                print("Fim de partida!")
                if (e9 == "X"):
                    print("Vitoria do JOGADOR 1!")
                else:
                    print("Vitoria do JOGADOR 2!")
                opcao = int(input("Para jogar novamente, digite <1>. Para sair do jogo, digite <0>: "))
                if (opcao == 1):
                    partida = 0
                    break
                if (opcao == 0):
                    jogo = 0
                    partida = 0
                    break
        if (jogador==2):
            linha = int(input("JOGADOR 2, escolha uma linha: "))
            coluna = int(input("JOGADOR 2, escolha uma coluna: "))
            import os
            os.system('cls')
            if(linha==1 and coluna==1 and e1==" "):
                e1 = "O"
                jogador=1
            if(linha==1 and coluna==2 and e2==" "):
                e2 = "O"
                jogador=1
            if(linha==1 and coluna==3 and e3==" "):
                e3 = "O"
                jogador=1
            if(linha==2 and coluna==1 and e4==" "):
                e4 = "O"
                jogador=1
            if(linha==2 and coluna==2 and e5==" "):
                e5 = "O"
                jogador=1
            if(linha==2 and coluna==3 and e6==" "):
                e6 = "O"
                jogador=1
            if(linha==3 and coluna==1 and e7==" "):
                e7 = "O"
                jogador=1
            if(linha==3 and coluna==2 and e8==" "):
                e8 = "O"
                jogador=1
            if(linha==3 and coluna==3 and e9==" "):
                e9 = "O"
                jogador=1            
        print("       COLUNA")
        print("     1   2   3")
        print("L 1  "+e1+" | "+e2+" | "+e3+"")
        print("I   -----------")
        print("N 2  "+e4+" | "+e5+" | "+e6+"")
        print("H   -----------")
        print("A 3  "+e7+" | "+e8+" | "+e9+"")
        #Verifica se a partida terminou
        if(e1 == e2 == e3 or e1 == e5 == e9 or e1 == e4 == e7):
            if (e1 != " "):
                print("Fim de partida!")
                if (e1 == "X"):
                    print("Vitoria do JOGADOR 1!")
                else:
                    print("Vitoria do JOGADOR 2!")
                opcao = int(input("Para jogar novamente, digite <1>. Para sair do jogo, digite <0>: "))
                if (opcao == 1):
                    partida = 0
                    break
                if (opcao == 0):
                    jogo = 0
                    partida = 0
                    break
        if(e2 == e5 == e8 or e3 == e5 == e7 or e4 == e5 == e6):
            if (e5 != " "):
                print("Fim de partida!")
                if (e5 == "X"):
                    print("Vitoria do JOGADOR 1!")
                else:
                    print("Vitoria do JOGADOR 2!")
                opcao = int(input("Para jogar novamente, digite <1>. Para sair do jogo, digite <0>: "))
                if (opcao == 1):
                    partida = 0
                    break
                if (opcao == 0):
                    jogo = 0
                    partida = 0
                    break
        if(e3 == e6 == e9  or e7 == e8 == e9):
            if (e9 != " "):
                print("Fim de partida!")
                if (e9 == "X"):
                    print("Vitoria do JOGADOR 1!")
                else:
                    print("Vitoria do JOGADOR 2!")
                opcao = int(input("Para jogar novamente, digite <1>. Para sair do jogo, digite <0>: "))
                if (opcao == 1):
                    partida = 0
                    break
                if (opcao == 0):
                    jogo = 0
                    partida = 0
                    break
