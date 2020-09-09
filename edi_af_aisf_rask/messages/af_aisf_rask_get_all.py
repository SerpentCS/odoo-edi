# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2020 Vertel AB (<http://vertel.se>).
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
from odoo import models, api, _
import ast
import json

import logging

_logger = logging.getLogger(__name__)

LOCAL_TZ = 'Europe/Stockholm'

class edi_message(models.Model):
    _inherit = 'edi.message'

    @api.one
    def unpack(self):
        if self.edi_type.id == self.env.ref('edi_af_aisf_rask.rask_get_all').id:
            # _logger.warn("unpack self.body: %s" % self.body.decode("utf-8"))
            # decode string and convert string to tuple, convert tuple to dict
            body = json.loads(self.body)
            customer_id = body.get('arbetssokande').get('sokandeId')
            res_partner_obj = self.env['res.partner'].search([('customer_id', '=', customer_id)])
            _logger.info(
                "edi_af_aisf_rask.edit_message.unpack() has been called, customer_id: %s" % res_partner_obj.customer_id)

    @api.one
    def pack(self):
        if self.edi_type.id == self.env.ref('edi_af_aisf_rask.rask_get_all').id:
            obj = self.model_record
            _logger.info("edi_af_aisf_rask.edit_message.pack() has been called, customer_id: %s" % obj.customer_id)

            self.body = self.edi_type.type_mapping.format(
                path="ais-f-arbetssokande/v1/arbetssokande/{customer_id}/anpassad?resurser=alla".format(
                    customer_id=obj.customer_id)
            )
            envelope = self.env['edi.envelope'].create({
                'name': 'RASK all information request',
                'route_id': self.route_id.id,
                'route_type': self.route_type,
                'edi_message_ids': [(6, 0, [self.id])]
            })
        else:
            super(edi_message, self).pack()
