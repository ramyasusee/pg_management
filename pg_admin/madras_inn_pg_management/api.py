# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
import base64
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt
import math, random 


def ascify(str):
	import string
	return filter(lambda x: x in string.printable, str)

@frappe.whitelist(allow_guest=True)
def sms_delivary_report(number, status, customID, datetime):
	auth = frappe.get_request_header('Authorization', None)
	token = False
	if auth is not None:
		auth_type = auth.split(' ')[0]
		auth_cred = auth.split(' ')[1]
		if auth_type == "Basic":
			cred = base64.b64decode(auth_cred)
			username = cred.split(':')[0]
			password = cred.split(':')[1]
			if username == '_at_callback' and password == '3ed3583b7ca':
				token = True

	if token is True:
		if status == 'D':
			reason = 'Message was delivered successfully.';
		elif status == 'U':
			reason = 'The message was undelivered.';
		elif status == 'P':
			reason = 'Message pending, the message is en route.';
		elif status == 'I':
			reason = 'The number was invalid.';
		elif status == 'E':
			reason = 'The message has expired.';
		elif status == '?':
			reason = 'Message pushed to networks, the message is en route.';
		elif status == 'B':
			reason = 'Blocked, this number has been blocked by the DND.';
		else:
			reason = 'Unknown status code.';

		with open("/tmp/sms_delivary_report.log", "a") as logfile:
			logfile.write("Number: {}, Status: {}, CustomID: {}, Reason: {}, Datetime: {}\n".format(number, status, customID, reason, datetime))

		import datetime as dt
		log = frappe.get_list('SMS Log', {'custom_id': customID})
		if(len(log)>0):
			doc = frappe.get_doc('SMS Log', log[0].name)
			i = 0
			while i < len(doc.delivery_log):
				if ascify(doc.delivery_log[i].number) == ascify(number[2:]) and ascify(doc.delivery_log[i].status) != ascify(status):
					doc.delivery_log[i].reason = ascify(reason)
					doc.delivery_log[i].datetime = dt.datetime.strptime(datetime, '%Y-%m-%d %H:%M:%S') + dt.timedelta(hours=4, minutes=30)
					doc.delivery_log[i].status = ascify(status)
					break
				i+=1

			doc.save()
			return 'success'
		else:
			return 'failure'
	else:
		return 'error'
@frappe.whitelist()
def get_fee_components(fee_structure):
	"""Returns Fee Components.

	:param fee_structure: Fee Structure.
	"""
	if fee_structure:
		fs = frappe.get_list("Fee Component", fields=["fee_category", "amount","fee_type"] , filters={"parent": fee_structure}, order_by= "idx")
		return fs

@frappe.whitelist()
def collect_fees(fees, amt):
	fee = frappe.get_doc("Fee", fees)
	stu = frappe.get_doc("Inmate", fee.data_1)
	paid_amount = flt(amt) + flt(frappe.db.get_value("Fee", fees, "paid_amount"))
	total_amount = flt(frappe.db.get_value("Fee", fees, "total_amount"))
	frappe.db.set_value("Fee", fees, "paid_amount", paid_amount)
	frappe.db.set_value("Fee", fees, "outstanding_amount", (total_amount - paid_amount))
	#send_sms([stu.student_mobile_number], stu.title+"'s payment of INR "+str(paid_amount)+" is honoured against academic term "+fee.academic_term+". Outstanding amount is INR "+str(total_amount - paid_amount))
	return paid_amount

@frappe.whitelist()
def generateOTP(): 
    digits = "0123456789"
    OTP = "" 
    for i in range(4) : 
        OTP += str(random.randint(0,9))
    return OTP