# -*- encoding: utf-8 -*-

from odoo import api, fields, models

class Lead2OpportunityPartner(models.TransientModel):

    _name = 'crm.apply.person.channel'
    _description = 'CRM Apply Sale person and Channel'

    user_id = fields.Many2one('res.users', 'Salesperson', index=True)
    team_id = fields.Many2one('crm.team', 'Sales Channel', oldname='section_id', index=True)

    @api.multi
    def action_apply(self):
        active_leads = self.env['crm.lead'].browse(self.env.context['active_ids'])
        for lead in active_leads:
        	if self.user_id:
        		lead.user_id = self.user_id.id
        	if self.team_id:
        		lead.team_id = self.team_id.id
