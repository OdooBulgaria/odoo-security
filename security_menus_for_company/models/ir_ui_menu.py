# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.


from openerp import models, api, exceptions, _


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.multi
    def load_menus_root(self):
        menus = super(IrUiMenu, self).load_menus_root()
        for root_menu in menus['all_menu_ids']:
            print root_menu

