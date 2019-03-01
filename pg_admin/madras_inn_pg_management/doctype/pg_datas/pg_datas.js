// Copyright (c) 2019, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt
cur_frm.add_fetch("name1", "mobile_number", "mobile_number")
frappe.ui.form.on('PG Datas', {
	status: function(frm){
		if(frm.doc.status == "Inactive"){
			frm.set_df_property("date_of_relieving", "reqd", 1);
		}
		else{
			frm.set_df_property("date_of_relieving", "reqd", 0);
		}
	},
	validate: function(frm) {
		if(cur_frm.doc.cot){
			frappe.set_route('Form', 'Fee', 'New%20Fee')
		}
		if(cur_frm.doc.date_of_joining > cur_frm.doc.date_of_relieving){
			frappe.throw("Date of joining must be lesser that date of relieving");
			// validate = false;
		}
	},
	fee_plan: function(frm) {
		if (cur_frm.doc.fee_plan == "Fully Furnished") {
			frm.set_df_property("cot", "reqd", 0)
			frm.set_df_property("room", "hidden", 1)
			frm.set_df_property("cot", "hidden", 1)
		}
		else{
			frm.set_df_property("cot", "reqd", 1)
			frm.set_df_property("room", "hidden", 0)
			frm.set_df_property("cot", "hidden", 0)
		}
	},
	on_submit: function(frm) {
		frappe.set_route('Form', 'Fee', 'New')
	}
});