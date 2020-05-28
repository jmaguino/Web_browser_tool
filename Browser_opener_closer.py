#This program is used to open the mostly used websites on my daily rutine.
#For this program to work, we need to import the modules webbrowser, time, and keyboard.
#We need to use a for count.
#I have already set my default brwoser to be Google Chrome before using this program.

#Este programa es usado para abrir los sitios web mas usados en mi rutina diaria.
#Para que este programa funcione, necesitamos importar los modulos webbrowser (buscador web,
#time (tiempo), and keyboard (Teclado).
#Ya he establecido por defecto Google Chrome como mi buscador antes the usar este programa.

import webbrowser
import time
import keyboard

urls = ['https://www.google.com', 'https://stackoverflow.com', 'https://weather.com',
        'https://www.youtube.com']

for url in urls:
    webbrowser.open_new(url)
    keyboard.press_and_release(['Ctrl','W'])
    

