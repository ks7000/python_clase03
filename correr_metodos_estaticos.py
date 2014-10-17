# -*- coding:utf-8 -*-
import click
from metodos_estaticos import MiClase

@click.command()
@click.option( '--mensaje', default=' el ejemplo en sí de metodos estaticos', prompt='Introduzca un mensaje diferente', help='Permite cambiar el mensaje por defecto a mostrar')
def correr_estatico(mensaje):
    a = MiClase()
    #a.metodo_estatico(" el ejemplo en sí de metodos estaticos")
    a.metodo_estatico(mensaje)
    
if __name__ == '__main__':
    correr_estatico()
