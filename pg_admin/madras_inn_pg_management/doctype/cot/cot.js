// Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cot', {
	onload: function(frm) {
		frm.fields_dict['room'].get_query = function(doc) {
			return {
				filters: {
					"house": doc.house
				}
			}
		}
	}
});
