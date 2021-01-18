# -*- coding: utf-8 -*-
# Copyright (c) 2021, edjewhfje and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	pass
	# def before_save(self, first_name, last_name, full_name):
	# 	self.first_name = first_name
	# 	self.last_name = last_name
	# 	self.full name = first_name + last_name
	# 	return self.full_name