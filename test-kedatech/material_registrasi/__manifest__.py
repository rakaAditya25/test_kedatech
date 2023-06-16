
{
    'name': 'Material Registrasi',
    'version': '1.0',
    'category': 'Inventory',
    'sequence': 35,
    'summary': '',
     'description': """
        This module will help you to manage material process in Lokon.
    """,
    'author': 'rakaaditya2527@gmail.com',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_regis.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}