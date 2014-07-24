{
    'name' : 'Redemption and Point Management - Promo Module',
    'version' : '1.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/Redemption And Point Management',
    'depends' : ['base_setup','base','jakc_redemption','jakc_redemption_customer','jakc_redemption_tenant'],
    'init_xml' : [],
    'data' : [			
        'security/ir.model.access.csv',
        'jakc_redemption_promo_view.xml',
        'jakc_redemption_rule_view.xml',
        'jakc_redemption_promo_trans_view.xml',        
        'jakc_redemption_promo_menu.xml',    
        'jakc_redemption_rule_menu.xml',   
        'jakc_redemption_promo_trans_menu.xml',   
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}