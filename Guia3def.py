# El siguiente sistema sirve para emitir el proximo turno y la receta medica de los pacientes de un consultorio medico.

fechaActual = input("Ingrese la fecha del dia de hoy : ")
nombreMedico = input("Ingrese el nombre del Dr/a : ")
nombrePaciente = input("Ingrese el nombre y apellido del paciente : ")
edadPaciente = int(input("Ingrese la edad del paciente : "))
diagnosticoMedico = input("Ingrese el diagnostico del paciente : ")
medicamento = input("Ingrese el nombre del medicamento recetado : ")
indicaciones = int(input("Indique la cantidad de veces al dia que debe ingerir : "))
cantDias = int(input("Ingrese el total de dias que dura el tratamiento : "))
proxTurno = input("Ingrese la fecha del proximo turno : ")

#La siguiente etapa del sistema define la salida de los datos ingresados con toda la informacion emitida por la clinica.

print ("\t\t---- Sanatorio Allende - Obispo Oro 42 – Córdoba ----")
print (f"\n{fechaActual}")
print (f"\nDr/Dra : {nombreMedico} .")
print (f"Paciente : {nombrePaciente} / Edad {edadPaciente}")
print (f"Diagnostico : {diagnosticoMedico}")
print (f"Debera ingerir : {medicamento} . {indicaciones} veces al dia durante {cantDias} dias.")
print(f"\nSu proxima cita es el dia {proxTurno}")
print(f"\n\n______________\t\t\t\t\t__________")
print(f"Firma Dr/Dra\t\t\t\t\tAclaracion")
print ("\n\t\t---- Ante cualquier consulta no dude en llamarnos al tel : (0351) 4234234 ----")