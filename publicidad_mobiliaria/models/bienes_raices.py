from odoo import models, fields

class bienes(models.Model):
    _name = 'bienes'

    titulo = fields.Char(string='Titulo')