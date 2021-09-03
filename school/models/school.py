
from odoo import models, fields, api

class SchoolProfile(models.Model):
    _name = "school.profile"

    name = fields.Char(string="School Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    is_virtual_class = fields.Boolean(string="Virtual Class Support?")
    school_rank = fields.Integer(string="Rank")
    result = fields.Float(string="Result",
                          digit=(2,2))
    address = fields.Text(string="Address")
    establish_date = fields.Date(string="Establish Date")
    open_date = fields.Datetime("Open Date")
    school_type = fields.Selection([('public', 'Public School'), ('private', 'Private School')],
                                   string="Type of School")
    documents = fields.Binary(string="Documents")
    document_name = fields.Char(string="File Name")
    school_image = fields.Image(string="Upload School Image", max_width=100,
                                max_height=100, verify_resolution=False)
    school_description = fields.Html(string="Description")
    auto_rank = fields.Integer(compute="_auto_rank_populate")

    @api.depends("school_type")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    @api.model
    def name_create(self, name):
        rtn = self.create({"name":name, "email":"mit@gmail.com"})
        return rtn.name_get()[0]