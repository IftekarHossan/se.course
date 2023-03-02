# -*- coding: utf-8 -*-

from odoo import models, fields, api

class se_teacher(models.Model):
    _name = 'se.teacher'
    _description = 'Teacher'

    name = fields.Char('Teacher Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    birth_date = fields.Date('Date of Birth')
    gender = fields.Selection([('M','Male'),('F','Female')],'Gender')