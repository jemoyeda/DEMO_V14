from odoo import models, fields

class bienes(models.Model):
    _name = 'bienes.raices'
    _description = 'CRM para Bienes Raices'

    titulo = fields.Char(string='Titulo')