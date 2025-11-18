
nombre = input("que figura desea usar: ")
print("la figura seleccionada es",nombre)

#distincion clase padre figura geometrica
fg = Figurasgeometricas(nombre)

#llamo la funcion paracalcular el area
tr = Triangulo(10,20)
tr.nombre = nombre