# Copyright (c) 2022, krupal vora and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class case(Document):
	""" def onload(self):
		self.user=frappe.session.user  #frappe.session.user """
	pass
		


@frappe.whitelist()
def get_raw_record(medecine_name):
	query = """
	select name,medicine,times
	from `tabmedecine` med
	where med.name = '{0}'
	""".format(medecine_name)
	return frappe.db.sql(query, [], as_dict=1)