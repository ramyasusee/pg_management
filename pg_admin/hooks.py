# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pg_admin"
app_title = "Madras-Inn PG Management"
app_publisher = "Aftertutor Ventures Pvt Ltd"
app_description = "The app is built to manage the rooms, rent and other costs as well as the occupant management. "
app_icon = "fa fa-building"
app_color = "#03B5AA"
app_email = "contact@atdigitals.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pg_admin/css/pg_admin.css"
# app_include_js = "/assets/pg_admin/js/pg_admin.js"

# include js, css files in header of web template
# web_include_css = "/assets/pg_admin/css/pg_admin.css"
# web_include_js = "/assets/pg_admin/js/pg_admin.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pg_admin.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pg_admin.install.before_install"
# after_install = "pg_admin.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pg_admin.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"*": {
		"on_update": "pg_admin.madras_inn_pg_management.doctype.fee.fee.update"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"cron": {
# 		"* * * * *": [
# 			"pg_admin.madras_inn_pg_management.tasks.every_minute"
# 		]
# 	}
# }

# Testing
# -------

# before_tests = "pg_admin.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pg_admin.event.get_events"
# }

