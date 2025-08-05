{
    'name': 'Sale Order Manufacturing Status',
    'version': '16.0',
    'summary': 'Displays Manufacturing Status on Sale Orders',
    'description': """
    This module helps track the manufacturing process status linked to Sale Orders:

    ✔ Shows manufacturing status on Sale Order form  
    ✔ Status includes: No MRP Order, Confirmed, Planned, In Progress, Done  
    ✔ Automatically updates based on related Manufacturing Orders  

    Improve visibility of manufacturing progress from the sales interface.
    """,
    'category': 'Manufacturing',
    'sequence': 10,
    'author': 'Namah Softech Private Limited',
    'maintainer': 'Namah Softech Private Limited',
    'company': 'Namah Softech Private Limited',
    'website': 'https://www.namahsoftech.com',
    'support': 'support@namahsoftech.com',
    'price': 14.99,
    'currency': 'USD',
    'contributors': ['Shivani Solanki'],
    'license': 'AGPL-3',
    'depends': ['sale_management', 'mrp', 'stock'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
