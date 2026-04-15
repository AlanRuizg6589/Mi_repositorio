Edad = int(input("Cual es tu edad? "))
Inscripcion = input("Estas inscrito previamente? (SI/NO) ")
if Edad >= 18:
    if Inscripcion == "SI":
        print("Inscripción aceptada")
    else:
        print("Inscripción rechazada")
elif Edad < 18:
    print("Debe ser mayor de edad para poder inscribirse")
print("Fin del proceso")