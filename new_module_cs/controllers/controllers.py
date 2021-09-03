# -*- coding: utf-8 -*-
# from odoo import http


# class NewModuleCs(http.Controller):
#     @http.route('/new_module_cs/new_module_cs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_module_cs/new_module_cs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_module_cs.listing', {
#             'root': '/new_module_cs/new_module_cs',
#             'objects': http.request.env['new_module_cs.new_module_cs'].search([]),
#         })

#     @http.route('/new_module_cs/new_module_cs/objects/<model("new_module_cs.new_module_cs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_module_cs.object', {
#             'object': obj
#         })
