def hacer_ventana():
    """Devuelve una ventana que pregunta si desea guardar la partida al salir del juego
    """
    import PySimpleGUI as sg

    import os
    if os.access(r'Data\Images\Juego\Avatar-CPU.png',0):
        layout = [
            [sg.Image(r"Data\Images\Juego\Ventana-salir\titulo.png",background_color="#40B7C9",pad=((200,0),(100,50)))],
            [sg.Button(image_filename=r"Data\Images\Juego\Ventana-salir\boton-guardar-y-salir.png",key="-GUARDAR_Y_SALIR2-",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=((370,0),(0,15)))],
            [sg.Button(image_filename=r"Data\Images\Juego\Ventana-salir\boton-salir-sin-guardar.png",key="-SALIR_SIN_GUARDAR2-",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=((370,0),(0,0)))]
        ]
    else:
        layout = [
            [sg.Image(r"Data/Images/Juego/Ventana-salir/titulo.png",background_color="#40B7C9",pad=((200,0),(100,50)))],
            [sg.Button(image_filename=r"Data/Images/Juego/Ventana-salir/boton-guardar-y-salir.png",key="-GUARDAR_Y_SALIR2-",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=((370,0),(0,15)))],
            [sg.Button(image_filename=r"Data/Images/Juego/Ventana-salir/boton-salir-sin-guardar.png",key="-SALIR_SIN_GUARDAR2-",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=((370,0),(0,0)))]
        ]

    window = sg.Window("ScrabbleAR - Salir",size=(1000,600),background_color="#40B7C9",disable_close=True,margins=(0,0)).Layout(layout)

    return window
