# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def create(self, vals):
        config_id = self.env['ecoservice.partner.auto.account.company'].search([('company_id', '=', self.env.user.company_id.id)])
        res = super(AccountInvoice, self).create(vals)
        receiveable = False
        payable = False
        if config_id.create_auto_account_on == 'invoices':
            if vals.get('partner_id'):
                partner = self.env['res.partner'].browse(vals['partner_id'])
                if partner.parent_id:
                    partner = partner.parent_id
                if partner.customer and vals.get('type') in ['out_invoice', 'out_refund']:
                    partner_default_id = str(partner['property_account_receivable_id'].id)
                    default_property_id = self.env['ir.property'].search(['&', (
                        'name', '=', 'property_account_receivable_id'), ('res_id', '=', None)])
                    if default_property_id:
                        property_id = str(default_property_id['value_reference'].split(',')[1])
                        if property_id == partner_default_id:
                            ctx = dict(self._context)
                            ctx['type'] = 'receivable'
                            receiveable, payable = self.env['res.partner'].create_accounts(vals['partner_id'], ctx)
                            if receiveable:
                                res['account_id'] = receiveable
                if partner.supplier and res['type'] in ['in_invoice', 'in_refund']:
                    partner_default_id = str(partner['property_account_payable_id'].id)
                    default_property_id = self.env['ir.property'].search(['&', (
                        'name', '=', 'property_account_payable_id'), ('res_id', '=', None)])
                    if default_property_id:
                        property_id = str(default_property_id['value_reference'].split(',')[1])
                        if property_id == partner_default_id:
                            ctx = dict(self._context)
                            ctx['type'] = 'payable'
                            receiveable, payable = self.env['res.partner'].create_accounts(vals['partner_id'], ctx)
                            if payable:
                                res['account_id'] = payable
        return res