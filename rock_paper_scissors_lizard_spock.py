def is_odd(a):
    if a % 2 != 0:
        return True
    else:
        False

def is_more_or_equal_3(a):
    if a >= 3:
        return True
    else:
        return False
        
while 1:
    first_input = int(input('¿Máximo número de partidas? (mínimo3): '))
    if is_odd(first_input) and is_more_or_equal_3(first_input):
        print("Input taken successfully.","Number is odd and greater than five.","The game starts now:")
        partidasjugadas=0
        numeropartidas=first_input
        jugadas=0
        maquinagana=0
        usuariogana=0
        paraganar=int((numeropartidas/2)+0.5)
        print(paraganar)
        cuantas_quedan=numeropartidas-1
        while jugadas<numeropartidas:
            import sys
            import random
            aleatorio = random.randrange(0, 5)
            print("1)Piedra")
            print("2)Papel")
            print("3)Tijera")
            print("4)Lagarto")
            print("5)spock")
            if aleatorio == 0:
                maquina = "piedra"
            elif aleatorio == 1:
                maquina = "papel"
            elif aleatorio == 2:
                maquina = "tijera"
            elif aleatorio == 3:
                maquina = "lagarto"
            elif aleatorio == 4:
                maquina = "spock"
            opcion = int(input("¿Qué quieres sacar?: "))
            while opcion > 5 or opcion==0:
                print("Opción no correcta.")# pick again
                opcion = int(input("¿Qué quieres sacar?: "))
            if opcion == 1:
                Usuario = "piedra"
            elif opcion == 2:
                Usuario = "papel"
            elif opcion == 3:
                Usuario = "tijera"
            elif opcion == 4:
                Usuario = "lagarto"
            elif opcion == 5:
                Usuario = "spock"
            print("Tu elijes: ", Usuario)
            print("La máquin ha elegido: ", maquina)
            if maquina == "piedra" and Usuario == "papel":
                print("Ganaste, papel envuelve piedra")
                usuariogana+=1
            elif maquina == "papel" and Usuario == "tijera":
                print("Ganaste, Tijera corta papel")
                usuariogana+=1
            elif maquina == "tijera" and Usuario == "piedra":
                print("Ganaste, Piedra pisa tijera")
                usuariogana+=1
            elif maquina == "papel" and Usuario == "piedra":
                print("perdiste, papel envuelve piedra")
                maquinagana+=1
            elif maquina == "tijera" and Usuario == "papel":
                print("perdiste, Tijera corta papel")
                maquinagana+=1
            elif maquina == "piedra" and Usuario == "tijera":
                print("perdiste, Piedra pisa tijera")
                maquinagana+=1
            elif maquina == "spock" and Usuario == "tijera":
                print("perdiste, spock rompe tijera")
                maquinagana+=1
            elif maquina == "tijera" and Usuario == "spock":
                print("Ganaste, spock rompe tijera")
                usuariogana+=1
            elif maquina == "spock" and Usuario == "piedra":
                print("perdiste, spock vaporiza piedra")
                maquinagana+=1
            elif maquina == "piedra" and Usuario == "spock":
                print("Ganaste, spock vaporiza tijera")
                usuariogana+=1
            elif maquina == "spock" and Usuario == "papel":
                print("Ganaste, papel desautoriza spock")
                usuariogana+=1
            elif maquina == "papel" and Usuario == "spock":
                print("perdiste, papel desautoriza spock")
                maquinagana+=1
            elif maquina == "spock" and Usuario == "lagarto":
                print("Ganaste, lagarto envenena a spock")
                usuariogana+=1
            elif maquina == "lagarto" and Usuario == "spock":
                print("perdiste, lagarto envenena a spock")
                maquinagana+=1  
            elif maquina == "lagarto" and Usuario == "piedra":
                print("Ganaste, Piedra aplasta lagarto")
                usuariogana+=1
            elif maquina == "piedra" and Usuario == "lagarto":
                print("perdiste, Piedra aplasta lagarto")
                maquinagana+=1
            elif maquina == "lagarto" and Usuario == "papel":
                print("perdiste, lagarto devora papel")
                maquinagana+=1
            elif maquina == "papel" and Usuario == "lagarto":
                print("Ganaste, lagarto devora papel")
                usuariogana+=1
            elif maquina == "lagarto" and Usuario == "tijera":
                print("Ganaste, tijera decapita lagarto")
                usuariogana+=1
            elif maquina == "tijera" and Usuario == "lagarto":
                print("perdiste, tijera decapita lagarto")
                maquinagana+=1
            elif maquina == Usuario:
                print("empate")    
            print("Just",cuantas_quedan,"game left to play")               
            print("\nPlayer won",usuariogana ,"games")
            print("The machine won",maquinagana ,"games\n")
            jugadas+=1
            cuantas_quedan-=1
            if usuariogana==paraganar or maquinagana==paraganar:
                    break
        if usuariogana<maquinagana or maquinagana==paraganar:
            print("The machine is the winner!!!! Machine did win ",maquinagana ,"games")
        elif usuariogana==paraganar or maquinagana<usuariogana:
            print("User is the winner!!!! User did win ",usuariogana ,"games")           
        else:
            print("There are no winners, TIE!!!!")
        sys.exit() #lo he puesto para que el loop infinito termine al llegar al numero de partidas que se querian jugar
    else:
        if not is_odd(first_input) or is_more_or_equal_3(first_input):
            print("Failed! The number of games must be odd and greater than or equal to 5")
            continue