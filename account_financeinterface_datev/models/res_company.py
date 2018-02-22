#See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResCompany(models.Model):
    """ Inherits the res.company class and adds methods and attributes
    .. automethod:: _finance_interface_selection
    """
    _inherit = 'res.company'

    finance_interface = fields.Selection(selection_add=[('datev', 'Datev')], string='Finance Interface')
    exportmethod = fields.Selection(selection=[('netto', 'netto'), ('brutto', 'brutto')], string='Export method')
    enable_datev_checks = fields.Boolean('Perform Datev Checks', default=True)
    enable_fixing = fields.Boolean('Enable Fixing Moves in Datev', default=False)

