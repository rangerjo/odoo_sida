# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class BoMTemplate(models.Model):
    _inherit = 'mrp.bom'

    sida_vendors = fields.Many2many('res.partner', string='Vendors to display')

    @api.multi
    def get_data(self,bom_id):
        _logger.debug("bom_id = %s"%bom_id)
        
        # get list of vendors to display
        desired_vendors = self.env['mrp.bom'].search([('id', '=', bom_id)])[0].sida_vendors
        _logger.debug("desired_vendors = %s"%desired_vendors)

        # list holding lists of strings with cell data
        records = []
        # make header row
        header = ['Name','Hersteller','Herstellernummer']
        for desired_vendor in desired_vendors:
            header.append(desired_vendor.name)
        header.append('Menge')
        records.append(header)

        # loop through all components
        components = self.env['mrp.bom.line'].search([('bom_id', '=', bom_id)])
        for component in components:
            record = []
            _logger.debug("Aggregating data for component id(%s) and name(%s)"%(component.product_id.id,component.product_id.name))
            record.append(component.product_id.name)
            record.append(component.product_id.manufacturer.name)
            record.append(component.product_id.manufacturer_pref)
            vendors = self.env['product.supplierinfo'].search([('product_tmpl_id','=',component.product_id.product_tmpl_id.id)])
            _logger.debug("vendors = %s"%vendors)
            # for all desired vendors to be listed
            for desired_vendor in desired_vendors:
                # check if vendor belongs to the ones to be displayed
                found = False
                for vendor in vendors:
                    _logger.debug("is desired_vendor(%s) == vendor(%s)"%(desired_vendor.id,vendor.name.id))
                    if vendor.name.id == desired_vendor.id:
                        record.append(vendor.product_code)
                        found = True
                if not found:
                    record.append("")

            record.append(str(component.product_qty))
            records.append(record)
        return records

