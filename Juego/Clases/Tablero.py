import PySimpleGUI as sg 
import random
from Juego.Clases.Casilla import Casilla

class Tablero:
    """ Esta clase crea un objeto Tablero que es una matriz de objetos "Casilla".\n
    Parámetros:\n
    tamaño: es la dimensión de la matriz (TxT).\n
    casillas_especiales: es un diccionario que contiene las keys de las casillas que son "especiales".\n
    inicio: es una tupla que contiene la key de la casilla de inicio del juego y una letra para esa casilla (key,letra).\n
    """
    def __init__(self, tamaño, casilas_especiales=None, inicio=(None,None)):
        self._tamaño = tamaño  
        self._casillas_especiales = casilas_especiales 
        self._inicio = inicio 
        self._casillas = [] # matriz que contiene todos los objetos "casilla" del tablero
        self._palabra = [inicio[0]] # letras de la palabra a formar
        self._layout = self._armar() # layout para PySimpleGUI
    
    def getLayout(self):
        return self._layout

    def _armar(self):
        """Este método arma una lista para la interfaz gráfica que contiene una matriz de objetos "Casilla"\n
        y guarda los objetos casilla en la propiedad _casillas.
        """
        layout = [] 
        for i in range(1, self._tamaño + 1):
            fila_layout = []
            fila_casillas = []
            for j in range(1, self._tamaño + 1):
                especial = False
                key = str(i)+"-"+str(j)
                #Para crear una casilla "especial":
                for clave in self._casillas_especiales:
                    if(key in self._casillas_especiales[clave][0]):
                        casilla = Casilla((3,1), key, deshabilitada=True, ocupada=False, especial=(True,clave,('black',self._casillas_especiales[clave][1])))
                        especial = True
                #Para crear una casilla normal o la casilla de inicio:        
                if not especial:
                    if key == self._inicio[0]:
                        casilla = Casilla((3,1), clave=self._inicio[0], contenido=self._inicio[1], color=('white','#684225'), deshabilitada=True, ocupada=True) #casilla de inicio
                    else:
                        casilla = Casilla((3,1), key, deshabilitada=True, ocupada=False) #casilla normal
                fila_casillas.append(casilla)
                fila_layout.append(casilla.getLayout())
            self._casillas.append(fila_casillas)     
            layout.append(fila_layout)

        return layout

    def click(self, event):
        """Este método retorna True si el evento fue en una de las casillas del tablero, False en caso contrario
        """
        for fila in self._casillas:
            for casilla in fila:
                if event == casilla.getKey():
                    return True
        return False        

    def habilitar(self, pantalla):
        """Este método habilita todas las casillas del tablero que esten desocupadas.
        """
        for fila in self._casillas:
            for casilla in fila:
                if casilla.estaOcupada():
                    continue
                else:
                    casilla.habilitar()
                    pantalla[casilla.getKey()].update(disabled=False)

    def deshabilitar(self, pantalla):
        """Este método deshabilita todas las casillas del tablero que esten desocupadas.
        """
        for fila in self._casillas:
            for casilla in fila:
                if casilla.estaOcupada():
                    continue
                else:
                    casilla.deshabilitar()
                    pantalla[casilla.getKey()].update(disabled=True)
    
    def insertarFicha(self,key,pantalla,valor):
        """Este método coloca una ficha en el tablero
        """
        self._palabra.append(key)
        aux = key.split("-")
        self._casillas[int(aux[0])-1][int(aux[1])-1].ocupar()
        self._casillas[int(aux[0])-1][int(aux[1])-1].deshabilitar()
        self._casillas[int(aux[0])-1][int(aux[1])-1].setContenido(valor)
        self._casillas[int(aux[0])-1][int(aux[1])-1].setColor(('white','#684225'))
        pantalla[key].update(valor, button_color=('white','#684225'), disabled_button_color=('white','#684225'), disabled=True)

    def reiniciarPalabra(self):
        self._palabra=[]

    def _reiniciarPalabraInicio(self):
        if (self._inicio[0] in self._palabra):
            self._palabra=[self._inicio[0]]
        else:
            self._palabra=[]

    def devolverFichas(self,pantalla_juego):
        lis_letras = []
        for key in self._palabra:
            if (key!=self._inicio[0]):
                aux = key.split('-')
                self._casillas[int(aux[0])-1][int(aux[1])-1].desocupar()
                lis_letras.append(pantalla_juego[key].GetText())
                especial = False
                for clave in self._casillas_especiales:
                    if key in self._casillas_especiales[clave][0]:
                        pantalla_juego[key].Update(clave, button_color=('black',self._casillas_especiales[clave][1]),disabled_button_color=('black',self._casillas_especiales[clave][1]))
                        especial = True
                if not especial:
                    pantalla_juego[key].Update('', button_color=('black','white'),disabled_button_color=('black','white'))
        self._reiniciarPalabraInicio()
        return lis_letras

    def getPalabra(self):
        lis_aux=[]
        for x in self._palabra:
            elems=x.split('-')
            for i in range(0,2):
                elems[i]=int(elems[i])
            lis_aux.append(elems)
        a_comparar=lis_aux[0][0]
        horizontal=True
        vertical=True
        for e in lis_aux:
            if(e[0]!=a_comparar):
                horizontal=False
        if (horizontal==False):
            a_comparar=lis_aux[0][1]
            
            for e in lis_aux:
                if(e[1]!=a_comparar):
                    vertical=False
            if (vertical==True):
                lis_ord=sorted(lis_aux, key=lambda valor: valor[0])
        else:
            lis_ord=sorted(lis_aux, key=lambda valor: valor[1])
        if (horizontal==True)or(vertical==True):
            pal=''
            for key in lis_ord:
                pal+= self._casillas[key[0]-1][key[1]-1].getContenido()
            return pal
        else:
            return 'xxxxxx'

def crearTablero(bolsa_fichas):
    casillas_especiales1 = {
    "x2":(("2-6","2-10","6-2","6-14","7-7","7-9","9-7","9-9","10-2","10-14","14-6","14-10",), "#2283BB"),
    "x3":(("1-4","1-12","3-7","3-9","4-1","4-8","4-15","7-3","7-13","8-4","8-12","9-3","9-13","12-1","12-15","12-8","13-7","13-9","15-4","15-12"), "#45BB22"),
    "-3":(("1-1","1-8","1-15","8-1","8-15","15-1","15-8","15-15"), '#F02121'),
    "-2":(("2-2","2-14","3-3","3-13","13-3","13-13","14-2","14-14"), '#F06C21'),
    "-1":(("4-4","4-12","5-5","5-11","6-6","6-10","10-6","10-10","11-5","11-11","12-4","12-12"), '#F0B121')
    }
    casillas_especiales2 = {
        "x2":(('2-5','2-12','4-10','5-2','8-8','8-12','8-18','10-3','10-17','12-2','12-8','12-12','15-18','16-10','18-8','18-15'), "#2283BB"),
        "x3":(('1-17','3-19','7-10','13-10','17-1','19-3'), "#45BB22"),
        "-3":(('2-15','5-18','8-4','8-16','12-4','12-16','15-2','18-5'), '#F02121'),
        "-2":(('1-3','3-1','5-7','5-13','15-7','15-13','17-19','19-17'), '#F06C21'),
        "-1":(('2-8','8-2','10-7','10-13','12-18','18-12'), '#F0B121')
    }
    casillas_especiales3 = {}

    num_random = random.randint(1,3)

    if num_random == 1:
        tablero = Tablero(15,casillas_especiales1,inicio=("8-8",bolsa_fichas.letras_random(1)[0]))
    elif num_random == 2:
        tablero = Tablero(19,casillas_especiales2,inicio=("10-10",bolsa_fichas.letras_random(1)[0]))
    else:
        tablero = Tablero(20,casillas_especiales2,inicio=("10-10",bolsa_fichas.letras_random(1)[0]))#3

    pad_tablero = {
        1:{"pad-izq":126,"pad-der":146,"pad-top":70,"pad-bot":70}, # medidas para tablero 1
        2:{"pad-izq":71,"pad-der":81,"pad-top":23,"pad-bot":23}, # medidas para tablero 2
        3:{"pad-izq":61,"pad-der":61,"pad-top":10,"pad-bot":10}, # medidas para tablero 3
    }

    return [tablero,pad_tablero,num_random]