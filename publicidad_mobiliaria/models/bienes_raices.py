from odoo import models 

class inmobiliario(models.Model):
    _name = 'inmobiliario'
    _description = 'CRM bienes raices'

    titulo = fields.Char(string='Titulo')