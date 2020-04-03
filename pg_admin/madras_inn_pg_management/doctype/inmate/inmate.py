# -*- coding: utf-8 -*-
# Copyright (c) 2019, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, msgprint
# from pg_admin.madras_inn_pg_management.doctype.sms_center.sms_center import send_sms
from pg_admin.madras_inn_pg_management.api import generateOTP
import binascii
import os
import base64
import datetime
import string
from frappe.utils import cstr, nowdate

class Inmate(Document):
    def send_otp(self):
        self.generated_otp = generateOTP()
        sms_text = "Your OTP for Madras Inn Registration Form is "+self.generated_otp
        send_welcome_sms(self.mobile_number, sms_text)
    # def validate_otp(self):
    #     frappe.errprint("hoi")
        # if(self.enter_the_otp == ""):
        #     frappe.throw("Enter the OTP to save your details")
        # if(self.enter_the_otp != self.generated_otp):
        #     frappe.throw("The OTP you entered is not right")
        # elif(self.enter_the_otp == self.generated_otp):
        #     frappe.throw("OTP is verified")
    def on_update(self):
        if not self.enter_the_otp:
            frappe.throw("Enter the OTP to save your details")
        if not self.i_agree_to_the_given_terms_and_conditions:
            frappe.throw("Please Agree the Terms & Conditions")
        if self.generated_otp and self.i_agree_to_the_given_terms_and_conditions:
            msgprint(_('Your details have been submitted successfully.'))
        
        




@frappe.whitelist()
def send_welcome_sms(mob_no,message):
    receiver_list = []
    # message = """ Your RI Housing Account has been created, \n Your Username: "%s" \n Password:"richindia@1" \nYou can access this through https://partner.rihousing.in""" %mob_no
    receiver_list.append(mob_no)
    log = send_sms(receiver_list, base64.b64encode(message.encode('utf-8')),cstr(message.encode('utf-8')))
    delist = '<br>'.join(receiver_list)
    frappe.msgprint(_("SMS sent to following numbers: {0}").format("\n" + mob_no))
    # msgprint(_("Message: <br><b>"+message.replace('\n', '<br>')+"</b><br><br>Queued for sending to the following "+str(len(receiver_list))+" recipient(s):<br><br>"+delist+"<br><br> Click here to know delivery status &nbsp; <span><a class='btn btn-primary btn-sm' target='_blank' href='http://partner.rihousing.in:8000/desk#Form/SMS Log/"+log.name+"'>View "+log.name+"</a></span>"))
    return log


def ascify(str):
    import string
    return filter(lambda x: x in string.printable, str)

def validate_receiver_nos(receiver_list):
    validated_receiver_list = []
    for d in receiver_list:
        # remove invalid character
        for x in [' ', '+', '-', '(', ')']:
            d = d.replace(x, '')

        validated_receiver_list.append(d)

    if not validated_receiver_list:
        throw(_("Please enter valid mobile nos"))

    return validated_receiver_list


def get_sender_name():
    "returns name as SMS sender"
    sender_name = 'AFTUTR'
    if len(sender_name) > 6 and \
            frappe.db.get_default("country") == "India":
        throw("""As per TRAI rule, sender name must be exactly 6 characters.
            Kindly change sender name in Setup --> Global Defaults.
            Note: Hyphen, space, numeric digit, special characters are not allowed.""")
    return sender_name

@frappe.whitelist()
def get_contact_number(contact_name, value, key):
    "returns mobile number of the contact"
    number = frappe.db.sql("""select mobile_no, phone from tabContact where name=%s and %s=%s""" %
        ('%s', frappe.db.escape(key), '%s'), (contact_name, value))
    return number and (number[0][0] or number[0][1]) or ''

@frappe.whitelist()
def send_sms(receiver_list, msg, m,sender_name = '', dialog = '', justlog=''):

    import json
    if isinstance(receiver_list, str):
        receiver_list = json.loads(receiver_list)
    if not isinstance(receiver_list, list):
        receiver_list = [receiver_list]
    receiver_list = validate_receiver_nos(receiver_list)

    arg = {
        'receiver_list' : receiver_list,
        'sms_log_m' : m,
        'message'		: msg,
        'sender_name'	: sender_name or get_sender_name(),
        'show_dialog'	: dialog,
        'justlog'	: justlog
    }
    return send_via_gateway(arg)

def send_via_gateway(arg):
    customID = binascii.hexlify(os.urandom(16))
    args = {'msg': arg.get('message')}
    log_args = {'log_msg': arg.get('sms_log_m')}
    success_list = []
    for d in arg.get('receiver_list'):
        args['phone'] = d
        if not arg.get('justlog'):
            status = send_request(args, customID)
            if status >= 200 and status < 300:
                success_list.append(d)
        else:
            success_list.append(d)
    if len(success_list) > 0 and arg.get('show_dialog'):
        args.update(arg)
        
        # frappe.msgprint(_("SMS sent to following numbers: {0}").format("\n" + "\n".join(success_list)))
        return create_sms_log(args,log_args ,success_list, customID)

    elif len(success_list) > 0:
        args.update(arg)
        # frappe.msgprint(_("SMS sent to following numbers: {0}").format("\n" + "\n".join(success_list)))
        return create_sms_log(args,log_args ,success_list, customID)

def send_request(params, customID):
    nums = "".join(filter(lambda x: x in string.printable, params.get('phone')))
    msg = params.get('msg')
    message = msg.decode("utf-8")
    os.system("sendsms "+nums+" '"+message+"'")
    return 200


# Create SMS Log
# =========================================================
def create_sms_log(args, log_args,sent_to, customID):
    sl = frappe.new_doc('SMS Log')
    sl.sender_name = args['sender_name']
    sl.sent_on = nowdate()
    sl.message = log_args['log_msg']
    sl.no_of_requested_sms = len(args['receiver_list'])
    sl.no_of_sent_sms = len(sent_to)
    sl.flags.ignore_permissions = True
    sl.custom_id = customID
    for number in args['receiver_list']:
        sl.append('delivery_log', {'number': number, 'status': 'Q', 'reason': 'Messaged sent and is en route.', 'datetime': datetime.datetime.now() +datetime.timedelta(hours=5, minutes=30)})
    sl.save()
    return sl