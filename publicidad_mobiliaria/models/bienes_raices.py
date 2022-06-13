from odoo import models, fields

class bienes(models.Model):
    _name = 'bienes.raices'
    _description = 'CRM para Bienes Raices'

    titulo = fields.Char(string='Titulo', required=True)
    descripcion  = fields.Text(string='Descripcion', required=True)
    codigo_postal  = fields.Char(string='Codigo postal')
    precio  = fields.Float(string='Precio', required=True)
    imagen  = fields.Binary(string='Foto de la propiedad')
    categoria_id = fields.Many2one(string='Categoria', comodel_name='categoria.bienes', ondelete='restrict')
    

class categoria(models.Model):
    _name = 'categoria.bienes'

    name  = fields.Char(string='Nombre de la categoria')
    