# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Sida Vendor BoM',
    'version': '12.0.1.0.0',
    'summary': 'This module allows to generate custom BOM reports including vendor information for all components.',
    'author': 'Jonas Amstutz',
    'license': 'AGPL-3',
    'category': 'Fertigung',
    'depends': ['mrp'],
    'data': [
        'views/sida_vendorinfo_view.xml',
        'reports/sida_report_bom.xml',
    ],
    'auto_install': False,
    'installable': True,
}
