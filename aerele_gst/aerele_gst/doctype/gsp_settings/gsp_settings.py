# -*- coding: utf-8 -*-
# Copyright (c) 2020, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from erpnext.regional.india.utils import generate_ewb_json

class GSPSettings(Document):
	pass


@frappe.whitelist()
def generate_eway_bill(dt, dn, additional_val):
	ewb = generate_ewb_json(dt, dn)
	return ewb

