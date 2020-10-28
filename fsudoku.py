import time
import random
import csv
import os.path
#imprimir tutorial dependiendo del idioma
def tutorialf(idioma):
    idioma=str(idioma)
    if idioma=='1':
        print('Instrucciones\nTu objetivo es que en cada columna, fila y zona solo esté una vez cada número del 1 al 9')
        siguiente=input('Presiona enter para continuar')
        print('Se te pedirá que ingreses la coordenada en x y luego en y, después que selecciones el número que deseas poner, si deseas cambiar un número que ya hayas puesto, selecciona sus cordenadas y cuando se te pida el número, pon un espacio en blanco \' \'. Cuando quieras dejar de tirar, en coordenada en x pon -1')
        siguiente=input('Presiona enter para continuar')
    elif idioma=='2':
        print('Instructions\nThe objective is to achive that in every column, row and zone there\'s only one time each number between 1 to 9')
        siguiente=input('Press enter to continue')
        print('You\'ll be asked to input the coordinates in x and y, then you\'ll have to select the number you want to input, if you wish to change a number that you have already selected, select the coordinates and put a blank espace \' \' when the number is asked. When you want to stop inputing,just type -1 in corrdinate x')
        siguiente=input('Press enter to continue')
    elif idioma=='3':
        print('Instructions\nL\'objective c\'est que chaque colonne, range et zone ont seulment une fois chauqe nombre entre le 1 et le 9')
        siguiente=input('Pressez enter pour continuer')
        print('On vous va demander de mettre les coordonnées x et y, après vous devez mettre le nombre que vous voulez mettre, si vous voulez changer un nombre que vous avez déjà selectioné, mettez les coordonnées et quand on te demande le nombre, mettez un space\' \'. Quand vous voulez arrêter de tirer, seulement mettez -1 en coordonnée x')
        siguiente=input('Pressez enter pour continuer')
        
#imprime creditos dependiendo del idioma
def creditosf(idioma):
    idioma=str(idioma)
    if idioma=='1':
        hecho=('Hecho por: ')
    elif idioma=='2':
        hecho=('Made by: ')
    elif idioma=='3':
        hecho=('Fait par: ')
        
    print(hecho)
    print('Diego Reyna Reyes & Diógenes Grajales Corona')
    time.sleep(2)
    
#seleccion de cada una de las dificultades
def dificultadf(dificultad):
    n=0
    while n==0:
        print(dificultad)
        selecdificultad=input()
        posibles=['1','2','3']    
        if selecdificultad in posibles:
            n=1
            return selecdificultad
#imprime la matriz
def imprimir(tablero):
    print('    ',end='')
    c=0
    for i in range(9):
        print(i,end=' ')
    print()
    print()
    for linea in tablero:
        print(c,end='')
        print('  ',end='')
        c+=1
        print('|',end='')
        for dato in linea:
            if dato==10:
                print(' ',end='|')
            else:
                print(dato,end='|')
        print()
#genera una matriz en la que cada uno de sus elementos es una columna en vez de una fila para comprobar que no se repita en cada una de las columnas
def columnas(tablero):
    tablero_columna=[]
    for i in range (9):
        columna=[]
        for j in range(9):
            columna.append(tablero[j][i])
        tablero_columna.append(columna)
        
    return tablero_columna
#guarda tablero y originales
def guardarf(tablero,seleccionpartida,guardado,originales,guar):
    n=0
    while n==0:
        print(seleccionpartida)
        for j in range (1,4):
            print(guardado,end='')
            print(j)
        print(guardado,end=':')
        partie=input()
        posibles=['1','2','3']
        print()
        #seleccionar una de las 3 partidas
        if partie in posibles:
            n=1
            if partie=='1':
                f=open('partida1.csv','w')
                for renglon in tablero:
                    for dato in renglon:
                        f.write('%d' % dato)
                        f.write(',')
                    f.write('\n')
                f.close()
                p=open('originales1.csv','w')
                for datos in originales:
                    p.write('%d' %datos)
                    p.write(',')
                p.close()
                print(guar)
            elif partie=='2':
                f=open('partida2.csv','w')
                for renglon in tablero:
                    for dato in renglon:
                        f.write('%d' % dato)
                        f.write(',')
                    f.write('\n')
                f.close()
                p=open('originales2.csv','w')
                for datos in originales:
                    p.write('%d' %datos)
                    p.write(',')
                p.close()
                print(guar)
            elif partie=='3':
                f=open('partida3.csv','w')
                for renglon in tablero:
                    for dato in renglon:
                        f.write('%d' % dato)
                        f.write(',')
                    f.write('\n')
                f.close()
                p=open('originales3.csv','w')
                for datos in originales:
                    p.write('%d' %datos)
                    p.write(',')
                p.close()
                print(guar)
#carga el tablero
def cargarf(partie,nopart):
    matriz = []
    posibles=['1','2','3']
    print()
            #seleccionar una de las 3 partidas
    if partie in posibles:
        n=1
        if partie=='1':
            try:
                f = open('partida1.csv')
                f.close()
            except FileNotFoundError:
                partie='10'
                print(nopart)
        elif partie=='2':
            try:
                f = open('partida2.csv')
                f.close()
            except FileNotFoundError:
                partie='10'
                print(nopart)
        elif partie=='3':
            try:
                f = open('partida3.csv')
                f.close()
            except FileNotFoundError:
                partie='10'
                print(nopart)
        if partie=='1':
            with open('partida1.csv') as archivo:
                lector=csv.reader(archivo,delimiter=',')
                for  renglon in lector:
                    lista=[]
                    for dato in renglon[0:len(renglon)-1]:
                        lista.append(int(dato))
                    matriz.append(lista)
        elif partie=='2':
            with open('partida2.csv') as archivo:
                lector=csv.reader(archivo,delimiter=',')
                for  renglon in lector:
                     lista=[]
                     for dato in renglon[0:len(renglon)-1]:
                         lista.append(int(dato))
                     matriz.append(lista)
        elif partie=='3':
             with open('partida3.csv') as archivo:
                lector=csv.reader(archivo,delimiter=',')
                for  renglon in lector:
                     lista=[]
                     for dato in renglon[0:len(renglon)-1]:
                         lista.append(int(dato))
                     matriz.append(lista)
    return matriz


#genera una lista con las coordenadas de los números puestos al dar el tablero
def coordenadainicial(tablero):
    originales=[]
    for i in range(9):
        for c in range(9):
            coordenada=tablero[c][i]
            if coordenada!=10:
                tau=str(i)+str(c)

                originales.append(int(tau))
                
    return originales
#pide la partida a cargar
def pedir_partida(seleccionpartida,guardado):
    n=0
    while n==0:
        print(seleccionpartida)
        for j in range (1,4):
            print(guardado,end='')
            print(j)
        print(guardado,end=':')
        partie=input()
        posibles=['1','2','3']
            #seleccionar una de las 3 partidas
        if partie in posibles:
            n=1
    return partie
#carga el archivo de las coordenadas de los números originales del tablero   
def cargarori(partie,car):
    matriz = []
    posibles=['1','2','3']
            #seleccionar una de las 3 partidas
    if partie in posibles:
        n=1
        if partie=='1':
            try:
                f = open('partida1.csv')
                f.close()
            except FileNotFoundError:
                partie='10'
                
        elif partie=='2':
            try:
                f = open('partida2.csv')
                f.close()
            except FileNotFoundError:
                partie='10'
                
        elif partie=='3':
            try:
                f = open('partida3.csv')
                f.close()
            except FileNotFoundError:
                partie='10'
                
        if partie=='1':
            with open('originales1.csv') as archivo:
                lector=csv.reader(archivo,delimiter=',')
                for  renglon in lector:
                    lista=[]
                    for dato in renglon[0:len(renglon)-1]:
                        matriz.append(int(dato))
            print(car)    
        elif partie=='2':
            with open('originales2.csv') as archivo:
                lector=csv.reader(archivo,delimiter=',')
                for  renglon in lector:
                    lista=[]
                    for dato in renglon[0:len(renglon)-1]:
                        matriz.append(int(dato))
            print(car)
        elif partie=='3':
            with open('originales3.csv') as archivo:
                lector=csv.reader(archivo,delimiter=',')
                for  renglon in lector:
                    lista=[]
                    for dato in renglon[0:len(renglon)-1]:
                        matriz.append(int(dato))
            print(car)     
        return matriz
#evalua si las coordenadas puestas no es una de las casillas originales del tablero
def evaluar_coordenada(x,y,originales):
    coordenada=str(x)+str(y)
    coordenada=int(coordenada)
    if coordenada not in originales:
        return 1
    elif coordenada in originales:
        return 0
 #función de tiro que pide coordenadas y el número a poner, es un ciclo hasta que coordenada en x es -1
def tiro(tablero, originales,coordenada1x, coordenada1y,coordenada,cinvalida,denuevo,numero,felicidades):
    x=0
    while x!='-1':
        print(coordenada1x,end=' ')
        x=str(input())
        if x!='-1':
            print(coordenada1y,end=' ')
            y=str(input())


            posibles=['1','2','3','4','5','6','7','8','0']
            if x in posibles and y in posibles:
                print(coordenada, end =' ')
                coordinate=str(x)+str(y)
                print(str(x)+','+str(y))
                x=int(x)
                y=int(y)
                valido=evaluar_coordenada(x,y,originales)
                posibles_num=['1','2','3','4','5','6','7','8','9',' ','']
                if valido==1:
                    print(numero,end=' ')
                    number=input()
                    if number in posibles_num:
                        if number==' 'or number=='':
                            number=10
                        else:
                            number=int(number)
                        tablero[y][x]=number
                    else:
                        print(cinvalida)
                    
                elif valido==0:
                    print(cinvalida)
            else:
                print(cinvalida)
            print()
            imprimir(tablero)
            print()
            win=ganar(tablero,felicidades)
            if win ==1:
                tablero=[]
                break
    return tablero
#a partir de la matriz en líneas, y coordenadas, genera la zona 3x3 correspondiente a esas coordenadas
def zonas(tablero,x,y):
    zona=[]
    if x in range(0,3):
        zx=0
    elif x in range(3,6):
        zx=3
    elif x in range (6,9):
        zx=6
    if y in range(0,3):
        zy=0
    elif y in range(3,6):
        zy=3
    elif y in range (6,9):
        zy=6
    for i in range (zy,(zy+3)):
        for j in range(zx,(zx+3)):
            zona.append(tablero[i][j])
    
    return zona
#verifica columnas, lineas y zonas y determina si se gana o no
def ganar(tablero,felicidades):
    fila=tablero
    columna=columnas(tablero)
    zona=[]
    fil=0
    col=0
    zon=0
    total=0
    
    for tau in range(0,9,3):
        for pi in range(0,9,3):
            zona.append(zonas(tablero,pi,tau))
    for w in range(0,9):
        fil=0
        for c in range(1,10):
            if c in fila[w]:
                fil+=1
                
           
        if fil==9:
            total+=1
    
    for w in range(0,9):
        
        col=0
        for c in range(1,10):
            if c in columna[w]:
                col+=1
                
        if col==9:
            total+=1
    
    for w in range(0,9):
        
        zon=0
        for c in range(1,10):
            if c in zona[w]:
                zon+=1
                
        if zon==9:
            total+=1
    
    if total==27:
        print(felicidades)
        return 1
    else:
        return 0
 #genera una matriz predfinida para comprobar la función de ganar       

def matriz_codigo(felicidades):
    tablero=[[8,1,2,7,5,3,6,4,9],[9,4,3,6,8,2,1,7,5],[6,7,5,4,9,1,2,8,3],[1,5,4,2,3,7,8,9,6],[3,6,9,8,4,5,7,2,1],[2,8,7,1,6,9,5,3,4],[5,2,1,9,7,4,3,6,8],[4,3,8,5,2,6,9,1,7],[7,9,6,3,1,8,4,5,2]]
    imprimir(tablero)           
    ganar(tablero,felicidades)

def matriz_codigo2(felicidades,coordenada1x, coordenada1y,coordenada,cinvalida,denuevo,numero):
    tablero=[[8,1,2,7,5,3,6,4,9],[9,4,3,6,8,2,1,7,5],[6,7,5,4,9,1,2,8,3],[1,5,4,2,3,7,8,9,6],[3,6,9,8,4,5,7,2,1],[2,8,7,1,6,9,5,3,4],[5,2,1,9,7,4,3,6,8],[4,3,8,5,2,6,9,1,7],[7,9,6,3,1,8,4,5,2]]
    tablero[0][0]=10
    tablero[1][0]=10
    tablero[8][8]=10
    imprimir(tablero)
    print('Meta los datos faltantes')
    print()
    print('0,0=8\n0,1=9\n8,8=2')
    originales=coordenadainicial(tablero)
    tiro(tablero, originales,coordenada1x, coordenada1y,coordenada,cinvalida,denuevo,numero,felicidades)
    
 #crea el tablero basado en patrones de tableros   
def crear_tablero4(difficulty):
    numero=[1,2,3,4,5,6,7,8,9]
    tablero=[]
    opcione=[]
    opcion1=[['a','b','c','d','e','f','g','h','i'],['d','e','f','g','h','i','a','b','c'],['g','h','i','a','b','c','d','e','f'],['b','c','a','e','f','d','h','i','g'],['e','f','d','h','i','g','b','c','a'],['h','i','g','b','c','a','e','f','d'],['c','a','b','f','d','e','i','g','h'],['f','d','e','i','g','h','c','a','b'],['i','g','h','c','a','b','f','d','e']]
    opcion2=[['a','b','c','h','i','f','g','e','d'],['d','e','f','g','a','c','b','h','i'],['g','h','i','e','d','b','c','a','f'],['b','i','e','c','f','h','a','d','g'],['f','g','d','a','e','i','h','c','b'],['c','a','h','b','g','d','i','f','e'],['i','c','b','d','h','e','f','g','a'],['e','f','a','i','c','g','d','b','h'],['h','d','g','f','b','a','e','i','c']]
    opcion3=[['a','d','c','h','e','i','f','g','b'],['b','e','f','g','a','c','d','h','i'],['g','i','h','b','f','d','a','e','c'],['e','c','b','f','i','g','h','a','d'],['h','f','d','a','b','e','c','i','g'],['i','a','g','d','c','h','b','f','e'],['f','h','i','c','g','b','e','d','a'],['c','g','a','e','d','f','i','b','h'],['d','b','e','i','h','a','g','c','f']]
    opcion4=[['b','a','e','i','c','h','d','f','g'],['g','h','f','a','b','d','c','e','i'],['i','c','d','f','e','g','b','h','a'],['h','f','i','e','d','b','a','g','c'],['a','d','c','g','h','f','e','i','b'],['e','b','g','c','i','a','h','d','f'],['f','g','b','d','a','e','i','c','h'],['d','i','h','d','f','c','g','a','e'],['c','e','a','h','g','i','f','b','d']]
    opci=random.randint(1,4)
    if opci==1:
        opcione=opcion1
    elif opci==2:
        opcione=opcion2
    elif opci==3:
        opcione=opcion3
    elif opci==4:
        opcione=opcion4
    for p in range(7):
        random.shuffle(numero)
        
    if difficulty=='1':
        np=30
    elif difficulty=='2':
        np=24
    elif difficulty=='3':
        np=17
    for p in range(9):
        l=[]
        for x in range(1,10):
            l.append(10)
            
        tablero.append(l)
    
    for p in range(np):
        si=0
        while si==0:
            x=random.randint(0,8)
            y=random.randint(0,8)
            if tablero[y][x]==10:
                si=1
                opcion=opcione[y][x]
                if opcion=='a':
                    numi=numero[0]
                elif opcion=='b':
                    numi=numero[1]
                elif opcion=='c':
                    numi=numero[2]
                elif opcion=='d':
                    numi=numero[3]
                elif opcion=='e':
                    numi=numero[4]
                elif opcion=='f':
                    numi=numero[5]
                elif opcion=='g':
                    numi=numero[6]
                elif opcion=='h':
                    numi=numero[7]
                elif opcion=='i':
                    numi=numero[8]
                tablero[y][x]=numi
    return tablero


    #genera una matriz aleatoria con solo unos números
def matriz():
    numeros_puestos=[]
    tablero=[]
    for i in range (1):
        for j in range (1,2):
            numeros_puestos.append(j)
    for p in range (9):
        linea=[]
        for x in range(9):
            linea.append(10)
        tablero.append(linea)
    
    coordenadas_puestas=[]
    
    for i in range (len(numeros_puestos)):
        o=0
        
        while o==0:
            x=random.randint(0,8)
            y=random.randint(0,8)
            coordenada=str(x)+str(y)
            tablero_columna=columnas(tablero)
            zona=zonas(tablero,x,y)
            if coordenada not in coordenadas_puestas and numeros_puestos[i] not in tablero[y] and numeros_puestos[i] not in tablero_columna[x] and numeros_puestos[i] not in zona :
                tablero[y][x]=numeros_puestos[i]
                coordenadas_puestas.append(coordenada)
                
                o=1
    
    return tablero
#en cada espacio en blanco, prueba cada uno de los números 1-9, si no encuentra ninguno posible, llama otra función
def resolver(tablero):
    originales=coordenadainicial(tablero)
    x=0
    y=0
    puest=0
    for y in range(9):
        for x in range(9):
            evalo=evaluar_coordenada(x,y,originales)
            ctablero=columnas(tablero)
            ztablero=zonas(tablero,x,y)
            if evalo==1:
                for p in range(1,10):
                    if p not in tablero[y]:
                        if p not in ctablero[x]:
                            if p not in ztablero:
                                tablero[y][x]=p                           
                                break
                if tablero[y][x]==10:
                    tablero=reparacion(tablero,x,y,originales)
                
                            
            
                
            
    return tablero
#cuando no se encuentra un número que cumpla con las reglas, se regresa al anterior y se prueban los valores del número puesto al 9, si algún otro puede ponerse, regresa a la casilla original e inetnta de nuevo, si no, vuelve a regresar y avanzar hasta que se satisfagan las reglas
def reparacion(tablero,x,y,originales):
    nolo=1
    ctablero=columnas(tablero)
    ztablero=zonas(tablero,x,y)
    
    p=x
    n=y
    cocha=10
    while nolo==1:
        
        if cocha==10:
            
            p=p-1
            n=n
            if p==-1:
                p=8
                n=n-1
            inicial=tablero[n][p]
            if tablero[y][x]==10:
                
                obama=evaluar_coordenada(p,n,originales)
                if obama==1:
                    
                    tablero[n][p]=10
                    for data in range(inicial+1,10):
                        ctablero=columnas(tablero)
                        ztablero=zonas(tablero,p,n)
                        
                        if data not in ctablero[p]:
                            if data not in ztablero:
                                if data not in tablero[n]:
                                    tablero[n][p]=data
                                    cocha=data
                                    
                                    break
                else:
                    p=p-1
                    n=n
                    if p==-1:
                        p=8
                        n=n-1
            else:
                nolo=0
            
        elif cocha!=10:
            
            p=p+1
            n=n
            if p==9:
                p=0
                n=n+1
            
            
            if tablero[y][x]==10:
                cocha=10
                
                obama=evaluar_coordenada(p,n,originales)
                if obama==1:
                    
                    tablero[n][p]=10
                    for data in range(1,10):
                        ctablero=columnas(tablero)
                        ztablero=zonas(tablero,p,n)
                        
                        if data not in ctablero[p]:
                            if data not in ztablero:
                                if data not in tablero[n]:
                                    tablero[n][p]=data
                                    cocha=data
                                    
                                    break
                                
                                
                else:
                    p=p+1
                    n=n
                    if p==9:
                        p=0
                        n=n+1
            else:
                nolo=0
        
            
    return tablero
#genera una matriz con solo una fraccion de los numeros de la original
def borrar(tablero,dificultad):
    
    finalo=[]
    if dificultad==1:
        puestos=30
    elif dificultad==2:
        puestos=25
    else:
        puestos=17
    linea=[10,10,10,10,10,10,10,10,10]
    for p in range(9):
        l=[]
        for x in range(1,10):
            l.append(10)
            
        finalo.append(l)
    
    for p in range(puestos):
        si=0
        while si==0:
            x=random.randint(0,8)
            y=random.randint(0,8)
            if finalo[y][x]==10:
                si=1
                numi=tablero[y][x]
                finalo[y][x]=numi
    return finalo
#función de nuestro intento de generar un tablero completamente aleatorio, funciona, solo que tarda demasiado tiempo para ser viable, solo es accesible poniendo 777 en el menú            
def intento(dificultad):           
    tablero=matriz()
    final=resolver(tablero)
    dif=dificultadf(dificultad)
    pan=borrar(final,dif)
    return pan


