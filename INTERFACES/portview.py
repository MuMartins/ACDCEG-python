#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color, Port
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.media.ev3dev import Font

import SYSTEM.battery as battery
import SYSTEM.buttons as buttons

'''
Arquivo responsável por mostrar o valor lido em cada uma das conexões do brick
'''

# Definição do brick como ev3
ev3 = EV3Brick()

# Definição das portas do brick
light_sensor_01 = ColorSensor(Port.S1)
light_sensor_02 = ColorSensor(Port.S2)
light_sensor_03 = ColorSensor(Port.S3)

medium_A_motor = Motor(Port.A)
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)
medium_D_motor = Motor(Port.D)


ports_coordinates = [
    # Lista com os valores de X1, Y1, X2, Y2 de cada uma das conexões do brick
    [148, 40, 176, 52],  # Port.S1
    [148, 57, 176, 69],  # Port.S2
    [148, 74, 176, 86],  # Port.S3
    [66, 40, 94, 52],   # Port.A
    [66, 57, 94, 69],   # Port.B
    [66, 74, 94, 86],   # Port.C
    [66, 91, 94, 103]   # Port.D
]

# Variáveis
last_sensor_value = 1
last_motor_value = 1


def sensor_reflection(sensor_value=0, sensor_coordinate):
    '''Função responsável por mostrar a leitura dos sensores na tela do brick'''
    global last_sensor_value
    # Define o tamanho da fonte do texto que será mostrado na tela do brick
    portview_font = Font(size=13)
    ev3.screen.set_font(portview_font)

    # Condição responsável por atualizar o texto mostrando a leitura dos sensores na tela do brick
    if sensor_value != last_sensor_value:
        ev3.screen.draw_box(
            *ports_coordinates[sensor_coordinate], fill=True, color=Color.WHITE)
        ev3.screen.draw_text(
            ports_coordinates[sensor_coordinate][0], ports_coordinates[sensor_coordinate][1], sensor_value)
        last_sensor_value = sensor_value


def motor_angle(motor_value=0, motor_coordinate):
    '''Função responsável por mostrar a leitura dos motores na tela do brick'''
    global last_motor_value
    # Define o tamanho da fonte do texto que será mostrado na tela do brick
    portview_font = Font(size=13)
    ev3.screen.set_font(portview_font)

    # Condição responsável por atualizar o texto mostrando a leitura dos motores na tela do brick
    if motor_value != last_motor_value:
        ev3.screen.draw_box(
            *ports_coordinates[motor_coordinate], fill=True, color=Color.WHITE)
        ev3.screen.draw_text(
            ports_coordinates[motor_coordinate][0], ports_coordinates[motor_coordinate][1], motor_value)
        last_motor_value = motor_value


def start():
    '''Inicia e gerencia a tela do portview'''
    ev3.screen.clear()
    ev3.screen.load_image('./IMAGES/display_portview.png')
    while not buttons.pressed(Button.DOWN):
        # Mostra o valor atual da bateria
        battery.voltage_text()

        # Sensores
        '''Inicia a leitura dos valores dos sensores'''
        sensor_value_01 = light_sensor_01.reflection()
        sensor_reflection(sensor_value_01, 0)

        sensor_value_02 = light_sensor_02.reflection()
        sensor_reflection(sensor_value_02, 1)

        sensor_value_03 = light_sensor_03.reflection()
        sensor_reflection(sensor_value_03, 2)

        # Motores
        '''Inicia a leitura dos valores dos motores'''
        motor_value_01 = medium_A_motor.angle()
        motor_angle(motor_value_01, 3)

        motor_value_02 = left_motor.angle()
        motor_angle(motor_value_02, 4)

        motor_value_03 = right_motor.angle()
        motor_angle(motor_value_03, 5)

        motor_value_04 = medium_D_motor.angle()
        motor_angle(motor_value_04, 6)

    # Reseta a tela do brick para voltar para o menu principal
    ev3.screen.clear()
