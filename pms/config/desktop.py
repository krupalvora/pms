from __future__ import unicode_literals

from frappe import _

def get_data():
	return [
		{
			"category": "Modules",
			"module_name": "pms",
			"reverse": 1,	
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("pms")
		}
	]
