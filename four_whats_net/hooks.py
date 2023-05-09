from . import __version__ as app_version

app_name = "four_whats_net"
app_title = "Four Whats Net"
app_publisher = "hts-qatar"
app_description = "4Whats.net"
app_email = "azim@htsqatar.com"
app_license = "MIT"
fixtures = [{
		"dt": "Property Setter", "filters": [
		[
			"name", "in", [
				"Notification-channel-options",
			]
		]
	]
	}
,]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/four_whats_net/css/four_whats_net.css"
# app_include_js = "/assets/four_whats_net/js/four_whats_net.js"

# include js, css files in header of web template
# web_include_css = "/assets/four_whats_net/css/four_whats_net.css"
# web_include_js = "/assets/four_whats_net/js/four_whats_net.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "four_whats_net/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "four_whats_net.utils.jinja_methods",
#	"filters": "four_whats_net.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "four_whats_net.install.before_install"
# after_install = "four_whats_net.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "four_whats_net.uninstall.before_uninstall"
# after_uninstall = "four_whats_net.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "four_whats_net.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

doctype_js = {
	"Notification" : "public/js/notification.js"
}

override_doctype_class = {
	"Notification": "four_whats_net.overrides.notifications.ERPGulfNotification"
 }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"four_whats_net.tasks.all"
#	],
#	"daily": [
#		"four_whats_net.tasks.daily"
#	],
#	"hourly": [
#		"four_whats_net.tasks.hourly"
#	],
#	"weekly": [
#		"four_whats_net.tasks.weekly"
#	],
#	"monthly": [
#		"four_whats_net.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "four_whats_net.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "four_whats_net.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "four_whats_net.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["four_whats_net.utils.before_request"]
# after_request = ["four_whats_net.utils.after_request"]

# Job Events
# ----------
# before_job = ["four_whats_net.utils.before_job"]
# after_job = ["four_whats_net.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"four_whats_net.auth.validate"
# ]
