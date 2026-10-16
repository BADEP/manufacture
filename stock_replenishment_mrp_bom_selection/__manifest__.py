# Copyright 2024 Tecnativa - Pilar Vargas
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Replenishment MRP BoM Selection",
    "version": "20.0.1.0.0",
    "license": "AGPL-3",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/manufacture",
    "depends": ["stock", "mrp"],
    "data": [
        "wizard/material_availability_wizard_views.xml",
        "wizard/stock_warehouse_orderpoint_replenish_wizard_views.xml",
        "security/ir.access.csv",
    ],
    "installable": True,
    "development_status": "Beta",
}
