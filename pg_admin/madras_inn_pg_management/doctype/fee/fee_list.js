frappe.listview_settings['Fee'] = {
	add_fields: [ "total_amount", "paid_amount"],
	get_indicator: function(doc) {
		// if ((doc.total_amount > doc.paid_amount) && doc.due_date < get_today()) {
		// 	return [__("Overdue"), "red", ["due_date,<,"+get_today()], ["due_date,<,"+get_today()]];
		// }
		if (doc.total_amount > doc.paid_amount) {
			return [__("Pending"), "red", ["total_amount,>,paid_amount"]];
		}
		else {
			return [__("Paid"), "green", ["total_amount,<=,paid_amount"]];
		}
	}
};