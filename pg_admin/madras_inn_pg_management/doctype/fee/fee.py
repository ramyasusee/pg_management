# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Fee(Document):
	def validate(self):
		# if(self.date_of_invoice == frappe.datetime.month_start()):
		# 	self.temp = "true"
		# else:
		# 	self.temp = "false"
		pass
