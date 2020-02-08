// Copyright (c) 2019, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Plan Structure', {
	validate: function(frm) {
		var total = 0;
		var c;
		var child = frm.doc.components;
		for (c in child){
			if (child[c].fee_type == "Addition"){
				total += child[c].amount
			} else {
				total -= child[c].amount
			}
		}
		frm.set_value("total_amount",total)
	}
});
