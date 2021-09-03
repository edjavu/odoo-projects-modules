# -*- coding: utf-8 -*-

from odoo import models, fields

class ToDo(models.Model):
    _name = "todo.app" #nombre de la base de datos: todo_app
    _description = "Lista de Tareas"

    name = fields.Char(string="Nombre")
    state = fields.Char(string="Estado")


 