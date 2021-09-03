# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Student(models.Model):
    _name="student.profile"
    _description = "Students"

    name = fields.Char(string="Nombre")
    school_id = fields.Many2one("school.profile")
    hobby_list = fields.Many2many("hobby.profile", "school_hobby_rel", "student_id", "hobby_id", string="Hobbies")

    is_virtual_school = fields.Boolean(related="school_id.is_virtual_class",
                                       string="Is Virtual Class", store=True)

    email_school = fields.Char(related="school_id.email", string="School's email", store=True)

    currency_id = fields.Many2one("res.currency", string="Currency")
    students_fees = fields.Monetary(string="Student Fees")
    total_fees = fields.Float(string="Total Fees")
    active = fields.Boolean(string="Active", default=True)


    def custom_button_method(self):
        print("This is a custom_button_method called for you", self)

    @api.model
    def create(self, values):
        rtn = super(Student, self).create(values)
        if not rtn.hobby_list:
            raise UserError(_("Please select at least hobby"))
        print("Values: ", values)
        print("Self: ", self)
        print("Rtn: ", rtn)
        return rtn

    def write(self, values):
        print("Values: ", values)
        print("Self: ", self)
        rtn = super(Student, self).write(values)
        print("Rtn: ", rtn)
        return rtn




    '''
    def unlink(self):
        print("Self statement", self)
        for rc in self:
            if rc.total_fees > 200:
                raise UserError(_("Dont delete this student!"))
        rtn = super(Student, self).unlink()
        print("Return statement", rtn)
        return rtn
        
    def copy(self, default = {}):
        print("Default: ", default)
        print("Self: ", self)
        rtn = super(Student, self).copy(default=default)
        print("Rtn: ", rtn)
        return rtn

     @api.model
    def create(self, values):
        print("Valores de metodos creados", values)
        print("Self", self)
        rtn = super(Student, self).create(values)
        print("Return statement", rtn)
        return rtn

        def write(self, vals):
        rtn = super(Student, self).write(vals)
        if not self.hobby_list:
            raise UserError(_("Please dont erase tag"))
    '''



class SchoolProfile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many(comodel_name="student.profile",
                                  inverse_name="school_id",
                                  string="School List",
                                  limit=3)

    '''
    @api.model
    def create(self, vals):
        rtn = super(SchoolProfile, self).create(vals)
        if not rtn.school_list:
            raise UserError(_("Student list is empty!"))
        return rtn
    '''



class Hobbies(models.Model):
    _name = "hobby.profile"

    name = fields.Char("Hobby")

