#See LICENSE file for full copyright and licensing details.


from odoo import models, api


class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        config_id = self.env['ecoservice.partner.auto.account.company'].search([('company_id', '=', self.env.user.company_id.id)])
        res = super(sale_order, self).create(vals)
        if config_id.create_auto_account_on == 'orders':
            if vals.get('partner_id'):
                partner = self.env['res.partner'].browse(vals['partner_id'])
                if partner.parent_id:
                    partner = partner.parent_id
                if partner:
                    partner_default_id = str(partner['property_account_receivable_id'].id)
                    default_property_id = self.env['ir.property'].search(['&', (
                        'name', '=', 'property_account_receivable_id'), ('res_id', '=', None)])
                    if default_property_id:
                        property_id = str(default_property_id['value_reference'].split(',')[1])
                        if property_id == partner_default_id:
                            ctx = dict(self._context)
                            ctx['type'] = 'receivable'
                            self.env['res.partner'].create_accounts(vals['partner_id'], ctx)
        return res

