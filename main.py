#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.tools import wait

from main_def import *

# Definição do brick como ev3
ev3 = EV3Brick()

# Código principal
menu_selecionador = [
    # A ordem é X1, Y1, X2, Y2, Preenchimento, Cor
    [3, 14, 85, 62, 1, False, Color.BLACK],     # MENU
    [90, 14, 172, 62, 1, False, Color.BLACK],   # CALIBRACAO
    [3, 65, 85, 113, 1, False, Color.BLACK],    # PROBLEMAS
    [90, 65, 172, 113, 1, False, Color.BLACK]   # PORT_VIEW
]

# Variáveis
menu_selecionador_single = 0
menu_selecionador_single_last = 3

round_selecionador = 0

# Função menu
def set_menu_selecionador():
    global menu_selecionador, menu_selecionador_single_last
    if menu_selecionador_single != menu_selecionador_single_last:
        ev3.screen.load_image('./IMG_MENU/display.png')
        ev3.screen.draw_box(*menu_selecionador[menu_selecionador_single])
        menu_selecionador_single_last = menu_selecionador_single

# Code
while True:
    set_menu_selecionador()

    # Interface selecionador
    if button_pressed(Button.DOWN):
        while not button_released(Button.DOWN):
            wait(10)
        menu_selecionador_single = (menu_selecionador_single + 2) % 4
    
    elif button_pressed(Button.UP):
        while not button_released(Button.UP):
            wait(10)
        menu_selecionador_single = (menu_selecionador_single - 2) % 4
    
    elif button_pressed(Button.RIGHT):
        while not button_released(Button.RIGHT):
            wait(10)
        menu_selecionador_single = (menu_selecionador_single + 1) % 4
    
    elif button_pressed(Button.LEFT):
        while not button_released(Button.LEFT):
            wait(10)
        menu_selecionador_single = (menu_selecionador_single - 1) % 4
    
    # Interface função
    elif button_pressed(Button.CENTER):
        if menu_selecionador_single == 0:
            while True:
                if button_pressed(Button.RIGHT):
                    while not button_released(Button.RIGHT):
                        wait(10)
                    round_selecionador = (round_selecionador + 1) % 4
                
                elif button_pressed(Button.LEFT):
                    while not button_released(Button.LEFT):
                        wait(10)
                    round_selecionador = (round_selecionador - 1) % 4
                
                if round_selecionador == 0:
                    ev3.screen.load_image('./IMG_ROUNDS/round_01')
                
                if round_selecionador == 1:
                    ev3.screen.load_image('./IMG_ROUNDS/round_02')

                if round_selecionador == 2:
                    ev3.screen.load_image('./IMG_ROUNDS/round_03')

                if round_selecionador == 3:
                    ev3.screen.load_image('./IMG_ROUNDS/round_04')

                if button_pressed(Button.CENTER):
                    if round_selecionador == 0:
                        ev3.screen.clear()
                        while True:
                            if button_pressed(Button.DOWN):
                                break
                            else:
                                ev3.screen.draw_circle(70, 90, 20, fill=True)

                    if round_selecionador == 1:
                        ev3.screen.clear()
                        while True:
                            if button_pressed(Button.DOWN):
                                break
                            else:
                                ev3.screen.draw_line(30,30,30,100)

                    if round_selecionador == 2:
                        ev3.screen.clear()
                        while True:
                            if button_pressed(Button.DOWN):
                                break
                            else:
                                ev3.screen.draw_line(30,30,30,100)
                    
                    if round_selecionador == 3:
                        ev3.screen.clear()
                        while True:
                            if button_pressed(Button.DOWN):
                                break
                            else:
                                ev3.screen.draw_box(50,30,90,60)

        elif menu_selecionador_single == 1:
            ev3.screen.clear()
            while True:
                if button_pressed(Button.DOWN):
                    break
                else:
                    ev3.screen.draw_circle(70, 90, 20, fill=True)
        
        elif menu_selecionador_single == 2:
            ev3.screen.clear()
            while True:
                if button_pressed(Button.DOWN):
                    break
                else:
                    ev3.screen.draw_line(30,30,30,100)
        
        elif menu_selecionador_single == 3:
            ev3.screen.clear()
            while True:
                if button_pressed(Button.DOWN):
                    break
                else:
                    ev3.screen.draw_box(50,30,90,60)