# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Sida Image URL Product',
    'version': '12.0.1.0.0',
    'summary': 'This module allows to add product images using an url.',
    'author': 'Jonas Amstutz',
    'license': 'AGPL-3',
    'category': 'Purchase',
    'depends': ['purchase'],
    'data': [
        'views/sida_urlimg_product_view.xml'
    ],
    'auto_install': False,
    'installable': True,
}
