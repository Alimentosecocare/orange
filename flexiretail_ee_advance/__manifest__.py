# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    'name': 'POS Retail with Responsive Design (Enterprise)',
    'version': '5.2.1',
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'summary': 'POS Retail with Responsive Design (Enterprise)',
    'description': "POS Retail with Responsive Design (Enterprise)",
    'category': 'Point Of Sale',
    'website': 'http://www.acespritech.com',
    'depends': ['base', 'web', 'bus', 'point_of_sale', 'sale_management',
        'barcodes', 'stock', 'product_expiry', 'purchase', 'hr_attendance',
        'account'
    ],
    'price': 250.00,
    'currency': 'EUR',
    'images': [
        'static/description/main_screenshot.png',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/reservation_data.xml',
        'data/product_expiry_scheduler.xml',
        'data/product_alert_email_template.xml',
        'data/pos_cache_data.xml',
        'views/res_config_setting_view.xml',
        'views/flexiretail.xml',
        'views/res_config_settings.xml',
        'views/generate_product_barcode_view.xml',
        'views/point_of_sale.xml',
        'views/pos_config.xml',
        'views/res_config_settings.xml',
        'views/sale_view.xml',
        'views/product_view.xml',
        'views/product_brand_view.xml',
        'views/account_view.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/gift_card.xml',
        'views/voucher_view.xml',
        'views/voucher_code_sequence.xml',
        'views/res_users_view.xml',
        'views/pos_sales_report_template.xml',
        'views/pos_sales_report_pdf_template.xml',
        'views/sales_details_pdf_template.xml',
        'views/sales_details_template.xml',
        'views/front_sales_report_pdf_template.xml',
        'views/front_sales_thermal_report_template.xml',
        'views/front_inventory_session_pdf_report_template.xml',
        'views/front_inventory_session_thermal_report_template.xml',
        'views/front_inventory_location_pdf_report_template.xml',
        'views/front_inventory_location_thermal_report_template.xml',
        'views/pos_report.xml',
        'reports.xml',
        'wizard/wizard_pos_sale_report_view.xml',
        'wizard/wizard_sales_details_view.xml',
        'wizard/wizard_pos_x_report.xml',
        'views/pos_promotion_view.xml',
        'views/stock_production_lot_view.xml',
        'views/wallet_management_view.xml',
        'views/cash_inout_menu.xml',
        'views/pos_store_view.xml',
        'views/stock.xml',
        'views/customer_display.xml',
        'views/dashboard.xml',
        'views/pos_z_report_template.xml',
        'views/pos_x_thermal_report.xml',
        'views/pos_z_thermal_report.xml',
        'views/pos_cache_views.xml',
        'views/delivery_order_screen.xml',
        'views/non_moving_product_report.xml',
        'wizard/non_moving_stock.xml',
        'report/grp_category_product_expiry_report_template.xml',
        'wizard/product_expiry_report_wizard_view.xml',
        'views/product_expiry_report_view.xml',
        'data/send_mail.xml',
        'report/pos_payment_report_action.xml',
        'wizard/pos_pending_report_wizard_view.xml',
        'wizard/set_product_valid_days.xml',
        'report/pos_pending_payment_report_template.xml',

        # Direct Login Pull
        'views/webclient_templates.xml',
    ],
    'post_init_hook': 'post_init',
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
