# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class binta_address_storage(models.Model):
#     _name = 'binta_address_storage.binta_address_storage'
#     _description = 'binta_address_storage.binta_address_storage'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
