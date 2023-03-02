# -*- coding: utf-8 -*-

from odoo import models, fields, api

class se_course_registration(models.Model):
    _name = 'se.course.registration'
    _description = 'Registration'

    section_id = fields.Many2one('se.section', 'Section')
    course_id = fields.Many2one('se.course', 'Course')
    teacher_id = fields.Many2one('se.teacher', 'Teacher', )
    student_ids = fields.Many2many('se.student', 'registration_student_rel', 'registration_id', 'student_id', 'Student List')
