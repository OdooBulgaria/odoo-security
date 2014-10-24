# -*- coding: utf-8 -*-
##############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2014-Today Trey, Kilobytes de Soluciones <www.trey.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.tests import common
from openerp.exceptions import AccessError
from openerp.osv.orm import except_orm


class test_security_rules(common.TransactionCase):

    def setUp(self):
        super(test_security_rules, self).setUp()

        cr, uid = self.cr, self.uid
        User = self.registry('res.users')

        self.utid = User.create(cr, uid, {
            'name': 'test',
            'login': 'test@test.com',
            'password': 'test',
        })

        groups_ids = [
            'group_partner_customer_created', 'group_partner_customer_created',
            'group_partner_customer_salesman_rule', 'group_product_procurement'
        ]
        self.groups = {}
        for group_id in groups_ids:
            ids = self.registry('ir.model.data').get_object_reference(
                cr, uid, 'security_extend', group_id)
            self.groups[group_id] = ids and ids[1] or False

        Partner = self.registry('res.partner')
        partner_id = Partner.create(cr, self.utid, {
            'name': 'Usuario creado para las pruebas',
            'email': 'test@localhost',
            'is_company': True,
        }, context=None)


    def test_partner(self):
        cr, uid, utid = self.cr, self.uid, self.utid

        # partner_id = Partner.create(cr, uid, {
        #     'name': 'Usuario creado para las pruebas'
        # })

        # with self.assertRaises(AccessError):
        #     partner_id = Partner.create(cr, utid, {
        #         'name': 'Usuario creado para las pruebas'
        #     })


