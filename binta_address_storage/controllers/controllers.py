# -*- coding: utf-8 -*-
# from odoo import http


# class BintaAddressStorage(http.Controller):
#     @http.route('/binta_address_storage/binta_address_storage', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/binta_address_storage/binta_address_storage/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('binta_address_storage.listing', {
#             'root': '/binta_address_storage/binta_address_storage',
#             'objects': http.request.env['binta_address_storage.binta_address_storage'].search([]),
#         })

#     @http.route('/binta_address_storage/binta_address_storage/objects/<model("binta_address_storage.binta_address_storage"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('binta_address_storage.object', {
#             'object': obj
#         })
