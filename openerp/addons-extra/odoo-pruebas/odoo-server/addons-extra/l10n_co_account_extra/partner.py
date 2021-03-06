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

class res_partner(osv.Model):
    _inherit = 'res.partner'
    _columns = {
       'comercial_name': fields.char('Nombre comercial', size=128, required=False, select=True),
    }
    _sql_constraints = [('vat_uniq', 'unique(vat, company_id)', 'La identificacion debe ser unica. El numero ingresado ya existe'),
                        ('name_uniq', 'unique(name, company_id)', 'El nombre debe ser unico. El nombre o razon social ingresado ya existe')
                       ]
    