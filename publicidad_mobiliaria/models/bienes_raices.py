from odoo import models 

class bienes_raices(models.Model):
    _name = 'bienes_raices'
    _description = 'CRM bienes raices'

    name = fields.Char(string='Nombre', required=True)