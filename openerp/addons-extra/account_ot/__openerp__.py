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
    "name": "Account OT ",
    "version": "1.0",
    "description": """
This module add a relation betwin purchase order and account invoice with the mpr_repair module OT. 

    """,
    "author": "Interconsulting S.A. e Innovatecsa SAS.",
    "website": "http://www.interconsulting.com.co",
    "category": "Financial",
    "depends": [
            "base",
		    "account",
            "hr_expense",
            "mrp_repair",
            "purchase",
            "sale",
			],
	"data":[
		    "account_ot_view.xml",
			],
    "demo_xml": [
			],
    "active": False,
    "installable": True,
    "certificate" : "",
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
