// Copyright (c) 2022, krupal vora and contributors
// For license information, please see license.txt
frappe.ui.form.on('case', {
	// refresh: function(frm) {

	// }
}); 
frappe.ui.form.on('case medicine child', {
	medecine_name: function (frm) {
		var item = frm.doc.c_medicine;
		for (var i in item) {
			if (item[i].medecine_name) {
				frappe.call({
					method: "pms.pms.pms.doctype.case.case.get_raw_record",
					args: {
						"medecine_name": item[i].medecine_name,
					}
				});
			}
		}
	}
});
