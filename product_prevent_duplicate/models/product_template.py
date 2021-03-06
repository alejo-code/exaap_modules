# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def create(self, vals):
        if self.default_code:
            existing_product = self.env['product.template'].search([
                '|', ('id', '!=', self.id),
                ('default_code', '=', self.default_code)
            ])
            if existing_product:
                raise UserError(_("It is not allowed to duplicate products"))
        return super(ProductTemplate, self).create(vals)
