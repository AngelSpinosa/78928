from flask import Flask, render_template
from modelos import Producto

class Producto:
    def _init_(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio