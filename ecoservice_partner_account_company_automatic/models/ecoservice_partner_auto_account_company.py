# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models, fields


class ecoservice_partner_auto_account_company(models.Model):
    _inherit = 'ecoservice.partner.auto.account.company'

    create_auto_account_on = fields.Selection([('partners', 'Partners'), ('orders', 'Orders'), ('invoices', 'Invoices')])