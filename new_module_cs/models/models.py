# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alumno(models.Model):
    _name = "nm.alumno"
    _description = "Alumnos"

    name = fields.Char(string="Nombre")

    asignatura_id = fields.Many2many("nm.asignatura", "alumno_asignatura_rel", "alum_id", "asignatura_id")
    calificacion_id = fields.Many2one("nm.calificacion")


class Asignatura(models.Model):
    _name = "nm.asignatura"
    _description = "Asignaturas"

    name = fields.Char("Asignatura")

    alumno_id = fields.One2many(comodel_name="nm.alumno", inverse_name="calificacion_id")


class Calificacion(models.Model):
    _name = "nm.calificacion"
    _description = "Calificaciones"

    name = fields.Float(string="Ingrese calificacion")




