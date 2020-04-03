# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import today
from pg_admin.madras_inn_pg_management.doctype.inmate.inmate import send_welcome_sms 

class Fee(Document):
	def on_update_after_submit(self):
		frappe.errprint(self)


@frappe.whitelist()
def send_sms(mob_no,due,amt):	
	message = "Hi {}, Thanks for your payment of Rs. {} towards your PG rent on {}. Your due is Rs. {}, kindly settle the dues at the earliest. \n Thanks".format(mob_no,amt,today(),due)
	send_welcome_sms(mob_no,message)

@frappe.whitelist()
def update(doc,method):
		frappe.errprint(doc)
