diccionario_alumnos = {
    'Rodolfo Blanco': {
        'Nombre': 'Rodolfo',
        'Apellido': 'Blanco',
        'DNI': 9567123,
        'Fecha de Nacimiento': '14 de Abril del 1943',
        'Tutor': 'Alberto Blanco',
        'Notas': [2, 3, 4, 6, 9, 9, 9],
        'Faltas': 0,
        'Amonestaciones': 6 },
    'Matias Lopez': {
        'Nombre': 'Matias',
        'Apellido': 'Lopez',
        'DNI': 65163009,
        'Fecha de Nacimiento': '14 de Septiembre del 2009',
        'Tutor': 'Julio Lopez',
        'Notas': [9, 9, 9, 9, 9, 9],
        'Faltas': 3,
        'Amonestaciones': 0 },
    'Sergio Plaza': {
        'Nombre': 'Sergio',
        'Apellido': 'Plaza',
        'DNI': 34012019,
        'Fecha de Nacimiento': '22 de Agosto del 2002',
        'Tutor': 'Ariel Plaza',
        'Notas': [7, 8, 8, 6, 9, 9, 9],
        'Faltas': 2,
        'Amonestaciones': 2 },
    'Alvaro Rodriguez': {
        'Nombre': 'Alvaro',
        'Apellido': 'Rodriguez',
        'DNI': 56562024,
        'Fecha de Nacimiento': '16 de Mayo del 2008',
        'Tutor': 'Marcelo Rodriguez',
        'Notas': [6, 5, 8, 4, 9, 9, 9],
        'Faltas': 0,
        'Amonestaciones': 2 },
    'Rocio Barranco': {
        'Nombre': 'Rocio',
        'Apellido': 'Barranco',
        'DNI': 48524678,
        'Fecha de Nacimiento': '12 de Junio del 2006',
        'Tutor': 'Julia Meontero',
        'Notas': [2, 3, 5, 8, 5, 0, 7],
        'Faltas': 5,
        'Amonestaciones': 0 },
    'Macarena Guerra': {
        'Nombre': 'Macarena',
        'Apellido': 'Guerra',
        'DNI': 66178184,
        'Fecha de Nacimiento': '14 de Abril del 2004',
        'Tutor': 'Olivia Garces',
        'Notas': [2, 3, 5, 6, 7, 8, 8],
        'Faltas': 22,
        'Amonestaciones': 1 },
    'Virginia Bonifacio': {
        'Nombre': 'Virginia',
        'Apellido': 'Bonifacio',
        'DNI': 52245976,
        'Fecha de Nacimiento': '23 de Marzo del 2001',
        'Tutor': 'Aida Lopez',
        'Notas': [5, 6, 8, 9, 4, 6, 9],
        'Faltas': 12,
        'Amonestaciones': 1 },
    'Irma Lopez': {
        'Nombre': 'Irma',
        'Apellido': 'Lopez',
        'DNI': 54456894,
        'Fecha de Nacimiento': '4 de Julio del 2003',
        'Tutor': 'Lucas Lopez',
        'Notas': [9, 9, 9, 8, 9, 9, 9],
        'Faltas': 3,
        'Amonestaciones': 3}
}
print ('Bienvenido a la plataforma de la escuela!')
print ('Usted puede elegir entre las siguientes opciones 👉🏻')
print ('📃 1- Consultar lista de alumnos')
print ('📝 2- Modificar datos de alumnos')
print ('✅ 3- Agregar Alumno')
print ('❌ 4- Expulsar Alumno')
opcion1 = '1'
opcion2 = '2'
opcion3 = '3'
opcion4 = '4'
opion5 = 'Salir' 
while True:
    seleccion= (input('Escriba la opcion que usted desea: '))
    if seleccion == '1':
        print(f'La lista de los alumnos es la siguiente: /n {diccionario_alumnos}')
    elif seleccion == '2':
        print ('Puede modificar los datos  de los siguiente alumnos: /n')
        
        print (f'El Dionario alumnos a sido modificado. Puede verlo acontinuacion:/n {diccionario_alumnos}')
    elif seleccion =='3': 
        print ('Agregar Alumno Nuevo: ')
        nuevo_alumno = {
        'Nombre': input(''),
        'Apellido': input(''),
        'DNI': input() ,
        'Fecha de Nacimiento': input(''),
        'Tutor': input(''),
        'Notas': input(),
        'Faltas': input (),
        'Amonestaciones': input() }
        diccionario_alumnos.update({nuevo_alumno})
    elif seleccion == '4':
        print ('¿A quíen quieres eliminar?')
        alumno_eliminado= input('Escriba el nombre: ')
        info_alumnos= diccionario_alumnos.get(alumno_eliminado)
        if info_alumnos:
            print (f'Los datos de {alumno_eliminado}: ')
            print (info_alumnos)
            diccionario_alumnos.pop(alumno_eliminado, None)
            print (f'El alumno {alumno_eliminado}, se quitó del Diccionario de Alumnos de la Institucion. Si fue un Error reinicie el proeso, marque opcion 3 y registrelo nuevamente. Gracias.')
        else:
            print ('No esta la informacion de quien usted solicita.')
    elif seleccion == opion5:
        print (input('Escriba salir a continuacion: '))
        break
    
