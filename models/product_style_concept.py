# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models


class ProductStyleConcept(models.Model):
    _name = 'product.style.concept'

    name = fields.Char('Concept', required=True)
    description = fields.Text('Description', translate=True)
    product_ids = fields.One2many(
        'product.template',
        'product_style_concept_id',
        string='Concepts Products',
    )
    products_count = fields.Integer(
        string='Number of products',
        compute='_get_products_count',
    )

    @api.one
    @api.depends('product_ids')
    def _get_products_count(self):
        self.products_count = len(self.product_ids)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_style_concept_id = fields.Many2one(
        'product.style.concept',
        string='Style Concept',
        help='Select a concept for this product'
    )
