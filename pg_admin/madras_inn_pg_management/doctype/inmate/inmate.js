// Copyright (c) 2019, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Inmate', {
	// validate: function(frm){
	// 	if(!frm.doc.enter_the_otp){
	// 		frappe.validate = false;
	// 		frappe.msgprint("Enter the OTP to save your details");
	// 	}
	// 	if(frm.doc.enter_the_otp != frm.doc.generated_otp){
	// 		frappe.validate = false;
	// 		frappe.msgprint("Enter the OTP to save your details")
	// 	}
	// 	if(!frm.doc.i_agree_to_the_given_terms_and_conditions){
	// 		frappe.validate = false;
	// 		frappe.msgprint("Please Agree the Terms & Conditions");			
	// 	}
	// },
	on_submit: function(frm) {
		if(cur_frm.doc.mobile_number){
			frappe.set_route('Form', 'PG Datas', 'New PG Datas',{"occupant_id": frm.doc.name})
		}
	},
	validate_otp: function(frm){
		if(!frm.doc.enter_the_otp){
			frappe.msgprint("Enter the OTP to save your details")
		}
        if(frm.doc.enter_the_otp != frm.doc.generated_otp){
			frappe.msgprint("The OTP you entered is not right")
		}else if(frm.doc.enter_the_otp == frm.doc.generated_otp && frm.doc.enter_the_otp && frm.doc.generated_otp){
			frappe.msgprint("OTP is verified")
		}
	}
	// refresh: function(frm){
	// 	if ((frm.doc.enter_the_otp == frm.doc.generated_otp) && frm.doc.enter_the_otp != ""){
	// 		frm.set_df_property("enter_the_otp", "hidden", 1)
	// 	}
	// }
});
