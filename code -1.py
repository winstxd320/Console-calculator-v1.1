import time
import os
import colorama
def animation():
    animacion = [".  ", ".. ", "...", ".  ", ".. ", "...", ".  ", ".. ", "...", ".  ", ".. ", "..."]
    for i in animacion:
        time.sleep(0.5)
        print("EXECUTING ACTION" + str(i), end="\r")
def clear():
    os.system('cls')
def cont(i):
    i += 1
    return i
def suma():
    try:
        while True:
            cant_sumar = int(input("Introduzca la cantidad de veces a sumar:\n>"))
            if cant_sumar >= 20:
                print(colorama.Fore.RED + "THE SYSTEM DETECTED THAT A HIGH NUMBER OF SUM ATTEMPTS HAS BEEN ENTERED.")
                continue
            if cant_sumar > 0:
                acum = 0.0
                for i in range(cant_sumar):
                    cont(i)
                    n = float(input(f"Introduzca el ({cont(i)}) número a restar:\n>"))
                    acum = acum + n
                print(f"El resultado de la suma es: {acum}")
                op_des = int(input("Volver al menú:(1)\nVolver a sumar valores:(2)\n>"))
                if op_des == 1:
                    animation()
                    clear()
                    break
                elif op_des == 2:
                    animation()
                    clear()
            else:
                print(colorama.Back.RED + "---->'ERROR. ENTER A WHOLE AMOUNT OR A NUMBER GREATER THAN (0)'")
    except:
        print(colorama.Back.RED + "---->'ERROR TRY AGAIN'")
def resta():
    try:
        while True:
            cant_resta = int(input("Ingrese la cantida de veces a restar:\n>"))
            if cant_resta > 1:
                if cant_resta >= 21:
                    print(colorama.Back.RED + "THE SYSTEM DETECTED THAT A HIGH NUMBER OF SUBTRACTION ATTEMPTS HAS BEEN ENTERED")
                    continue
                print(colorama.Back.GREEN + "NOTA: EL NÚMERO INGRESADO TIENE QUE SER MAYOR A (0). ")
                n_inicial = float(input("Introduzca el valor inicial a restar:\n>"))
                if n_inicial >= 1:
                    for i in range(cant_resta):
                        cont(i)
                        n = float(input(f"Introduzca el ({cont(i)}) número a restar:\n>"))
                        n_inicial = n_inicial - n
                    print(f"El resultado de la resta es: {n_inicial}")
                    op_des = int(input("Volver al menú:(1)\nVolver a resta valores:(2)\n>"))
                    if op_des == 1:
                        animation()
                        clear()
                        break
                    elif op_des == 2:
                        animation()
                        clear()
                else:
                    print(colorama.Back.RED + f"---->'THE SYSTEM DETECTED THAT THE INITIAL VALUE ENTERED WAS {n_inicial}. ENTER A NUMBER GREATER THAN (0)'")
            else:
                print(colorama.Back.RED + "---->'ERROR. ENTER A WHOLE AMOUNT OR A NUMBER GREATER THAN (0)'")
    except:
        print(colorama.Back.RED + "---->'ERROR TRY AGAIN'")
def multipllicacion():
    try:
        while True:
            cant_mult = int(input("Ingrese la cantidad de veces a multiplicar:\n>"))
            if cant_mult > 1:
                if cant_mult >= 20:
                    print(colorama.Back.RED + "THE SYSTEM DETECTED THAT A HIGH NUMBER OF MULTIPLICATION ATTEMPTS HAS BEEN ENTERED.")
                    continue
                n_inical = float(input("Introduzca el número a multiplicar:\n>"))
                for i in range(cant_mult):
                    cont(i)
                    n = float(input(f"Introduzca el ({cont(i)}) número a multiplicar:\n>"))
                    n_inical = n_inical * n
                print(f"El resultado de la multiplicación es: {n_inical}")
                op_des = int(input("Volver al menú:(1)\nVolver a multiplicar valores:(2)\n>"))
                if op_des == 1:
                    animation()
                    clear()
                    break
                elif op_des == 2:
                    animation()
                    clear()
            else:
                print(colorama.Back.RED + "---->'ERROR. ENTER A WHOLE AMOUNT OR A NUMBER GREATER THAN (0)'")
    except:
        print(colorama.Back.RED + "---->'ERROR TRY AGAIN'")
def division():
    try:
        while True:
            cant_div = int(input("Ingrese la cantidad de veces a dividir:\n"))
            if cant_div > 0:
                if cant_div >= 20:
                    print(colorama.Back.RED + "THE SYSTEM DETECTED THAT A HIGH NUMBER OF SUBTRACTION ATTEMPTS HAS BEEN ENTERED")
                    continue
                n_inicial = float(input("Ingrese el número inicial a dividir:\n>"))
                if n_inicial > 0:
                    for i in range(cant_div):
                        cont(i)
                        n = float(input(f"Ingrese el ({cont(i)}) a dividir:\n>"))
                        n_inicial /= n
                    print(f"El resutado de la división es: {n_inicial}")
                    op_des = int(input("Volver al menú:(1)\nVolver a dividir valores:(2)\n>"))
                    if op_des == 1:
                        animation()
                        clear()
                        break
                    elif op_des == 2:
                        animation()
                        clear()
                print(colorama.Back.RED + f"---->'THE SYSTEM DETECTED THAT THE INITIAL VALUE ENTERED WAS {n_inicial}. ENTER A NUMBER GREATER THAN (0)'")
            else:
                print(colorama.Back.RED + "---->'ERROR. ENTER A WHOLE AMOUNT OR A NUMBER GREATER THAN (0)'")
    except:
        print(colorama.Back.RED + "---->'ERROR TRY AGAIN'")
def dib_tabla_mult():
    try:
        while True:
            n_tabla = int(input("Ingrese el número de la tabla a dibujar:\n>"))
            if n_tabla >= 1 and n_tabla <= 20:
                for i in range(12):
                    cont(i)
                    print(colorama.Fore.BLUE + f"{n_tabla} * {cont(i)} = {n_tabla * cont(i)}")
                op_des = int(input("Volver al menú:(1)\nVolver a dibujar valores:(2)\n>"))
                if op_des == 1:
                    animation()
                    clear()
                    break
                elif op_des == 2:
                    animation()
                    clear()
            else:
                print(colorama.Back.RED + "THE MAXIMUM RANGE TO DRAW A MULTIPLICATION TABLE IS (20).")
    except:
        print(colorama.Back.RED + "---->'ERROR TRY AGAIN'")
def main():
    colorama.init(autoreset= True)
    while True:
        try:
            print(colorama.Fore.RED + "-----------------------------------------------")
            print(colorama.Fore.GREEN + "|      Calculadora de consola                 |")
            print(colorama.Fore.RED + "-----------------------------------------------")
            print(colorama.Fore.RED + "|***** Digite una opción: *****               |")
            print(colorama.Fore.RED + "|+++++ 1 - Suma ++++++++++++++++++++++++++++++|")
            print(colorama.Fore.RED + "|----- 2 - Resta------------------------------|")
            print(colorama.Fore.RED + "|***** 3 - Multiplicación ********************|")
            print(colorama.Fore.RED + "|///// 4 - División///////////////////////////|")
            print(colorama.Fore.RED + "|/*/*/ 5 - Dibujar tabla de multiplicar */*/*/|")
            print(colorama.Fore.RED + "|      6 - Salir        made for winstXS320   |")
            print(colorama.Fore.RED + "-----------------------------------------------")
            op = int(input("Introduzca un número del menú:\n>"))
            if op == 1:
                animation()
                clear()
                suma()
            elif op == 2:
                animation()
                clear()
                resta()
            elif op == 3:
                animation()
                clear()
                multipllicacion()
            elif op == 4:
                animation()
                clear()
                division()
            elif op == 5:
                animation()
                clear()
                dib_tabla_mult()
            elif op == 6:
                animation()
                time.sleep(2)
                break
        except:
            print(colorama.Back.RED + "---->'ERROR TRY AGAIN'")
#Funciones principales
main()