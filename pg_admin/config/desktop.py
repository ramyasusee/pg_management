# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Madras-Inn PG Management",
			"color": "#03B5AA",
			"icon": "fa fa-building",
			"type": "module",
			"label": _("Madras-Inn PG Management")
		},
		{
			"module_name": "Rooms",
			"_doctype": "Rooms",
			"color": "#F79F79",
			"icon": "fa fa-building-o",
			"type": "link",
			"link": "List/Rooms/List",
		},
		{
			"module_name": "House",
			"_doctype": "House",
			"color": "#274C77",
			"icon": "fa fa-building-o",
			"type": "link",
			"link": "List/House/List",
		},
		{
			"module_name": "Fee Plan",
			"_doctype": "Fee Plan",
			"color": "#BED558",
			"icon": "fa fa-ticket",
			"type": "link",
			"link": "List/Fee Plan/List",
		},
		{
			"module_name": "Inmate",
			"_doctype": "Inmate",
			"color": "#F28F3B",
			"icon": "fa fa-users",
			"type": "link",
			"link": "List/Inmate/List",
		},
		{
			"module_name": "Cot",
			"_doctype": "Cot",
			"color": "#A1CDF4",
			"icon": "fa fa-bed",
			"type": "link",
			"link": "List/Cot/List",
		},
		{
			"module_name": "Fee",
			"_doctype": "Fee",
			"color": "#40798C",
			"icon": "fa fa-money",
			"type": "link",
			"link": "List/Fee/List",
		},
	]
