from openerp.osv import fields, osv

class rdm_rules(osv.osv):
    _name = "rdm.rules"
    _description = "Redemption Rules"
    _columns = {
        'name': fields.char('Name', size=200, required=True),
        'apply_for': fields.selection([('1','Coupon'),('2','Point')],'Apply For',required=True),
        'rule_schema': fields.selection([('birthday','Birthday'),('day','Day'),('dayname','Day Name'),('cardtype','Card Type'),('tenant','Tenant'),('tenanttype','Tenant Type'),('bankcard','Bank Card')],'Schema',required=True),           
        'birthday': fields.boolean('Birthday'),
        'day': fields.date('Day'),    
        'day_name': fields.selection([('01','Sunday'),('02','Monday'),('03','Tuesday'),('04','Wednesday'),('05','Thursday'),('06','Friday'),('07','Saturday')],'Day Name'),           
        'card_type_ids': fields.one2many('rdm.rules.card.type','rules_id','Card Type'),
        'tenant_ids': fields.one2many('rdm.rules.tenant','rules_id','Tenant'),
        'tenant_type_ids': fields.one2many('rdm.rules.tenant.type','rules_id','Tenant Type'),
        'bank_card_ids': fields.one2many('rdm.rules.bank.card','rules_id','Bank Card'),        
        'operation': fields.selection([('add','Add'),('multiple','Multiple')],'Operation'),
        'quantity': fields.float('Quantity'),
    }
rdm_rules()

class rdm_rules_card_type(osv.osv):
    _name = "rdm.rules.card.type"
    _description = "Redemption Rule Card Type"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'card_type_id': fields.many2one('rdm.card.type','Card Type') 
    }

rdm_rules_card_type()
    
class rdm_rules_tenant(osv.osv):
    _name = "rdm.rules.tenant"
    _description = "Redemption Rule Tenant"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'tenant_id': fields.many2one('rdm.tenant','Tenant') 
    }

rdm_rules_tenant()

class rdm_rules_tenant_type(osv.osv):
    _name = "rdm.rules.tenant.type"
    _description = "Redemption Rule Tenant Type"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'tenant_type_id': fields.many2one('rdm.tenant.type','Tenant Type') 
    }

rdm_rules_tenant_type()

class rdm_rules_bank_card(osv.osv):
    _name = "rdm.rules.bank.card"
    _description = "Redemption Rule Bank Card"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'bank_card_id': fields.many2one('rdm.bank.card','Bank Card') 
    }

rdm_rules_bank_card()