from openerp.osv import fields, osv
import datetime

import logging
_logger = logging.getLogger(__name__)

AVAILABLE_STATES = [
    ('draft','New'),    
    ('open','Open'),    
    ('done', 'Closed'),
]

class rdm_promo_trans(osv.osv):
    _name =  "rdm.promo.trans"
    _description = "Redemption Promo Transaction"
    
    def trans_close(self, cr, uid, ids, context=None):        
        self.write(cr,uid,ids,{'state':'done'},context=context)              
        return True
    
    def _get_active_promo(self, cr, uid, context=None):          
        _logger.info("Start Get Active Promo")
        current_date = datetime.date.today().strftime('%Y-%m-%d')
        ids = self.pool.get('rdm.promo').search(cr, uid, [('start_date','<=',current_date),'|',('end_date','>=',current_date)], context=context)
        if len(ids) == 1:
            id = ids[0]
            promo = self.pool.get('rdm.promo').browse(cr, uid, id, context=context)
            if promo.state == 'active':
                _logger.info("Active Promo Found")
                return promo.id        
        else:                
            _logger.info("Active Promo not Found")
        _logger.info("End Get Active Promo")    
        return None
            
    def _get_trans(self, cr, uid, trans_id , context=None):
        return self.pool.get('rdm.promo.trans').browse(cr, uid, trans_id, context=context);
            
    def _get_trans_detail(self, cr, uid, trans_id, context=None):
        return self.pool.get('rdm.promo.trans.detail').browse(cr, uid, trans_id, context=context)

    def _get_promo_rules(self, cr, uid, promo_id, context=None):
        ids = self.pool.get('rdm.promo.rules').search(cr, uid, [('promo_id','=',promo_id)], context=context);
        return self.pool.get('rdm.promo.rules').browse(cr, uid, ids, context=context)
        
    def _generate_coupon(self, cr, uid, trans_id, context=None):        
        trans = self._get_trans(cr, uid, trans_id)
        for i in range(trans.total_coupon):
            values = {}
            values.update({'trans_id':trans_id})       
            result = self.pool.get('rdm.promo.trans.coupon').create(cr, uid, values, context=context)        
            
    def _generate_point(self, cr, uid, trans_id, context=None):
        trans = self._get_trans(cr, uid, trans_id)
    
    def _calculate_add_coupon(self, cr, uid, promo_id, context=None):
        promo = self.pool.get('rdm.promo')
        return 0
    
    def _calcuate_add_point(self, cr, uid, promo_id, context=None):
        return 0
    
    def _get_bank_card_filters(self, cr ,uid, promo_id, trans_id, context=None):
        status  = False
        message = "Not Allowed"
        return 
    
    def _get_tenant_filters(self, cr, uid, promo_id, tenant_id, context=None):
        status = False
        message = ""        
        
        promo = self.pool.get('rdm.promo').browse(cr, uid, promo_id, context=context)
        tenant = self. pool.get('rdm.tenant').browse(cr, uid, tenant_id, context=context)
        
        if promo and tenant:
            tenant_ids = promo.tenant_ids
            tenant_type_ids = promo.tenant_type_ids
            
            if tenant_ids or tenant_type_ids:
                print ""
            else:
                status = True
                message = ""
                
        return status, message
    
    def _get_customer_filters(self, cr, uid, promo_id, customer_id, context=None):                
        segment_status = False
        segment_message = "Segment not Allowed"
        gender_status = False
        gender_message = "Gender not Allowed"
        religion_status = False
        religion_message = "Religion not Allowed"
        ethnic_status = False
        ethnic_message = "Ethnic not Allowed"       
        marital_status = False
        marital_message = "Marital not Allowed"
        interest_status = False
        interest_message = "Interest not Allowed"
        cardtype_status = False
        cardtype_message= "Card Type not Allowed"
        
        
        message = ""
        promo = self.pool.get('rdm.promo').browse(cr, uid, promo_id, context=context)
        print "==Promo=="
        print promo
        customer = self.pool.get('rdm.customer').browse(cr, uid, customer_id, context=context)
        print "==Customer=="
        print customer
        #Filter Segment        
        _logger.info("Start Segment Filter")
        if promo.segment_ids:            
            for segment in promo.segment_ids:
                customer_age = datetime.date.today() - customer.birth_date
                if customer_age >= customer.start_age and customer_age <= customer.end_age:
                    segment_message = "Segment Allowed"
                    segment_status = True                    
        else:            
            segment_message = "Seg ment Allowed"
            segment_status = True         
        _logger.info("End Segment Filter")
        #Filter Gender    
        _logger.info("Start Gender Filter")
        if promo.gender_ids:            
            for gender in promo.gender_ids:
                print "==Gender=="
                print gender.id
                print customer.gender.id
                if gender.id == customer.gender.id:
                    gender_message = "Gender Allowed"                                                
                    gender_status = True
        else:            
            message = message + "\n" + "Gender Allowed"                                                
            gender_status = True
        _logger.info("End Gender Filter")
        if promo.religion_ids:
            for religion in promo.religion_ids:
                if religion.id == customer.religion.id:
                    religion_message = "Religion Allowed"                                                
                    religion_status = True                
        else:
            religion_message = "Religion Allowed"                                                
            religion_status = True
        if promo.ethnic_ids:
            for ethnic in promo.ethnic_ids:
                if ethnic.id == customer.ethnic.id:
                    ethnic_message = "Ethnic Allowed"                                                
                    ethnic_status = True
        else:
            ethnic_message = "Ethnic Allowed"                                                
            ethnic_status = True
        
        if promo.marital_ids:
            for marital in promo.marital_ids:
                if marital.id == customer.marital.id:
                    marital_message = "Marital Allowed"                                                
                    marital_status = True
        else:
            marital_message = "Marital Allowed"                                                
            marital_status = True
            
        if promo.interest_ids:
            for interest in promo.interest_ids:
                if interest.id == customer.interest.id:
                    interest_message = "Interest Allowed"                                                
                    interest_status = True                    
        else: 
            interest_message = "Interest Allowed"                                                
            interest_status = True                
            
        if promo.card_type_ids:
            for card_type in promo.card_type_ids:
                if card_type.id == customer.card_type.id:
                    cardtype_message = "Card Type Allowed"                                                
                    cardtype_status = True                
        else:
            cardtype_message = "Card Type Allowed"                                                
            cardtype_status = True                             
            
        status = segment_status and gender_status and religion_status and ethnic_status and marital_status and interest_status and cardtype_status
        message = segment_message + "\n" + gender_message + "\n" + religion_message + "\n" + ethnic_message + "\n" + marital_message + "\n" + interest_message + "\n" + cardtype_message
        
        return status, message
    
    def _process_calculation(self, cr, uid, trans_id, context=None):
        trans = self._get_trans(cr, uid, trans_id, context=context)     
        print "===Tans==="
        print trans
        total_amount = 0
        valid_amount = 0
        total_item = 0
        total_coupon = 0
        total_point = 0    
        coupon = 0
        point = 0
        add_coupon = 0
        add_point = 0
        tenants = trans.promo_id.tenant_ids        
        for trans_detail in trans.trans_detail_ids:                    
            total_amount = total_amount + trans_detail.total_amount              
            total_item = total_item + trans_detail.total_item        
            #Calculate valid_amount
            #Check Tenant Type and Tenant
            valid_amount = valid_amount + trans_detail.total_amount
            #Calculate Coupon            
            #Calculate Point                    
        
        status_customer, message_customer = self._get_customer_filters(cr, uid, trans.promo_id.id, trans.customer_id.id, context=context)
        status_tenant, message_tenant = self._get_tenant_filters(cr, uid, trans.promo_id.id, trans.trans_detail_ids, context=context )
        
        status = status_customer
        message = message_customer
        
        trans_data = {}
        if status == True:
            coupon = (total_amount // trans.promo_id.spend_amount) * trans.promo_id.coupon
            point = (total_amount // trans.promo_id.spend_amount) * trans.promo_id.point

            total_coupon = coupon + add_coupon
            total_point = point + add_point
            
            trans_data.update({'total_amount':total_amount})                
            trans_data.update({'total_item':total_item})                      
            trans_data.update({'total_coupon':total_coupon})
            trans_data.update({'total_point':total_point})
            trans_data.update({'coupon':coupon})
            trans_data.update({'point':point})
            trans_data.update({'add_coupon':add_coupon})
            trans_data.update({'add_point':add_point})
            trans_data.update({'remark':message})
        else:
            trans_data.update({'total_amount':total_amount})                
            trans_data.update({'total_item':total_item})                      
            trans_data.update({'remark':message})
            
        super(rdm_promo_trans,self).write(cr, uid, [trans_id], trans_data, context=context)  
            
    _columns = {
        'customer_id': fields.many2one('rdm.customer','Customer',required=True),
        'promo_id': fields.many2one('rdm.promo','Promo',required=True),
        'trans_date': fields.date('Date', required=True, readonly=True),
        'total_amount': fields.float('Total Amount', readonly=True),
        'valid_amount': fields.float('Valid Amount', readonly=True),
        'total_item': fields.integer('Total Item', readonly=True),  
        'total_coupon': fields.integer('Total Coupon', readonly=True),
        'total_point': fields.integer('Total Point', readonly=True),
        'coupon': fields.integer('Coupon', readonly=True),
        'point': fields.integer('Point', readonly=True),
        'add_coupon': fields.integer('Additional Coupon', readonly=True),
        'add_point': fields.integer('Additional Point', readonly=True),
        'state':  fields.selection(AVAILABLE_STATES, 'Status', size=16, readonly=True),
        'trans_detail_ids': fields.one2many('rdm.promo.trans.detail','trans_id','Details'),
        'trans_coupon_ids': fields.one2many('rdm.promo.trans.coupon','trans_id','Coupons'),
        'remark': fields.text('Remark'),
    }   
    _defaults = {
        'trans_date': fields.date.context_today,      
        'state': lambda *a: 'open',
    }
    
    def create(self, cr, uid, values, context=None):
        trans_id = super(rdm_promo_trans,self).create(cr, uid, values, context=context)    
        self._process_calculation(cr, uid, trans_id, context=context)
        self._generate_coupon(cr, uid, trans_id, context=context)
        return trans_id
            
    def write(self, cr, uid, ids, values, context=None ):        
        result = super(rdm_promo_trans,self).write(cr, uid, ids, values, context=context)        
        trans_id = ids[0]
        print trans_id
        self._process_calculation(cr, uid, trans_id, context=context)                
        return result
        
rdm_promo_trans()

class rdm_promo_trans_detail(osv.osv):
    _name = "rdm.promo.trans.detail"
    _description = "Redemption Promo Transaction Detail"
    _columns = {
        'trans_id': fields.many2one('rdm.promo.trans','Transaction', required=True),
        'tenant_id': fields.many2one('rdm.tenant','Tenant',required=True),
        'trans_date': fields.date('Date',required=True),
        'total_amount': fields.float('Total Amount',required=True),
        'total_item': fields.integer('Total Item'),
        'payment_type': fields.selection([('cash','Cash'),('creditcard','Credit Card'),('debit','Debit')],'Payment Type',required=True),
        'bank': fields.many2one('rdm.bank','Bank'),
        'card_type': fields.selection([('visa','Visa'),('master','Master')],'Card Type'),
        'card_number': fields.char('Card Number', size=20)        
    }
    
    _defaults = {
        'trans_date': fields.date.context_today,
        'payment_type': lambda *a: 'cash'
    }

rdm_promo_trans_detail()


class rdm_promo_trans_coupon(osv.osv):
    _name = "rdm.promo.trans.coupon"
    _description = "Redemption Promo Transaction Coupon"
    _columns = {
        'trans_id': fields.many2one('rdm.promo.trans','Transaction', required=True),
        'coupon_num': fields.char('Coupon #', size=10)    
    }    
    _defaults = {
        'coupon_num' : lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'rdm.promo.trans.coupon.sequence'),        
    }
rdm_promo_trans_coupon()