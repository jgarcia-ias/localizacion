# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 I.A.S. INGENIERÍA, APLICACIONES Y SOFTWARE Johan Alejandro Olano (<http:http://www.ias.com.co).
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
    "name": "Colombia - Chart Account and Taxes by I.A.S. INGENIERÍA, APLICACIONES Y SOFTWARE",
    "version": "1.0",
    "description": """
Colombian accounting chart and tax localization.

Plan contable colombiano e impuestos de acuerdo a disposiciones vigentes
Collaborators:
   - Johan Alejandro Olano <jolano@ias.com.co>

    """,
    "author": "I.A.S. Ingenieria, Aplicaciones y Software",
    "website": "http://www.ias.com.co",
    "category": "Localization/Account Charts",
    "depends": [
			"account_chart",
			],
	"data":[
        "account_tax_code.xml",
        "l10n_co_chart.xml",
        "account_tax.xml",
        "l10n_co_wizard.xml",
			],
    "demo_xml": [
			],
    "update_xml": [
			],
    "active": False,
    "installable": True,
    "certificate" : "",
    'images': ['images/config_chart_l10n_co.jpeg','images/l10n_co_chart.jpeg'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
