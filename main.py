from Figurasgeometricas import Figurasgeometricas
from Triangulo import Triangulo
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Cilindro import Cilindro
from Paralelograma import Paralelograma




while True:
    print("-----------------MENU------------")
    print("triangulo (1) ")
    print("circulo (2) ")
    print("cuadrado (3) ")
    print("rectangulo (4) ")
    print("rectangulo (5) ")
    print("paralelogramo (6) ")
    print("Cerrar (0) ")
    opcion = input("digite el numero de la figura que desea hallar el area: ")
    if opcion == "1":
        base = int(input("digite la base: "))
        altura = int(input("digite la altura: "))
        tr = Triangulo(altura,base)
        print("el area del triangulo es: ",opcion, "es", tr.area())
    elif opcion =="2":
        radio = int(input("digite el radio: "))
        ci = Circulo(radio)
        print("El area del circulo es:",opcion, "es",ci.area())
    elif opcion == "3":
        lado = float(input("digite el lado del cuadrado: "))
        cu = Cuadrado(lado)
        print("El area del cuadrado es:",opcion, "es",cu.area())
    elif opcion == "4":
        base = float(input("digite la base: "))
        altura = float(input("digite la altura: "))
        re = Rectangulo(base,altura)
        print("El area del rectangulo es:",opcion, "es" ,re.area())
    elif opcion == "5":
        radio_c = float(input("digite el radio: "))
        altura_c = float(input("digite la altura:  "))
        cil = Cilindro(opcion)
        cil.radio = radio_c
        cil.altura = altura_c
        print("El area del rectangulo es:",opcion, "es" ,cil.area())
    elif opcion == "6":
        altura_p = float(input("digite la altura: "))
        base_p = float(input("digite la base: "))
        pa = Paralelograma(opcion)
        pa.altura = altura_p
        pa.base = base_p
        print("El area del rectangulo es:",opcion, "es" ,pa.area())
    else: 
        opcion == "0"
        print("fin del programa")
        break
    






