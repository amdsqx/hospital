# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Hospital Management System""",

    'description': """
        
    """,

    'author': "Ahmad Sauqi",
    'website': "https://www.ahmadsauqi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'version': '0.1',
    'sequence' : -100,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    # untuk import data file modul xml
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
    'auto_intstall' : False,
}
