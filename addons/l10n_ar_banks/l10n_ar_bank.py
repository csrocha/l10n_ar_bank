# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2014 Otra localización argentina de Odoo.
# http://odoo-l10n-ar.github.io/
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

from openerp.osv import fields,osv
from openerp.tools.translate import _
import time

class Bank(osv.osv):
    _inherit = 'res.bank'
    _columns = {
		  'update' : fields.date(_('Update')),
		  'vat': fields.char(_('VAT'),size=32 ,help="Value Added Tax number."),
		}
    _defaults = {
		  'update': lambda *a: time.strftime('%Y-%m-%d')
		}
Bank()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
