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
	onload: function(frm){
		if(frm.doc.__islocal){
			frm.trigger("plan")
		}
	},
	refresh: function(frm) {
		cur_frm.fields_dict['components'].grid.wrapper.find('.grid-add-row').hide();
        cur_frm.fields_dict['components'].grid.wrapper.find('.grid-remove-rows').hide();
		if (frm.doc.outstanding_amount > 0 && frm.doc.docstatus == 1) {
			frm.add_custom_button(__("Collect Fees"), function() {
				frappe.prompt({fieldtype:"Float", label: __("Amount Paid"), fieldname:"amt"},
					function(data) {
						var paid_amount = frm.doc.paid_amount + data.amt;
						frm.set_value("paid_amount",paid_amount)
						frm.set_value("outstanding_amount",(frm.doc.total_amount - paid_amount))
						var today = frappe.datetime.nowdate()
						if(frm.doc.payment_record){
						var payment_record = frm.doc.payment_record + "\n" + today + "- Collected Amount: Rs." + data.amt;
						} else {
						var payment_record = today + "- Collected Amount: Rs." + data.amt;
						}
						frm.set_value("payment_record",payment_record)
					}, __("Enter Paid Amount"), __("Collect"));
			});
		}
	},
	
	plan: function(frm) {
		// refresh_field("components");
		// frm.set_value("components" ,"");
		if (frm.doc.plan) {
			frappe.call({
				method: "frappe.client.get",
				args: {
					"doctype": "Plan Structure",
					"name": frm.doc.plan
				},
				callback: function(r) {
					if (r.message) {
						var fee_component_child = r.message.components;
						$.each(fee_component_child, function(i, d) {
							if(d.fee_type){
								var row = frappe.model.add_child(frm.doc, "Fee Component", "components");
								row.fee_category = d.fee_category;
								row.fee_type = d.fee_type;
								row.amount = d.amount;
								refresh_field("components");
							}							
						});
						refresh_field("components");
					}
					frm.trigger("calculate_total_amount");
				}
			});
			
		}
	},
	calculate_total_amount: function(frm) {
		var total = 0;
		var c;
		var child = frm.doc.components;
		for (c in child){
			if (child[c].fee_type == "Addition"){
				total += child[c].amount
			} else if (child[c].fee_type == "Deduction"){
				total -= child[c].amount
			}
		}
		frm.set_value("total_amount",total)
		var paid_amount = frm.doc.total_amount - frm.doc.paid_amount
		frm.set_value("outstanding_amount",paid_amount)
	},
	validate: function(frm) {
		if(!frm.doc.total_amount){
			frm.trigger("calculate_total_amount");
		}
	}
});