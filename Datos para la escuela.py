
diccionario_alumnos = { 'Rodolfo Blanco': {'Nombre': 'Rodolfo', 'Apellido': 'Blanco','DNI': 9567123,'Fecha de Nacimiento': '14 de Abril del 1943', 'Tutor': 'Alberto Blanco', 'Notas': [2, 3, 4, 6, 9, 9, 9], 'Faltas': 0, 'Amonestaciones': 6 },
    'Mailo Lopez': { 'Nombre': 'Mailo', 'Apellido': 'Lopez','DNI': 65163009,'Fecha de Nacimiento': '14 de Septiembre del 2009','Tutor': 'Julio Lopez','Notas': [9, 9, 9, 9, 9, 9],  'Faltas': 3, 'Amonestaciones': 0 },
    'Sergio Plaza': {'Nombre': 'Sergio','Apellido': 'Plaza', 'DNI': 34012019, 'Fecha de Nacimiento': '22 de Agosto del 2002', 'Tutor': 'Ariel Plaza', 'Notas': [7, 8, 8, 6, 9, 9, 9], 'Faltas': 2,'Amonestaciones': 2 },
    'Alvaro Rodriguez': {'Nombre': 'Alvaro','Apellido': 'Rodriguez',  'DNI': 56562024, 'Fecha de Nacimiento': '16 de Mayo del 2008',  'Tutor': 'Marcelo Rodriguez', 'Notas': [6, 5, 8, 4, 9, 9, 9], 'Faltas': 0, 'Amonestaciones': 2 },
    'Rocio Barranco': { 'Nombre': 'Rocio',  'Apellido': 'Barranco', 'DNI': 48524678, 'Fecha de Nacimiento': '12 de Junio del 2006', 'Tutor': 'Julia Meontero', 'Notas': [2, 3, 5, 8, 5, 0, 7], 'Faltas': 5, 'Amonestaciones': 0 },
    'Macarena Guerra': {'Nombre': 'Macarena','Apellido': 'Guerra', 'DNI': 66178184, 'Fecha de Nacimiento': '14 de Abril del 2004', 'Tutor': 'Olivia Garces', 'Notas': [2, 3, 5, 6, 7, 8, 8],'Faltas': 22,'Amonestaciones': 1 },
    'Virginia Bonifacio': {'Nombre': 'Virginia','Apellido': 'Bonifacio', 'DNI': 52245976, 'Fecha de Nacimiento': '23 de Marzo del 2001', 'Tutor': 'Aida Lopez', 'Notas': [5, 6, 8, 9, 4, 6, 9], 'Faltas': 12, 'Amonestaciones': 1 },
    'Irma Lopez': {'Nombre': 'Irma','Apellido': 'Lopez', 'DNI': 54456894, 'Fecha de Nacimiento': '4 de Julio del 2003', 'Tutor': 'Lucas Lopez', 'Notas': [9, 9, 9, 8, 9, 9, 9], 'Faltas': 3,'Amonestaciones': 3} }
print ('Bienvenido a la plataforma Educativa. 💻')
print ('-------------------------------------------')
print ('Usted puede elegir entre las siguientes opciones 👉🏻')
print ('--------------------------------------------------------')
print ('📃 1- Consultar lista de alumnos')
print ('📝 2- Modificar datos de alumnos')
print ('✅ 3- Agregar Alumno')
print ('❌ 4- Expulsar Alumno')
print ('--------------------------------------------------------')
print ('🔚 - Salir del programa.')
print ('--------------------------------------------------------')
opcion1 = ' 1- Consultar lista de alumnos'
opcion2 = ' 2- Modificar datos de alumnos'
opcion3 = '✅ 3- Agregar Alumno'
opcion4 = '❌ 4- Expulsar Alumno'
opcion5 = 'Salir'

while True:
    seleccion = input('¿Qué opción desea? Escriba el número: ')

    if seleccion == '1':
        print(f'La lista de los alumnos es la siguiente:\n{diccionario_alumnos}')

    elif seleccion == '2':
        while True:
            alumno_a_modificar = input('Nombre del alumno a modificar: ')
            if alumno_a_modificar in diccionario_alumnos:
                while True:
                    dato_a_modificar = input('¿Qué dato desea modificar? (Nombre, Apellido, DNI, Fecha de Nacimiento, Tutor, Notas, Faltas, Amonestaciones): ')
                    if dato_a_modificar in diccionario_alumnos[alumno_a_modificar]:
                        nuevo_dato = input('Introduzca el nuevo dato: ')
                        diccionario_alumnos[alumno_a_modificar][dato_a_modificar] = nuevo_dato
                        print(f'El dato {dato_a_modificar} se ha modificado correctamente.')
                        break
                    else:
                        print(f'El dato {dato_a_modificar} no existe para el alumno {alumno_a_modificar}')
                break
            else:
                print('Alumno no encontrado. 🤷🏻‍♀️🤷🏻‍♂️')

    elif seleccion == '3':
        while True:
            nuevo_alumno = {
                'Nombre': input('Nombre: '),
                'Apellido': input('Apellido: '),
                'DNI': int(input('DNI: ')),
                'Fecha de Nacimiento': input('Fecha de Nacimiento: '),
                'Tutor': input('Tutor: '),
                'Notas': [],
                'Faltas': 0,
                'Amonestaciones': 0
            }
            diccionario_alumnos.update({nuevo_alumno['Nombre']: nuevo_alumno})
            print ( f'El alumno {nuevo_alumno["Nombre"]} se ha agregado correctamente.✅')
            break

    elif seleccion == '4':
        while True:
            alumno_a_eliminar = input('¿A quién quieres eliminar? Escriba el nombre: ')
            if alumno_a_eliminar in diccionario_alumnos:
                confirmacion = input('¿Está seguro de que desea eliminar al alumno {}? (Si/No): '.format(alumno_a_eliminar))
                if confirmacion.lower() == 'si':
                    del diccionario_alumnos[alumno_a_eliminar]
                    print(f'El alumno {alumno_a_eliminar} se ha eliminado correctamente.✅')
                    break
                else:
                    print('Eliminación cancelada.🚫')
            else:
                print('Alumno no encontrado. ⚠')

    elif seleccion == opcion5:
        print('¡Hasta pronto!Muchas Gracias')
        break
    else:
        print('Opción Invalida ❗❗❗.')