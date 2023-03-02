# -*- coding: utf-8 -*-
{
    'name': "se.course.registration",

    'summary': """
        smart edu course registration module""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Daffodil Software Ltd",
    'website': "http://www.dsl.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'demo/demo.xml',
        # 'security/ir.model.access.csv',
        'views/course_view.xml',
        'views/registration_view.xml',
        'views/section_view.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/menu.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
