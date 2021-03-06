# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountInvoiceLine(models.Model):
    _inherit = ['account.invoice.line']

    is_product_kit = fields.Boolean(
        string='Part of a Product Kit?',
        readonly=True,
        default=False)
    order_kit_line_id = fields.Many2one(
        comodel_name='sale.order.kit.line',
        string='Order Kit Line')
