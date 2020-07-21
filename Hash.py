from TDA_Hash import crear_tabla, agregar_ta, agregar_tc, quitar_ta, quitar_tc
from TDA_Hash import buscar_tc, buscar_ta, cantidad_ta, cantidad_tc
from TDA_Hash import hash_division, hash_diccionario, bernstein, hash_division_contacto
from TDA_Hash import barrido_ta, barrido_tc
from math import sqrt
from TDA_Hash import hash_division_guiatel, hash_division_catedra, bernstein_contactos
from TDA_Hash import bernstein_st, hash_division_st, bernstein_star_wars, bernstein_palabra
from TDA_Hash import bernstein_pokemones
from random import randint, choice
from tda_lista import barrido_lista

'''1. Desarrollar un algoritmo que permita implementar una tabla hash para representar un 
diccionario que permita resolver las siguientes actividades:'''

# EJ 1
class Palabra():
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado

    def __str__(self):
        return self.palabra + ', ' + self.significado

#a. agregar una palabra y su significado al diccionario
tabla = crear_tabla(28)
def diccionario(tabla):
    palabra = Palabra('danzar', 'Bailar al ritmo de una música')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    palabra = Palabra('ballena','Animal mamífero marino')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    palabra = Palabra('madriguera','Cueva donde viven y se esconden algunos animales')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    palabra = Palabra('felicidad','Sentimiento de alegría o satisfacción')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    barrido_ta(tabla)

    #b. determinar si una palabra existe y mostrar su significado
    pos = buscar_ta(tabla, hash_diccionario, Palabra('Hola', ''), 'palabra')
    if(pos is not None):
        print('Palabra', pos.info.palabra, 'significado', pos.info.significado)
    print()

    #c. borrar una palabra del diccionario;
    print('Elemento eliminado:', quitar_ta(tabla, hash_diccionario, Palabra('Hielo', ''), 'palabra'))
    barrido_ta(tabla)

'''2. Desarrollar un algoritmo que implemente una tabla hash para una guía de teléfono, los 
datos que se conocen son número de teléfono, apellido, nombre y dirección de la persona. 
El campo clave debe ser el número de teléfono.'''

class Guia_Tel():
    def __init__(self, numero, apellido, nombre, direccion):
        self.numero = numero
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return str(self.numero) + ' | ' + self.apellido + ' | ' + self.nombre + ' | ' + self.direccion


def guia_telefono():
    tabla = crear_tabla(20)
    guiatel = Guia_Tel(randint(400000, 499999), 'Genaro', 'Arijon', 'Parana 234')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    guiatel = Guia_Tel(randint(400000, 499999), 'Federico', 'Gonzalez', 'Rpublica de Libano')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    guiatel = Guia_Tel(randint(400000, 499999), 'Nahuel', 'Mani', 'Barrio 150')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    guiatel = Guia_Tel(randint(400000, 499999), 'Pedro', 'Fister', '9 de julio 42')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    print('NUMERO DE TELEFONO | NOMBRE | APELLIDO | DIRECCION')
    barrido_ta(tabla)

#guia_telefono()

'''3. Implementar un tabla hash cerrada para guardar las cátedras de una carrera universitaria
de acuerdo a su código, que permita resolver las siguientes actividades:'''

class Catedra():
    def __init__(self, nombre, modalidad, horas, docente, codigo):
        self.nombre = nombre
        self.modalidad = modalidad
        self.horas = horas
        self.docente = docente
        self.codigo = codigo

    def __str__(self):
        return self.nombre + ' | ' + self.modalidad + ' | ' + self.horas + ' | ' + self.docente + ' | ' + str(self.codigo)


#a b c d y e 

def carrera_u ():
    tabla = crear_tabla(50)
    cargar_catedra = Catedra('Matematica Disccreta', 'Anual','120 horas', 'Marisa Romero', 100)
    agregar_tc(tabla, hash_division_catedra, cargar_catedra)
    cargar_catedra = Catedra('Calcuo', 'Anuela', ' 130 horas', 'Silvina y Susana', 108)
    agregar_tc(tabla,hash_division_catedra, cargar_catedra)
    cargar_catedra = Catedra('Algebra', 'Anual', '145 horas', 'Eugenia y Jesica', 109)
    agregar_tc(tabla, hash_division_catedra, cargar_catedra)
    cargar_catedra = Catedra('Ecuaciones diferenciales y calculo', 'Cuatrimestral :C', '50','Julio, Silvina', 106)
    agregar_tc(tabla,hash_division_catedra, cargar_catedra)
    print (' Nombre de la catedra  -   Modalidad   -   Horas -  Docente   - Codigo ')
    barrido_tc(tabla)

#carrera_u()

'''4. Desarrollar un algoritmo que implemente una tabla hash cerrada para cargar personajes
de Star Wars de los que solo se conoce su nombre'''
# EJ 4
class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

# a b c

def sw():
    tabla = crear_tabla(20)
    personajes = ['Darth Vader', 'Luke Skywalker', 'Chewbacca', 'Yoda', 'R2D2','Obi-Wan Keobi', 'Han Solo','C3PO', 'Rey','Finn',
        'Leia Organa', 'Jabba el Hutt',  'Jawa', 'Darth Maul', 'Bobba Fett', 'Jar Jar Binks', 'Darth Sidious', 'Kylo Ren',
        'Obi-Wan Kenobi', 'Greddo']
    pos = 0

    for i in range(0, len(personajes)):
        nombre = personajes[pos]
        dato = Personaje(nombre)
        agregar_tc(tabla, bernstein_star_wars, dato)
        pos += 1

    print('Tabla de personajes de Star Wars tiene ', len(tabla), ' posiciones')
    barrido_tc(tabla)

    porcentaje = (cantidad_tc(tabla)*100)/len(tabla)    # porcentaje de personajes ingresados en la tabla
    print('El porcentaje usado de la tabla es de: ', porcentaje)
    print()

    if porcentaje > 75:
        print('La carga ha superado el 75%. REHASHING:')
        tabla_duplicada = crear_tabla(len(tabla)*2)
        for dato in tabla:
            if dato is not None:
                agregar_tc(tabla_duplicada, bernstein_star_wars, dato)
        print('La nueva tabla tine :', len(tabla_duplicada), 'posiciones')
        barrido_tc(tabla_duplicada)
        porcentaje_tabla_duplicada = (cantidad_tc(tabla_duplicada)*100)/len(tabla_duplicada)
        print('Porcentaje usado en la tabla duplicada ', porcentaje_tabla_duplicada)


# ej 5
'''Desarrollar un algoritmo que implemente una tabla hash cerrada para administrar los
contactos de personas de las cuales se conoce nombre, apellido y correo electrónico,
contemplando las siguientes pautas:
a. El campo clave para generar las posiciones son el apellido y nombre.
b. Deberá contemplar una función de sondeo para resolver las colisiones.'''

class Contacto ():
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return self.nombre + ' | ' + self.apellido + ' | ' + ' | ' + self.email 

def administrar_contactos():
    tabla = crear_tabla(30)
    crear_contacto = Contacto('Victoria', 'Gimenez','vickygi@gmail.com')
    agregar_tc(tabla, hash_division_contacto,crear_contacto)
    crear_contacto = Contacto('Sofia', 'Hidalgo','sofi_hid@gmail.com')
    agregar_tc(tabla, hash_division_contacto,crear_contacto)
    crear_contacto = Contacto('Rocio', 'Suarez','ro_sua@gmail.com')
    agregar_tc(tabla, hash_division_contacto,crear_contacto)
    crear_contacto = Contacto('Carlos', 'Vives','carlos2020@gmail.com')
    agregar_tc(tabla, hash_division_contacto,crear_contacto)
    print('NOMBRE | APELLIDO | CORREO ELECTRÓNICO')
    barrido_tc(tabla)

#administrar_contactos()


#ej 6 que onda el ENUNCIADOOO XD HAHA
'''Darth Vader le encarga desarrollar los algoritmos para organizar los Stormtrooper cumpliendo 
con las siguientes demandas'''

class Stormtroopers():
    def __init__(self, legion, codigo):
        self.legion = legion
        self.codigo = codigo

    def __str__(self):
        return self.legion + ' ' + str(self.codigo)

def DVader():
    legion = [ 'FL',' TF' , 'TK', 'CT', 'FN', 'FO']
    tablaL = crear_tabla(10)
    tablaC = crear_tabla(1500)

    for i in range(1500):
        legion = choice(legion)
        cod = randint(1000, 5000)
        st = Stormtroopers(legion, cod)
    agregar_ta(tablaL, bernstein_st, st, 'legión')
    agregar_ta(tablaC, hash_division_st, st, 'código')
    print('Sormtroopers ordenados por legion: ')
    barrido_ta(tablaL)
    print('Stormtroopers ordenados por código: ')
    barrido_ta(tablaC)
    pos  =  hash_division ( 537 , tablaC )
    if  tablaC [ pos ]:
        print ( 'Stormtrooper designados para una misión de exploración' )
        barrido_lista ( tablaC [ pos ])
    print ()
    pos  =  hash_division ( 781 , tablaC )
    if  tablaC [ pos ]:
        print ( 'Stormrooper designados para una misión de asalto' )
        barrido_lista ( tablaC [ pos ])
    print ()
    posl  =  bernstein ( 'FN' , tablaL )
    if  tablaL [ posl ]:
        print ( 'Stormroopers de la Legión FN' )
        barrido_lista ( tablaL [ posl ])
    print ()
    posl  =  bernstein ( 'CT' , tablaL )
    if  tablaL [ posl ]:
        print ( 'Stormtroopers de la Legión CT' )
        barrido_lista ( tablaL [ posl ])

#DVader()

#7 Escribir un algoritmo que permita utilizar una tabla hash doble para guardar los datos de Pokémons

class Pokemon():
    def __init__(self, numero, nombre, tipo, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        return str(self.numero) + ' | ' + self.nombre + ' | ' + str(self.tipo) + ' | ' + str(self.nivel)

def tabla_pokemon():
    tabla = crear_tabla(1000)
    nombres = ['Groudon','Mew','Dialga','Palkia','Giratina','Darkrai','Kyogre', 'Xerneas', ' Manaphy','Phione',
    'El trio del lago','Kyogre Primigenio','Kyurem','Reshiram','Zekrom']
    tipo = ['Tierra','Psiquico','Acero/Dragón','Agua/Dragon','Fantasma/Dragon','Siniestro','Agua','Hada','Agua','Agua',
    'Psiquico', 'Agua','Dragón/Hielo','Dragón/Fuego','Dragón/Eléctrico']
    posicion = 0
    for i in range(len(nombres)):
        nom = nombres[posicion]
        tip = tipo[posicion]
        pokemon = Pokemon(randint(1, 500), nom, tip, randint(1, 60))
        agregar_tc(tabla, bernstein_pokemones, pokemon)
        posicion += 1

    print('Numero | Nombre | Tipo | Nivel')
    barrido_tc(tabla)
#tabla_pokemon()

#8 princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes

def alianza():
    pass

    def encriptar(oracion):
        clave = ""
        for letra in oracion:
            p1 = str(ord(letra)*37)
            p2 = hex(ord(letra)*2)
            clave += p1[0] + p2[1] + p2[3] + p1[1] + p1[2] + p2[0] + p1[3] + p2[2]
        return clave

    def desencriptar(clave):
        oracion = ""
        while len(clave) > 0:
            car = ""
            car += clave[0] + clave[3] + clave[4] + clave[6]
            clave = clave[8:]
            car = int(car)
            car = int(car/37)
            car = chr(car)
            oracion += car
        return oracion
    mensaje = '-Si te defines por tu poder de quitar la vida, por tu deseo de dominar, de poseer, entonces no eres nadie.-Obi-Wan Kenobi.'
    print('Mensaje a encripar:')
    print(mensaje)
    print()
    enpr = encriptar(mensaje)
    print('Mensaje encriptado:')
    print(enpr)
    print()
    dnpr = desencriptar(enpr)
    print('Mensaje desencriptado:')
    print(dnpr)


# 9 Desarrollar un algoritmo que permita cifrar y descifrar un mensaje carácter a carácter

def sms_cifrados():
    tabla = crear_tabla(10)
    tabla_aux = crear_tabla(10)

    def desifrar_sms(dato):
        dic = {'#?&': '0','abc': '1','def':'2','ghi':'3','jkl':'4','mnñ':'5','opq':'6','rst':'7','uvw':'8','xyz':'9'}
        cad = ''
        for i in range (0, len(dato), 3):
            cad += dic[dato[i:i+3]]
        return chr(int(cad))

    def cifrar_sms(dato):
        val = str(ord(dato))
        val_cirado = ['#?&','abc','def','ghi','jkl','mnñ','opq','rst','uvw','xyz']
        cad = ''
        for num in valor:
            num_ent = int(num)
            cad += val_cirado[num_ent]
        cad += "%"
        return cad

    mensaje = 'El amor y el odio, son dos lados de una misma cuchilla. –Jacqueline Carey.'
    mensaje_cifrado = ''

    print('Mensaje a cifrar: ')
    print(mensaje)
    print()

    for letra in mensaje:
        valor = buscar_ta(tabla, hash_diccionario, Palabra(letra, ''), 'palabra')
        cifrado = ''
        if valor is None:
            cifrado = cifrar_sms(letra)
            palabra = Palabra(letra, cifrado)
            agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
        else:
            cifrado = valor.info.significado
        mensaje_cifrado += cifrado
    print('Mensaje cifrado:')
    print(mensaje_cifrado)
    print()

    lista = mensaje_cifrado.split('%')
    lista.pop()

    sms = ''
    for letras in lista:
        valor = buscar_ta(tabla_aux, bernstein_palabra, Palabra(letras, ''), 'palabra')
        decifrado = ''
        if valor is None:
            decifrado = desifrar_sms(letras)
            palabra = Palabra(letras, decifrado)
            agregar_ta(tabla_aux, bernstein_palabra, palabra, 'palabra')
        else:
            decifrado = valor.info.significado
        sms += decifrado
    print('El mensaje ha sido decifrado')
    print(sms)


# EJ 10) Ahora Fury nos solicita desarrollar el algoritmo que permita decodificar los mensajes, contemplando las siguientes pautas:


def agencia():
    pass

    def hash_cadenas(string):
        hash = 5381
        for caracter in string:
            hash = ((hash << 5) + hash) + ord(caracter)
        return hash & 0xFFFFFFFF

    def calculo_comp(caracter):
        if ord(caracter) <= 78:
            return 79 + ord(caracter) - 32
        else:
            return 32 + ord(caracter) - 79

    def cod(carac):
        caracteres = ''
        car_ascii = ord(carac)
        car_ascii *= 37
        compl = calculo_comp(carac)
        car_ascii = str(car_ascii)


        for dig in car_ascii:
            digito = int(digito)
            num = pow(digito, 2) + compl
            carac = chr(int(num))
            caracteres += carac
        caracteres += chr(compl)
        return caracteres

    def codifica_segm(segmento):
        num_4_dig = ''
        pri_chr = segmento[:4]
        ult_chr = segmento[4]
        compl = ord(ult_chr)
        for elemento in pri_chr:
            elemento = ord(elemento) - compl
            elemento = int(sqrt(elemento))
            elemento = str(elemento)
            num_4_dig += elemento
        num_4_dig = int(num_4_dig)
        chr_ascii = int(num_4_dig/37)
        car = chr(chr_ascii)
        return car

    def decod(mensaje):
        oracion = ''
        i = 0
        while i < len(mensaje):
            segmento = mensaje[i:i+5]
            indice = hash_cadenas(segmento) % len(tabla)
            if (tabla[indice] is None):
                car = codifica_segm(segmento)
                tabla[indice] = car
            else:
                car = tabla[indice]
            oracion += car
            i += 5
        return oracion

    tabla = crear_tabla(240)

#APRENDI SOBRE STAR WARS, POKEMON Y TODOO DE PASO XD, WALTER CRAK AH




