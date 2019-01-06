# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import models, fields, api
import requests
import base64

_logger = logging.getLogger(__name__)

class ProductSupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'
    

    sida_product_url = fields.Html(
                                    string = "Vendor Product Code",
                                    compute = '_create_url',
                                    store = False,
                                    compute_sudo = False
                                    )
    @api.depends('name','product_code')
    def _create_url(self):
        if self.name.website != False and self.name.website != "":
            self.sida_product_url = '<a href="' + self.name.website + self.product_code + '" target="_blank">' + self.product_code + '</a>'
        else:
            self.sida_product_url = self.product_code
        _logger.debug('Computed url %s'%self.sida_product_url)

   
