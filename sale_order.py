# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp.osv import fields, osv
import pdb

class sale_order_line_stock(osv.osv):
    _name = 'sale.order.line'
    _inherit = "sale.order.line"

    def _fnct_line_stock(self, cr, uid, ids, field_name, args, context=None):
        product_obj = self.pool.get('product.product')
        if context is None:
            context = {}
        stock_available = 0
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = line.product_id.virtual_available - line.product_uom_qty
        return res

    _columns = {
        'virtual_available': fields.function(_fnct_line_stock, string='Available Stock'),
    }

sale_order_line_stock()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
