# -*- encoding: utf-8 -*-

from odoo import api, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        Lead = self.env['crm.lead']
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.options:
                for option in order.options:
                    lead = Lead.create({
                        'type': "lead",
                        'name': option.product_id.name,
                        'partner_id': order.partner_id.id,
                        'description': option.name,
                        'team_id': order.team_id.id,
                        'user_id': order.user_id.id,
                        'order_ids': [(4, order.id, 0)]
                    })
                    lead.convert_opportunity(order.partner_id.id)
        return res
