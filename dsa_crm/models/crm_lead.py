# -*- encoding: utf-8 -*-

from odoo import api, models

class CrmLead(models.Model):
    _inherit = "crm.lead"

    @api.multi
    def handle_partner_assignation(self,  action='create', partner_id=False):
        res = super(CrmLead, self).handle_partner_assignation()
        for lead, partner in res.items():
            if action == 'create':
                partner = self.env['res.partner'].browse(partner)
                partner.ref = 'CRM_' + str(lead)
        return res 