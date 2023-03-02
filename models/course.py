# -*- coding: utf-8 -*-

from odoo import models, fields, api

class se_course(models.Model):
    _name = 'se.course'
    _description = 'Course'

    name = fields.Char('Course Name', required=True)
    code = fields.Char('Code')
    