from fsudoku import *
import time
#Diego Reyna A01657387 & Diógenes Grajales A01653251


#en el menu, si teclea 628, se genera una partida predefinida que automáticamente gana
#si teclea 314, se genera la misma partida, pero le faltan tres números, que se tendrán que ingresar para ganar la partida
#si teclea 777, se utiliza la función de crear una partida completamente aleatoria, que tarda mucho, por lo que no es parte del juego

#selección de idioma
selecidio=-1
print('Hola / Hello / Bonjour')
time.sleep(.5)
print()
while selecidio<1:
    print('Idioma / Langue / Language')
    print('Español-->1\nEnglish-->2\nFrançais-->3')
    idioma=input()
    #revisar si es una opción válida, que no sea un string o un número fuera del rango
    selecciones=['1','2','3']
    selecidio=0
    if idioma in selecciones:
        #Español
        if idioma=='1':
            selecidio=1
            print('Bienvenido')
            coordenada1x='Coordenada en x: '
            coordenada1y='Coordenada en y: '
            numero='Número: '
            coordenada='Coordenada: '
            cinválida='\nEntrada inválida, intenta de nuevo.'
            denuevo='Intenta de nuevo'
            felicidades='Felicidades, ganaste'
            load3='Cargando...'
            load2='Cargando..'
            load1='Cargando.'
            jugar='Comenzar juego--> 1'
            tutorial='Tutorial--> 2'
            creditos='Créditos--> 3'
            salir='Salir--> -1'
            dificultad='Dificultad:\nFácil-->1\nMedia-->2\nDifícil-->3'
            menu='Menú'
            guardar='Guardar la partida-->4'
            cargar='Cargar partida-->5'
            seleccionpartida='Elige una partida:'
            guardado='Partida '
            no_valido='¡ Debes comenzar un juego para guardarlo !'
            nopart='No hay ninguna partida guardada en este archivo'
            car='Cargado'
            guar='Guardado'
            bye='Gracias por jugar.\n¡ Adiós !'
        #Inglés
        if idioma=='2':
            selecidio=1
            print('Welcome')
            coordenada1x='Coordinate 1 in x: '
            coordenada1y='Coordinate 1 in y: '
            numero='Number: '
            coordenada='Coordinate: '
            cinválida='\nInvalid input, try again'
            denuevo='Try again'
            felicidades='Congratulations, you won'
            load3='Loading...'
            load2='Loading..'
            load1='Loading.'
            jugar='Start game--> 1'
            tutorial='Tutorial--> 2'
            creditos='Credits--> 3'
            salir='Quit--> -1'
            dificultad='Difficulty:\nEasy-->1\nMedium-->2\nHard-->3'
            menu='Menu'
            guardar='Save game-->4'
            cargar='Load game-->5'
            seleccionpartida='Choose a save:'
            guardado='Save '
            no_valido='You have to start a game to save it !'
            nopart='There\'s no saved game in this file'
            car='Loaded'
            guar='Saved'
            bye='Thanks for playing.\nBye bye !'

        #Francés
        if idioma=='3':
            selecidio=1
            print('Bienvenue')
            coordenada1x='Coordonnée 1 x: '
            coordenada1y='Coordonnée 1 y: '
            numero='Nombre: '
            coordenada='Coordonnée: '
            cinválida='\nEntrée invalide, éssayez a nouveau'
            denuevo='Éssayez à nouveau'
            felicidades='Felicitations, vous avez gangé'
            load3='Chargement...'
            load2='Chargement..'
            load1='Chargement.'
            jugar='Commencer Jeu--> 1'
            tutorial='Tutoriel--> 2'
            creditos='Credites--> 3'
            salir='Quitter--> -1'
            dificultad='Difficulté:\nFacile-->1\nMoyenne-->2\nDifficile-->3'
            menu='Menu'
            guardar='Garder la partie-->4'
            cargar='Charger une partie-->5'
            seleccionpartida='Chosisez une partie:'
            guardado='Partie '
            no_valido='Il faut commencer un jeu pour garder !'
            nopart='Il n\'y a un jeu gradée dans ce fichier'
            car='Chargé'
            guar='Gardée'
            bye='Merci d\'avoir joué. \nAu revoir !'
#menu

print(load1)
time.sleep(.5)
print(load2)
time.sleep(.5)
print(load3)
time.sleep(.5)
seleccion=0

tablero=[]
while seleccion!=-1:
    #selecciones extra 777 y 628, pero no están impresas en el menú
    time.sleep(.7)
    print()
    print('Sudoku')
    print()
    print(menu)
    print(jugar)
    print(tutorial)
    print(creditos)
    print(guardar)
    print(cargar)
    print(salir)
    seleccion=input()
    selecionposible=['1','2','3','-1','4','5','628','777','314']
    #comprobar que se mete una opcion posible, y si no es el caso, evitar que crashee
    time.sleep(.3)
    if seleccion in selecionposible:
        seleccion=int(seleccion)
        #tutorial
        if seleccion==2:
            tutorialf(idioma)
        #créditos
        elif seleccion==3:
            creditosf(idioma)
        #salida
        elif seleccion==-1:
            print(bye)
        #juego
        elif seleccion==1:
            print()
            if tablero==[]:
                dificulty=dificultadf(dificultad)
                tablero=crear_tablero4(dificulty)
                originales=coordenadainicial(tablero)
            time.sleep(.3)
            imprimir(tablero)
            tiro(tablero, originales,coordenada1x, coordenada1y,coordenada,cinválida,denuevo,numero,felicidades)
            time.sleep(.5)
            
           
            
        #guardar
        elif seleccion==4:
            if tablero!=[]:
                guardarf(tablero,seleccionpartida,guardado,originales,guar)
            else:
                print()
                print(no_valido)
        #cargar código
        elif seleccion==5:
            partie=pedir_partida(seleccionpartida,guardado)
            tablero=cargarf(partie,nopart)
            time.sleep(.9)
            originales=cargarori(partie,car)
        #probar función de ganar
        elif seleccion==628:
            tablero=matriz_codigo(felicidades)
            
            tablero=[]
        #se usa el código que genera una función completamente aleatoria, puede tardar mucho tiempo
        elif seleccion==777:
            tablero=intento(dificultad)
            originales=coordenadainicial(tablero)
        #genera matriz con solo 3 número faltantes a completar
        elif seleccion==314:
            matriz_codigo2(felicidades,coordenada1x, coordenada1y,coordenada,cinválida,denuevo,numero)