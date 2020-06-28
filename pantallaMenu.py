import PySimpleGUI as sg 
import pantallaJuego 
import pantallaConfig

layout = [
    [sg.Text("ScrabbleAR - Game",background_color="#71B3BD",font=("Fixedsys",40),pad=((0,0),(30,70)))],
    [sg.Button("Cómo jugar",size=(18,1),pad=((0,0),(0,20)),font=("Fixedsys",18),auto_size_button=False)],
    [sg.Button("Jugar",key="-PLAY-",size=(24,2),pad=((0,0),(0,20)),font=("Fixedsys",18),auto_size_button=False)],
    [sg.Button("Configuración",key="-CONFIG-",size=(18,1),pad=((0,0),(0,20)),font=("Fixedsys",18),auto_size_button=False)]
]
pantalla_menu = sg.Window("Menu",layout,element_justification="center",size=(725,480),background_color="#71B3BD")

def main():
    while True:
        
        event,values = pantalla_menu.read()
        if event is None:
            break

        elif event == "-PLAY-":
            pantalla_menu.Hide()
            pantallaJuego.main()
            pantalla_menu.UnHide()

        elif event == "-CONFIG-":
            pantalla_menu.Hide()
            pantallaConfig.main()
            pantalla_menu.UnHide()

    pantalla_menu.close()

if __name__ == "__main__":
    main()
