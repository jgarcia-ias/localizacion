##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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

class product_product(osv.Model):
    _inherit = 'product.product'
    
    _defaults = {
        'valuation' : 'real_time'         
    }
    _sql_constraints = [
        ('_reference_uniq', 'unique (default_code)', 'La referencia interna debe ser unica !')
    ]


class product_template(osv.Model):
    _inherit = 'product.template'
    
    _defaults = {
        'cost_method': 'average',
        'type' : 'product',
    }

