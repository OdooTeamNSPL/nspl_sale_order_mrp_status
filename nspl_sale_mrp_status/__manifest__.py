{
    'name': 'Sale Order Manufacturing Status',
    'version': '19.0.1',
    'category': 'Sales / Manufacturing / Stock',
    'summary': 'Displays Manufacturing Status of related MOs in Sale Orders',
    'description': """
This module adds a computed field "Manufacturing Status" to Sale Orders. 
It automatically shows the status of related Manufacturing Orders as:
- Confirmed
- In Progress
- Done
- No MO

Status updates automatically based on Delivery and Manufacturing validations.
The field is visible in both Form and List views.
Compatible with Odoo 16, 17, and 18.
No group-by filters to avoid RPC errors.
""",
    'author': 'Mohit Nare',
    'maintainer': 'Namah Softech Private Limited',
    'contributors': ['Mohit Nare'],
    'website': 'http://namahsoftech.com/',
    'support': 'support@namahsoftech.com',
    'price': 14.90,
    'currency': 'USD',
    'license': 'OPL-1',
    'depends': ['sale_management', 'mrp', 'account', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_mrp_view.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
