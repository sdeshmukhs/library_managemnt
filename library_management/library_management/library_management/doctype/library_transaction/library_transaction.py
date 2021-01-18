# -*- coding: utf-8 -*-
# Copyright (c) 2021, edjewhfje and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):
    def before_save(self):
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
            "library_member": self.library_member,
            "docstatus": 1,
            "from_date": ("<", self.date),
            "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")

    def before_submit(self):
        if self.type == "Issued":
            self.validation()
            self.validate_issue()
            # set the article status to be Issued
            article = frappe.get_doc("Books", self.books)
            article.status == "Issued"
            article.save()

        elif self.type == "Returned":
            self.validate_return()
            # set the article status to be Available
            article = frappe.get_doc("Books", self.books)
            article.status = "Available"
            article.save()

        def validate_issue(self):
            self.validate_membership()
            article = frappe.get_doc("Books", self.books)
        # article cannot be issued if it is already issued
            if article.status == "Issued":
                frappe.throw("Book is already issued by another member")

        def validation(self):
            valid_book = frappe.db.exists(
                "Library Settings",{
                "Library Member":self.library_member,
                "Maximum number of issued books":("<=", 2),
                },)
            if not valid_book:
                frappe.throw("This member reached max limit")

        def validate_return(self):
            article = frappe.get_doc("Books", self.books)
        # article cannot be returned if it is not issued first
            if article.status == "Available":
                frappe.throw("Book cannot be returned without being issued first")


