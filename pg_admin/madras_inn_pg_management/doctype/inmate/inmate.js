// Copyright (c) 2019, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Inmate', {
	on_submit: function(frm) {
		if(cur_frm.doc.mobile_number){
			frappe.set_route('Form', 'PG%20Datas', 'New%20PG%20Datas%201')
		}
	}
	// refresh: function(frm){
	// 	if ((frm.doc.enter_the_otp == frm.doc.generated_otp) && frm.doc.enter_the_otp != ""){
	// 		frm.set_df_property("enter_the_otp", "hidden", 1)
	// 	}
	// }
});
