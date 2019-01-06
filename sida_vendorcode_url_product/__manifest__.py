# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Sida Vendor Code URL Product',
    'version': '12.0.1.0.0',
    'summary': 'This module turns the product vendor reference code into an external link to the product..',
    'author': 'Jonas Amstutz',
    'license': 'AGPL-3',
    'category': 'Purchase',
    'depends': ['purchase'],
    'data': [
        'views/sida_vendorcode_url_product_view.xml'
    ],
    'auto_install': False,
    'installable': True,
}
