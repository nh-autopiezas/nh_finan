# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields
from openerp.tools.translate import _
import time


class account_check(osv.osv):
	_name = 'account.check'
	_inherit = 'account.check'

	_columns = {
		'deposit_date': fields.related('deposit_account_move_id','date',type="date",string="Deposit Date"),
		}

account_check()


class account_check_hold(osv.osv_memory):
	_name = 'account.check.hold'

	def action_hold(self, cr, uid, ids, context=None):
		check_obj = self.pool.get('account.check')
		check_ids = context['active_ids']
		for check_id in check_ids:
			check_object = check_obj.browse(cr,uid,check_id)
			if check_object.state == 'draft':
		                check_object.signal_workflow('draft_router')
		        	# check_object.signal_workflow('holding_handed')
		return None
	

account_check_hold()
