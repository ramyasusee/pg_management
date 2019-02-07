from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
			{
				"label": _("Inmates"),
				"items": [
					{
						"type": "doctype",
						"name": "Inmate"
					}
				]
			},
			{
				"label": _("PG Registration"),
				"items": [
					{
						"type": "doctype",
						"name": "Rooms"
					},
					{
						"type": "doctype",
						"name": "House"
					}
				]
			},
			{
				"label": _("Metadata"),
				"items": [
					{
						"type": "doctype",
						"name": "Cot"
					}
				]
			},
			{
				"label": _("SMS Manager"),
				"items": [
					{
						"type": "doctype",
						"name": "SMS Center"
					},
					{
						"type": "doctype",
						"name": "SMS Log"
					},
					{
						"type": "doctype",
						"name": "SMS Templates"
					}
				]
			},
			{
				"label": _("Fees"),
				"items": [
					{
						"type": "doctype",
						"name": "Fee"
					},
					{
						"type": "doctype",
						"name": "Fee Plan"
					}
				]
			}
        ]
