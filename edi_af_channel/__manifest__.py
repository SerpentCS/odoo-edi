# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2016 Vertel AB (<http://vertel.se>).
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
    'name': 'Depreciated EDI AF Channel',
    'version': '0.1',
    'category': 'edi',
    'summary': """
        Return channel through which jobseekers sign on. \n
        Example: \n
        PDM, LOKAL, SJALVSERVICE
        """,
    'description': """
Depreciated
===============================================================================
The functioinality of this module was replaced by edi_af_aisf_rask. \n 
""",
    'licence': 'AGPL-3',
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['partner_view_360', 'edi_route_ipf', 'af_data_ais-f_loader'],
    'external_dependencies': {
    },
    'data': [
        'data/edi_route_data.xml',
        'views/edi_af_channel_views.xml',
    ],
    'application': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4s:softtabstop=4:shiftwidth=4:
