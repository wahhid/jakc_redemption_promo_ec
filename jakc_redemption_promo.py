from openerp.osv import fields, osv

AVAILABLE_STATES = [
    ('draft','Draft'),    
    ('review','Review'),    
    ('active','Active'),
    ('done','Close'),    
]

class rdm_age_segment(osv.osv):
    _name = 'rdm.age.segment'
    _description = 'Redemption Age Segment'
    _columns = {
        'name': fields.char('Name', size=200, readonly=True),
        'start_age': fields.integer('Start Age', required=True),
        'end_age': fields.integer('End Age', required=True),        
    }    
    
    def create(self, cr, uid, values, context=None):
        values.update({'name':str(values['start_age']) + " to " + str(values['end_age']) + " Years"})        
        return super(rdm_age_segment,self).create(cr,uid,values,context=context)
    
    def write(self, cr, uid, ids, values, context=None):
        values.update({'name':str(values['start_age']) + " to " + str(values['end_age']) + " Years"})        
        return super(rdm_age_segment,self).write(cr, uid, ids, values,context=context)
    
rdm_age_segment()

class rdm_promo_segment(osv.osv):
    _name = 'rdm.promo.segment'
    _description = 'Redemption Promo Segment'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'age_segment': fields.many2one('rdm.age.segment','Age Segment'),
    }    
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_segment()   

class rdm_promo_gender(osv.osv):
    _name = 'rdm.promo.gender'
    _description = 'Redemption Promo gender'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'gender_id': fields.many2one('rdm.customer.gender','Gender'),        
    }    
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_gender()

class rdm_promo_religion(osv.osv):
    _name = 'rdm.promo.religion'
    _description = 'Redemption Promo Religion'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'religion_id': fields.many2one('rdm.customer.religion','Religion'),        
    }    
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_religion()

class rdm_promo_ethnic(osv.osv):
    _name = 'rdm.promo.ethnic'
    _description = 'Redemption Promo Ethnic'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'ethnic_id': fields.many2one('rdm.customer.ethnic','Ethnic'),
    }   
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_ethnic()   

class rdm_promo_tenant(osv.osv):
    _name = 'rdm.promo.tenant'
    _description = 'Redemption Promo Tenant'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'tenant_id': fields.many2one('rdm.tenant','Tenant'),
    }    
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_tenant()   

class rdm_promo_marital(osv.osv):
    _name = 'rdm.promo.marital'
    _description = 'Redemption Promo Marital'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'marital_id': fields.many2one('rdm.customer.marital','Marital'),
    }   
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_marital()   

class rdm_promo_interest(osv.osv):
    _name = 'rdm.promo.interest'
    _description = 'Redemption Promo Interest'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'interest_id': fields.many2one('rdm.customer.interest','Interest'),
    }    
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_interest()   

class rdm_promo_card_type(osv.osv):
    _name = 'rdm.promo.card.type'
    _description = 'Redemption Promo Card Type'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'card_type_id': fields.many2one('rdm.card.type','Card Type'),
    }   
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_card_type()   

class rdm_promo_tenant_type(osv.osv):
    _name = 'rdm.promo.tenant.type'
    _description = 'Redemption Promo Tenant Type'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'tenant_type_id': fields.many2one('rdm.tenant.type','Card Type'),
    }   
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_tenant_type()   

class rdm_promo_rules(osv.osv):
    _name = 'rdm.promo.rules'
    _description = 'Redemption Promo Rules'
    _columns = {
        'promo_id': fields.many2one('rdm.promo','Promo', readonly=True),
        'rules_id': fields.many2one('rdm.rules','Rules'),
    }   
    _defaults = {
        'promo_id': lambda self, cr, uid, context: context.get('promo_id', False),}
        
rdm_promo_rules()   

class rdm_promo(osv.osv):
    _name = 'rdm.promo'
    _description = 'Redemption Promo'
    _columns = {
        'name': fields.char('Name', size=200, required=True),
        'description': fields.text('Description'),
        'desc_email': fields.text('Description For Email'),
        'desc_sms': fields.char('Description For SMS', size=140),
        'start_date': fields.date('Start Date'),
        'end_date': fields.date('End Date'),
        'last_redeem': fields.date('Last Redeem'),                
        'draw_date': fields.date('Draw Date'),
        'spend_amount': fields.float('Spend Amount'),
        'coupon': fields.integer('Coupon #'),
        'point': fields.integer('Point #'),
        'limit_point': fields.integer('Point Limit',help="-1 for No Limit"),
        'segment_ids': fields.one2many('rdm.promo.segment','promo_id','Segment'),
        'image1': fields.binary("Promo Image"),
        'gender_ids': fields.one2many('rdm.promo.gender','promo_id','Promo Gender'),
        'religion_ids': fields.one2many('rdm.promo.religion','promo_id','Promo Religion'),
        'ethnic_ids': fields.one2many('rdm.promo.ethnic','promo_id','Promo Ethnic'),
        'tenant_ids': fields.one2many('rdm.promo.tenant','promo_id','Promo Tenant'),
        'marital_ids': fields.one2many('rdm.promo.marital','promo_id','Promo Marital'),
        'interest_ids': fields.one2many('rdm.promo.interest','promo_id','Promo Interest'),
        'card_type_ids': fields.one2many('rdm.promo.card.type','promo_id','Promo AYC Card Type'),            
        'tenant_type_ids': fields.one2many('rdm.promo.tenant.type','promo_id','Tenant Type'),        
        'rules_ids': fields.one2many('rdm.promo.rules','promo_id','Rules'),
        'state':  fields.selection(AVAILABLE_STATES, 'Status', size=16, readonly=True),
    }
    
    _default = {
        'state': lambda *a: 'draft',
        'limit_point': lambda *a: -1,
    }

rdm_promo()
