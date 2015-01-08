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


class res_partner(osv.osv):
	_name = 'res.partner'
	_inherit = 'res.partner'

	def _check_document_number(self, cr, uid, ids, context=None):
		for self_obj in self.browse(cr, uid, ids, context=context):
			dupplicate_ids = self.search(cr,uid,[('document_number','=',self_obj.document_number),\
				('document_type_id','=',self.document_type_id),('supplier','=',True)])
			if len(dupplicate_ids) > 1:
				return False
		return True

	_constraints = [(_check_document_number, 'CUIT duplicado', ['document_number'])]


res_partner()

