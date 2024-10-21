# -*- coding: utf-8 -*-
{
    "name": "Aden Logs",

    "version": "1.0",

    "author": "Aden Business School",

    "category": "aden",

    "license": 'AGPL-3',

    "description": """Customized logs module for Aden Business School""",

    "depends": ['base'],

    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/aden_log.xml",
    ],

    "installable": True,

    "active": False,

    'auto_install': False,

    'application': True,
}
