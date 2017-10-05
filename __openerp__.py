# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Product Style Concepts Manager',
    'version': '9.0.0.1.0',
    'category': 'Product',
    'summary': 'Product Style Concepts Manager',
    'author': 'Humanytek',
    'website': "http://www.humanytek.com",
    'license': 'AGPL-3',
    'depends': ['product'],
    'data': [
        'views/product_style_concept_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False
}