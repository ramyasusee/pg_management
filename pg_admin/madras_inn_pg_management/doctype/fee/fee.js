// Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt

// cur_frm.add_fetch("data_1", "cot", "cot_number");
// cur_frm.add_fetch("data_1", "fee_plan", "fee_structure");
// cur_frm.add_fetch("data_1", "status", "status");
// cur_frm.add_fetch("data_1", "date_of_joining", "date_of_joining");
// cur_frm.add_fetch("data_1", "date_of_relieving", "date_of_relieving");
// cur_frm.add_fetch("data_1", "mobile_number", "mobile_number");

frappe.ui.form.on('Fee', {
//
	refresh: function(frm) {
		if (frm.doc.docstatus === 0 && (frm.doc.total_amount > frm.doc.paid_amount)) {
			frm.add_custom_button(__("Collect Fees"), function() {
				frappe.prompt({fieldtype:"Float", label: __("Amount Paid"), fieldname:"amt"},
					function(data) {
						frappe.call({
							method:"pg_admin.madras_inn_pg_management.api.collect_fees",
							args: {
								"fees": frm.doc.name,
								"amt": data.amt
							},
							callback: function(r) {
								frm.doc.paid_amount = r.message
								frm.doc.outstanding_amount = frm.doc.total_amount - r.message
								frm.doc.advance_pending = frm.doc.components[3].amount - frm.doc.paid_amount;
								if(frm.doc.advance_pending < 0){
									frm.doc.advance_pending = 0;
								}
								frm.refresh()
							}
						});
					}, __("Enter Paid Amount"), __("Collect"));
			});
		}
		if (frm.doc.total_amount == 0) {
			frm.trigger("calculate_total_amount");
		}
	},
	
	fee_structure: function(frm) {
		frm.set_value("components" ,"");
		if (frm.doc.fee_structure) {
			frappe.call({
				method: "pg_admin.madras_inn_pg_management.api.get_fee_components",
				args: {
					"fee_structure": frm.doc.fee_structure
				},
				callback: function(r) {
					if (r.message) {
						$.each(r.message, function(i, d) {
							var row = frappe.model.add_child(frm.doc, "Fee Component", "components");
							row.fee_category = d.fee_category;
							row.amount = d.amount;
						});
					}
					refresh_field("components");
					frm.trigger("calculate_total_amount");
				}
			});
		}
	},
	calculate_total_amount: function(frm) {
		total_amount = 0;
		if(cur_frm.doc.fee_structure == "Daily PG"){
				var dailypg_days = frappe.datetime.get_diff(frm.doc.date_of_relieving, frm.doc.date_of_joining);
				cost_per_day = frm.doc.components[0].amount;
				frm.doc.components[0].amount = dailypg_days * frm.doc.components[0].amount;
			}
		for(var i=0;i<frm.doc.components.length;i++) {
			total_amount += frm.doc.components[i].amount;
		}
		if(frm.doc.components[4].amount > 0){
			total_amount = total_amount - (frm.doc.components[4].amount * 2)
		}
		if((frm.doc.components[3].fee_category == "Advance") && (frm.doc.components[3].amount > 0)){
			frm.doc.advance_pending = frm.doc.components[3].amount;
			// frm.doc.components[3].amount = 0;
		}
		frm.set_value("total_amount", total_amount);
		frm.doc.components[0].amount = cost_per_day;
		//frm.set_value("pending_amount", total_amount)
	},
	validate: function(frm) {
		frm.trigger("calculate_total_amount");
		refresh_field("total_amount");
		if(frm.doc.paid_amount == ""){
			frm.set_value("outstanding_amount", total_amount);
		}
		frm.refresh();
		// if(frm.doc.date_of_invoice == frappe.datetime.month_start()){
		// if(cur_frm.doc.fee_structure == "Daily PG"){
		// 		var dailypg_days = frappe.datetime.get_diff(frm.doc.date_of_relieving, frm.doc.date_of_joining);
		// 		var frm.doc.components[0].amount = dailypg_days * frm.doc.components[0].amount;
		// 		frm.set_value("total_amount", total_amountt); 
		// 		refresh_field("total_amount");
		// 	}
		
	}
});