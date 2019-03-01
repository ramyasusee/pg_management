from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, msgprint
from pg_admin.madras_inn_pg_management.doctype.sms_center.sms_center import send_sms
from pg_admin.madras_inn_pg_management.api import get_fee_components

def every_minute():
	pg = frappe.get_all("PG Datas", fields=["name1", "fee_plan"])
	for d in pg:
		sch = frappe.new_doc("Fee")
		sch.data_1 = d['name1']
		sch.fee_structure = d['fee_plan']
		fs = frappe.get_list("Fee Component", fields=["fee_category", "amount"] , filters={"parent": sch.fee_structure}, order_by= "idx")
		for s in fs:
			row = sch.append('components', {})
			row.fee_category = s.fee_category
			row.amount = s.amount
		sch.save()