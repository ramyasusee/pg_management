# -*- coding: utf-8 -*-
# Copyright (c) 2019, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PGDatas(Document):
	def validate(self):
		cot_doc = frappe.get_doc("Cot", self.cot)
		if self.status == "Active":
			cot_doc.update({
				"cot_status": "Filled"
			})
		else:
			cot_doc.update({
				"cot_status": "Available"
			})
		cot_doc.save(ignore_permissions=True)
