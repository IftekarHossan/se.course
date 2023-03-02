# -*- coding: utf-8 -*-

from odoo import models, fields, api

class se_section(models.Model):
    _name = 'se.section'
    _description = 'Section'

    name = fields.Char('Section Name', required=True)
    code = fields.Char('Code')