# -*- coding: utf-8 -*-
# Copyright (c) 2020, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from erpnext.regional.india.utils import generate_ewb_json
from requests import request
import json
import random, string

class GSPSettings(Document):
	pass


@frappe.whitelist()
def generate_eway_bill(dt, dn, additional_val):
	doc = frappe.get_single("GSP Settings")
	# ewb = generate_ewb_json(dt, dn)
	ewb = json.loads('{"version":"1.0.1118","billLists":[{"transporterId":"29AKLPM8755F1Z2","TotNonAdvolVal":0,"userGstin":"05AAACG2115R1ZN","fromGstin":"05AAACG2115R1ZN","supplyType":"O","subSupplyType":1,"docType":"INV","docDate":"23/05/2020","fromPincode":641604,"fromStateCode":33,"actualFromStateCode":33,"toGstin":"05AAACG2140A1ZL","toPincode":841239,"toStateCode":10,"transType":1,"actualToStateCode":10,"itemList":[{"hsnCode":61034200,"taxableAmount":131307,"qtyUnit":"","sgstRate":0,"cgstRate":0,"igstRate":5,"cessRate":0,"cessNonAdvol":0},{"hsnCode":61091000,"taxableAmount":40375,"qtyUnit":"","sgstRate":0,"cgstRate":0,"igstRate":5,"cessRate":0,"cessNonAdvol":0}],"totalValue":171682,"cgstValue":0,"sgstValue":0,"igstValue":8412.42,"cessValue":0,"OthValue":-3433.64,"totInvValue":176661,"transDistance":1234,"transMode":1,"vehicleType":"R","docNo":"INV20/21-00498","fromTrdName":"Essdee Knitting Mills Private Limited","toTrdName":"HANDLOOM STORE","transDocNo":"","fromAddr1":"4/1, first floor, 3rd street, Sivasakthi Nagar","fromAddr2":"K.T.C School Road,","fromPlace":"Tirupur","toAddr1":"MAIRWA MAIN ROAD,MAIRWA.","toAddr2":"","toPlace":"MAIRWA","transporterName":""}]}')
	data = make_supporting_request_data(ewb['billLists'][0])
	token = get_token()

	url = doc.endpoint + "/test/enriched/ewb/ewayapi?action=GENEWAYBILL"

	payload = json.dumps(data)
	headers = {
	'Content-Type': 'application/json',
	'username': '05AAACG2115R1ZN',
	'gstin': '05AAACG2115R1ZN',
	'requestid': ''.join(random.choice(string.ascii_letters) for i in range(5)),
	'Authorization': token
	}

	response = request("POST", url, headers=headers, data = payload)
	import pdb; pdb.set_trace()
	print(response.text.encode('utf8'))
	return ewb

def construct_request():
	doc = frappe.get_single("GSP Settings")
	return doc

def make_supporting_request_data(ewb):
	doc = frappe.get_single("GSP Settings")
	for key_row in doc.match_keys:
		if key_row.erpnext_key in ewb:
			ewb[key_row.gsp_key] = ewb[key_row.erpnext_key]
			del ewb[key_row.erpnext_key]
		else:
			if key_row.is_mandatory:
				#Throw error
				pass
	return ewb

def get_token():
	doc = frappe.get_single("GSP Settings")
	url = doc.endpoint
	url += '/gsp/authenticate?grant_type=token'
	clinet_id = doc.api_key
	clinet_secret = doc.api_secret
	payload  = {}
	headers = {
		'gspappid': clinet_id,
		'gspappsecret': clinet_secret
	}
	response = request("POST", url, headers=headers, data = payload)
	return "Bearer " + json.loads(response.text.encode('utf8'))['access_token']
