# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "aerele_gst"
app_title = "Aerele Gst"
app_publisher = "Aerele Technologies Private Limited"
app_description = "Frappe app to support GST requirements in manufacturing industries"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@aerele.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aerele_gst/css/aerele_gst.css"
# app_include_js = "/assets/aerele_gst/js/aerele_gst.js"

# include js, css files in header of web template
# web_include_css = "/assets/aerele_gst/css/aerele_gst.css"
# web_include_js = "/assets/aerele_gst/js/aerele_gst.js"

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
# get_website_user_home_page = "aerele_gst.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "aerele_gst.install.before_install"
# after_install = "aerele_gst.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aerele_gst.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"aerele_gst.tasks.all"
# 	],
# 	"daily": [
# 		"aerele_gst.tasks.daily"
# 	],
# 	"hourly": [
# 		"aerele_gst.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aerele_gst.tasks.weekly"
# 	]
# 	"monthly": [
# 		"aerele_gst.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "aerele_gst.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "aerele_gst.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "aerele_gst.task.get_dashboard_data"
# }

doctype_js = {
"Sales Invoice" : "public/js/sales_invoice.js",
}
