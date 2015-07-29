# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Interconsulting S.A e Innovatecsa SAS.
#    (<http://www.interconsulting.com.co).
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
{
    "name": "Legalizaciones y anticipos",
    "version": "1.0",
    "description": """
This module add new fields needed in hr_expenses in order to handle the process of employee advances of mony and legalizatios of them

    """,
    "author": "Interconsulting S.A. e Innovatecsa SAS.",
    "website": "http://www.interconsulting.com.co",
    "category": "Financial",
    "depends": [
		    "hr",
		    "hr_expense",
		    "hr_contract",
		    "hr_payroll",
		    "account",
		    "account_voucher",
		    "hr_payroll_co",
		    "base",
			],
	"data":[
		    "legalizaciones_y_anticipos_view.xml",
			],
    "demo_xml": [
			],
    "active": False,
    "installable": True,
    "certificate" : "",
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
