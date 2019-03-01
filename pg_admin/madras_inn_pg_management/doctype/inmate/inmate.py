# -*- coding: utf-8 -*-
# Copyright (c) 2019, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, msgprint
from pg_admin.madras_inn_pg_management.doctype.sms_center.sms_center import send_sms
from pg_admin.madras_inn_pg_management.api import generateOTP

class Inmate(Document):
	def send_otp(self):
		self.generated_otp = generateOTP()
		sms_text = "Your OTP for Madras Inn Registration Form is "+self.generated_otp
		send_sms([self.mobile_number], sms_text)
	def validate(self):
		if(self.enter_the_otp == ""):
			frappe.throw("Enter the OTP to save your details")
		if(self.enter_the_otp != self.generated_otp):
			frappe.throw("The OTP you entered is not right")
	def on_update(self):
		msgprint(_('Your details have been submitted successfully.'))
		
		
	