# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 CT Moldeo Interactive Ltda
#    (<http://business.moldeo.coop>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

{
    'name': "Modulo que agrega extras a la operacion de finanzas de NH",
    'version': '0.1',
    'category': 'Accounting & Finance',
    'author': 'Moldeo Interactive',
    'website': 'http://business.moldeo.coop',
    'license': 'AGPL-3',
    "depends" : ['account_check'],
    "data" : [
        'check_view.xml',
	'voucher_view.xml',
	'invoice_view.xml'
        ],
    'test' : [
    ],
    "demo" : [],
    "active": False,
    "installable": True
}
