# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.


from openerp import models, api, exceptions, fields, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    hidden_menu_ids = fields.Many2many(
        comodel_name="ir.ui.menu",
        relation="ir_ui_menu_in_res_company_rel",
        column1="company_id",
        column2="menu_id",
        string="Hidden Menus"
    )
