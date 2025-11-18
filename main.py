from Figurasgeometricas import Figurasgeometricas
from Triangulo import Triangulo





while True:
    print("-----------------MENU------------")
    print("triangulo(1)")
    print("circulo(2)")
    print("cuadrado(3)")
    print("rectangulo(4)")
    print("Cerrar(0)")
    opcion = input("digite el numero de la figura que desea hallar el area: ")
    if opcion == "1":
        base = int(input("digite la base: "))
        altura = int(input("digite la altura: "))
        tr = Triangulo(altura,base)
        print("el area del triangulo es: ",opcion, "es", tr.area())
   


        



