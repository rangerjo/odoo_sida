# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import models, fields, api
import requests
import base64

_logger = logging.getLogger(__name__)

class ProductImageFetcher(models.Model):
    _inherit = 'product.template'
    

    sida_imgurl = fields.Char("Image Url")

    @api.onchange('sida_imgurl')
    def fetch_image(self):
        _logger.debug("Downloading %s"%self.sida_imgurl)
        if self.sida_imgurl != "" and self.sida_imgurl != False:
            r = requests.get(self.sida_imgurl,allow_redirects=True)
            if r.status_code == 200:
                image_base64 = base64.b64encode(r.content)
                self.image_medium = image_base64
            else:
                _logger.warning("Downloading %s failed"%self.sida_imgurl)

        

