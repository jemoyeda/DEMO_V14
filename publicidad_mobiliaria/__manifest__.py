
# -*- coding: utf-8 -*-
#Módulo creado por Ing. Industrial Hermes Colina
{
    'name': "CRM Bienes Raices",

    'summary': """
        CRM para la gestion de clientes en el negocio de Bienes raices, para un negocio exitosos""",

    'description': """
        
        El área superior de la vista del formulario resume información importante para la propiedad, como el nombre, 
        el tipo de propiedad, el código postal, etc.  La primera pestaña contiene información que describe la propiedad: 
        habitaciones, salón, garaje, jardín…
        
        La segunda pestaña enumera las ofertas de la propiedad. Podemos ver aquí que los compradores potenciales
        pueden hacer ofertas por encima o por debajo del precio de venta esperado. 
        Depende del vendedor aceptar una oferta.
    """,

    'author': "Ing. Hermes Colina",
    'website': "https://contablesag.com",
    
    #Siempre se debe agregar los módulos de los que depende el nuevo módulo para evitar errores
    #inesperados. (Ej. TypeError, ¡tal módulo no existe!)
    'depends': ['base'],

    # Siempre cargar las vistas a utilizar en el modulo
    'data': [
        'views/bienes.xml',
        'views/propiedades.xml',
        'security/ir.model.access.csv'
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,

    'license': 'LGPL-3',
}