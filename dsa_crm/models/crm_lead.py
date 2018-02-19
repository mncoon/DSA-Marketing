# -*- encoding: utf-8 -*-

from odoo import api, models

class CrmLead(models.Model):
    _inherit = "crm.lead"

    @api.multi
    def handle_partner_assignation(self,  action='create', partner_id=False):
        res = super(CrmLead, self).handle_partner_assignation()
        for lead in self:
            if action == 'create':
                partner = lead._create_lead_partner()
                partner.ref = 'CRM_' + str(lead.id)
        return res
