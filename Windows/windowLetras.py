def hacer_ventana(diccionario,categoria,clave):
    """Devuelve una ventana que puede ser utilizada para:
    -Seleccionar el puntaje que vale cada letra
    -Seleccionar la cantidad de fichas por letra
    """
    import PySimpleGUI as sg

    if categoria == "Puntos":
        categoria = "Puntaje"
    else:
        categoria = "Fichas"

    lis_values=[1,2,3,4,5,6,7,8,9,10,11]

    import os
    if os.access(r'Data\Images\Juego\Avatar-CPU.png',0):
        imagen_titulo = sg.Image(r"Data\Images\Configuracion\Letras\titulo-"+categoria+".png",background_color='#40B7C9',pad=((90,0),(10,10)))
        boton_confirmar = sg.Button(image_filename=r"Data\Images\Configuracion\Letras\boton-confirmar.png",key="-CONFIRMAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((80,0),(30,0)))
        boton_cancelar = sg.Button(image_filename=r"Data\Images\Configuracion\Letras\boton-cancelar.png",key="-CANCELAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((10,0),(30,0)))
    else:
        imagen_titulo = sg.Image(r"Data/Images/Configuracion/Letras/titulo-"+categoria+".png",background_color='#40B7C9',pad=((90,0),(10,10)))
        boton_confirmar = sg.Button(image_filename=r"Data/Images/Configuracion/Letras/boton-confirmar.png",key="-CONFIRMAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((80,0),(30,0)))
        boton_cancelar = sg.Button(image_filename=r"Data/Images/Configuracion/Letras/boton-cancelar.png",key="-CANCELAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((10,0),(30,0)))


    layout=[
        [imagen_titulo],
        [sg.Text('A',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='A',default_values=[diccionario['A'][clave]]), sg.Text('B',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='B',default_values=[diccionario['B'][clave]]), sg.Text('C',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='C',default_values=[diccionario['C'][clave]]), sg.Text('D',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='D',default_values=[diccionario['D'][clave]]), sg.Text('E',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='E',default_values=[diccionario['E'][clave]]), sg.Text('F',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='F',default_values=[diccionario['F'][clave]]), sg.Text('G',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='G',default_values=[diccionario['G'][clave]])],
        [sg.Text('H',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='H',default_values=[diccionario['H'][clave]]), sg.Text('I',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='I',default_values=[diccionario['I'][clave]]), sg.Text('J',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='J',default_values=[diccionario['J'][clave]]), sg.Text('K',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='K',default_values=[diccionario['K'][clave]]), sg.Text('L',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='L',default_values=[diccionario['L'][clave]]), sg.Text('M',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='M',default_values=[diccionario['M'][clave]]), sg.Text('N',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='N',default_values=[diccionario['N'][clave]])],
        [sg.Text('Ñ',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='Ñ',default_values=[diccionario['Ñ'][clave]]), sg.Text('O',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='O',default_values=[diccionario['O'][clave]]), sg.Text('P',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='P',default_values=[diccionario['P'][clave]]), sg.Text('Q',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='Q',default_values=[diccionario['Q'][clave]]), sg.Text('R',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='R',default_values=[diccionario['R'][clave]]), sg.Text('S',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='S',default_values=[diccionario['S'][clave]]), sg.Text('T',size=(1,1),background_color='#40B7C9',font=("Arial black",10),text_color="black"),sg.Listbox(lis_values,key='T',default_values=[diccionario['T'][clave]])],
        [sg.Text('U',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='U',default_values=[diccionario['U'][clave]]), sg.Text('V',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='V',default_values=[diccionario['V'][clave]]), sg.Text('W',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='W',default_values=[diccionario['W'][clave]]), sg.Text('X',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='X',default_values=[diccionario['X'][clave]]), sg.Text('Y',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='Y',default_values=[diccionario['Y'][clave]]), sg.Text('Z',size=(2,1),background_color='#40B7C9',font=("Arial black",12),text_color="black"),sg.Listbox(lis_values,key='Z',default_values=[diccionario['Z'][clave]])],
        [boton_confirmar,boton_cancelar]
    ]

    window = sg.Window("ScrabbleAR - "+categoria,size=(500,400),background_color='#40B7C9').Layout(layout)

    return window
