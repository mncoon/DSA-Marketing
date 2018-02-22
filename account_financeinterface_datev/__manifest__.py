#See LICENSE file for full copyright and licensing details.

{
    'name': 'Finanzinterface - Datev Export',
    'version': '11.0.2.0.0',
    'depends': [
        'account_financeinterface'
    ],
    'author': 'ecoservice, syscoon GmbH',
    'website': 'https://syscoon.com',
    'summary': 'Export of account moves to Datev',
    'description': """The module ecoservice_financeinterface_datev provides methods to convert account moves to the Datevformat (Datev Dok.-Nr.: 1036228).""",
    'category': 'Accounting',
    'data': [
        'views/account_view.xml',
        'data/account_cron.xml',
        'views/res_company_view.xml',
        'views/account_invoice_view.xml',
    ],
    'active': False,
    'installable': True
}
