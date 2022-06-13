from odoo import models, fields

class bienes(models.Model):
    _name = 'bienes.raices'
    _description = 'CRM para Bienes Raices'

    titulo = fields.Char(string='Titulo', required=True)
    descripcion  = fields.Text(string='Descripcion', required=True)
    codigo_postal  = fields.Char(string='Codigo postal')
    precio = fields.Monetary(string='Precio')
    imagen = fields.Binary(string='Foto de la propiedad')
    categoria_id = fields.Many2one(string='Categoria', comodel_name='categoria.bienes', ondelete='restrict')
    fecha_disponibilidad  = fields.Date(string='Fecha de disponibilidad')
    dormitorios  = fields.Integer(string='Dormitorios')
    sala  = fields.Integer(string='Sala de estar')
    fachadas  = fields.Integer(string='Fachadas')
    garaje  = fields.Boolean(string='Garaje')
    jardin  = fields.Boolean(string='Jardin')
    jardin_area  = fields.Integer(string='Areas del jardin')
    jardin_orientacion  = fields.Selection(string='Orientacion del jardin', selection=[
        ('Norte', 'Norte'),
        ('Sur', 'Sur'),        
        ('Este', 'Este'),
        ('Oeste', 'Oeste')
        ])
    

class categoria(models.Model):
    _name = 'categoria.bienes'

    name  = fields.Char(string='Nombre de la categoria')