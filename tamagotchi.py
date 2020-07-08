import math

DecreGral = 0.03 #Decremento de las estadisticas en cada turno
DecreTipo = 0.05 #Decremento segun tipo de mascota

#Declaracion de clase Tmascota
def IniciarJuego():
    class Tmascota():
        def __init__(self,tipo,nombre):
            self.tipo = tipo
            self.nombre = nombre
            self.foto = ''
            self.sed = 0.8 + DecreGral
            self.peso = 0.8 + DecreGral
            self.felicidad = 0.8 + DecreGral
            self.anios = 1
            self.jugar = True 

        def comer(self):
            if (mascota.peso < 10.00) and (mascota.peso > 0):
                if 10-mascota.peso < 9.85 :
                    mascota.peso = mascota.peso+0.25
                    mascota.sed = mascota.sed-0.06
                else: print(' no tiene hambre.')

        def TomarAgua(self):
            if (mascota.sed < 10.00) and (mascota.sed >0):
                if (10-mascota.sed)< 9.85:
                    mascota.sed=mascota.sed+0.25
                    mascota.peso=mascota.peso - 0.07
                else:
                    mascota.sed=(10-mascota.sed)
            else: print(' no tiene sed.')

        def Jugar(self):
            if (mascota.felicidad < 10.00)and(mascota.felicidad>0):
                if (10-mascota.felicidad)< 9.85:
                    mascota.felicidad = mascota.felicidad + 0.25
                    mascota.sed = mascota.sed - 0.07
                    mascota.peso = mascota.peso - 0.06
                else:
                    mascota.felicidad = (10-mascota.felicidad)
            else: print(mascota.nombre,' no quiere jugar.')

        def Ignorar(self):
            mascota.peso = mascota.peso
            mascota.sed = mascota.sed
            mascota.felicidad = mascota.felicidad

        def DejarJuego(self):
            print('')
            print('Gracias por jugar.')
            print('')
            mascota.jugar = False

    def ElijirAccion(accion):
            if accion == '1':
                mascota.comer()
            elif accion =='2':
                mascota.TomarAgua()
            elif accion == '3': 
                mascota.Jugar()
            elif accion == '4':
                mascota.Ignorar()
            elif accion == '5':
                mascota.DejarJuego()
            else: print('Accion no valida.')

    print('Elija el nombre de su mascota:')
    nombre = input()
    print('')
    check = False

    while check == False:
            print('Elija un tipo de mascota: 1:perro  2:gato  3:rata.')
            tipo = input()
            mascota = Tmascota(tipo,nombre)
            if tipo == '1':
                foto = '(V._.V)'
                check = True
            elif tipo == '2':
                    foto = '(^._.^)'
                    check = True
            elif tipo == '3':
                    foto = '<:3 )~'
                    check = True
            else: print('Tipo no disponible.')
            print('')

    mascota = Tmascota(tipo,nombre)
    mascota.foto = foto

    mascota.anios=1
    mascota.sed=8.00 + DecreGral
    mascota.peso=8.00 + DecreGral
    mascota.felicidad=8.00 + DecreGral

    while (mascota.jugar == True) and ((mascota.peso > 0) and (mascota.sed>0) and(mascota.felicidad>0)and (mascota.anios<13)) :
        edad = mascota.anios + 0.05
        mascota.anios = math.trunc(edad)
        mascota.peso = mascota.peso - DecreGral
        mascota.sed = mascota.sed - DecreGral
        mascota.felicidad = mascota.felicidad - DecreGral

        if mascota.tipo == 'perro':
            mascota.felicidad = mascota.felicidad-DecreTipo
        elif mascota.tipo == 'gato':
            mascota.sed = mascota.sed-DecreTipo
        else: mascota.peso= mascota.peso-DecreTipo

        print('-----------------------------------')
        print('')
        print(mascota.foto)
        print('')
        print('-----------------------------------')
        print('| edad  | peso | sed  | felicidad |')
        print('-----------------------------------')
        print('|  ',round(mascota.anios,2),'| ',round(mascota.peso,2),' | ',round(mascota.sed,2),' | ', round(mascota.felicidad,2),' |')
        print('-----------------------------------')
        print('')
        print('Seleccione una accion: 1: Comer   2: Tomar Agua  3: Jugar con ',mascota.nombre,'  4: Ignorar   5: Para dejar de jugar.')
        accion=input()
        ElijirAccion(accion)
        print('')


    if (mascota.peso <= 0) or (mascota.sed<=0) or (mascota.felicidad<=0) or (mascota.anios>=13):
        print(mascota.nombre,' murio.')

    print('')

def Instrucciones():
    print('--------------------------------------------------------------------------------------')
    print('')
    print('Instrucciones: ')
    print('')
    print(' + Primero debe crear su personaje, debe elegir un nombre y que mascota quiere')
    print('   puede elegir entre un perro, un gato o una rata.')
    print('')
    print(' + Luego debe mantener viva a su mascota, para esto debe darle de comer,')
    print('   beber y jugar con ella .')
    print('')
    print(' + Tenga en cuenta que cada accion que realiza modifica las estadisticas de')
    print('   su mascota, cuando la alimente subira de peso pero tendra mas sed, cuando')
    print('   la de agua tendra mas hambre, si juega con ella tendra mas hambre y sed.')
    print('')
    print(' + Recuerde que si ignora a su mascota todas sus estadisticas bajaran en cada turno.')
    print('')
    print(' + Si deja que alguna de las estadisticas llegue a 0 su mascota morira.')
    print('')
    print(' + Cada tipo de mascota tiene una necesidad especial, el perro requiere jugar mas tiempo,')
    print('   el gato requiere tomar agua mas seguido y la rata requiere comer mas.')
    print('')
    print('--------------------------------------------------------------------------------------')
    print('')

def MenuInicial():
    print('')
    print('Bienvenido!')
    menu = False
    while menu == False:
        print('Elija una opcion 1:Jugar  2:Instrucciones  3:Salir.')
        opcion = input()
        if opcion == '1':
            IniciarJuego()
        elif opcion == '2':
            Instrucciones()
        elif opcion =='3':
            menu = True
        else: print('Ingrese una opcion disponible.')

MenuInicial()