#saludo
saludo = "Reciban un cordial saludo de nuestra parte, en esta ocasión, hemos elaborado un programa capaz de brindar información de los integrantes de nuestro grupo(nombre completo, edad y sexo), "
saludo += "sin mas que agregar, acontinuación se darán los datos de los integrantes. "
print(saludo)
print("    ")
# Variables con los datos de cada uno
nombres1 = "Bryan Alexis "
apellidos1 = "Rauda Gómez, "
nombres2 = "Jeremy Odir "
apellidos2 = "Fuentes Soriano, "
nombres3 = "Karla Patricia " 
apellidos3 = "Miranda Orellana, "
nombres4  = "Jonathan Humberto "
apellidos4 = "Alas Landaverde, "
nombres5 = "Mónica Nohemi "
apellidos5 = "Orallana Arteaga, "
edad1 = 18
edad2 = 19
edad3 = 17
edad4 = 17
edad5 = 20
gen1= "Masculino"
gen2= "Femenino"
print("DATOS DE LOS INTEGRANTES:")
print("    ")
# Variables de complemento
x = "Nombre completo: "
y = "edad: "
y2 = " años,"
z = " sexo: "
# Codigo
dato1 = ("Integrante 1: "f"{x}{nombres1}{apellidos1}{y}{edad1}{y2}{z}{gen1}"". Al finalizar la carrera tendrá "f"{edad1 + 5} años de edad.")
dato2 = ("Integrante 2: "f"{x}{nombres2}{apellidos2}{y}{edad2}{y2}{z}{gen1}"". Al finalizar la carrera tendrá "f"{edad2 + 5} años de edad.")
dato3 = ("Integrante 3: "f"{x}{nombres3}{apellidos3}{y}{edad3}{y2}{z}{gen2}"". Al finalizar la carrera tendrá "f"{edad3 + 5} años de edad.")
dato4 = ("Integrante 4: "f"{x}{nombres4}{apellidos4}{y}{edad4}{y2}{z}{gen1}"". Al finalizar la carrera tendrá "f"{edad4 + 5} años de edad.")
dato5 = ("Integrante 5: "f"{x}{nombres5}{apellidos5}{y}{edad5}{y2}{z}{gen2}"". Al finalizar la carrera tendrá "f"{edad5 + 5} años de edad.")
print(dato1)
print("   ")
print(dato2)
print("   ")
print(dato3)
print("   ")
print(dato4)
print("   ")
print(dato5)
print("   ")
edadPromedio = (edad1+edad2+edad3+edad4+edad5)/5
print("El promedio de la edad actual del grupo es de: ", edadPromedio, "años")
