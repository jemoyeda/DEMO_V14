from odoo import models, fields

class bienes(models.Model):
    _name = 'bienes.raices'

    titulo = fields.Char(string='Titulo')