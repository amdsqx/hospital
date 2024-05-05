from odoo import models, fields, api


# model untuk Appointment rumah sakit
class HospitalAppointment(models.Model):
    _name               = 'hospital.appointment'
    _inherit            = ['mail.thread', 'mail.activity.mixin']
    _description        = 'Hospital Appointment'
    _rec_name           = 'patient_id'

    patient_id          = fields.Many2one(comodel_name='hospital.patient', string='Pasien')
    gender              = fields.Selection(related='patient_id.gender', readonly=False)
    appointment_time    = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date        = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref                 = fields.Char(string='Referensi', help="Reference of the patient from patient record")
    # presentasi 28
    prescription        = fields.Html(string='Resep')
    # presentasi 30
    priority            = fields.Selection(string='Priositas', selection=[
                            ('0', 'Normal'),
                            ('1', 'Low'),
                            ('2', 'High'),
                            ('3', 'Very High'),])

    state               = fields.Selection(string='Status', selection=[
                            ('draft', 'Draft'),
                            ('in_consultation', 'In Consultation'),
                            ('done', 'Done'),
                            ('cancel', 'Cancelled')], default="draft", required=True)
    
    

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button check!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click successfull',
                'type': 'rainbow_man',
            }
        }
    
    
    
    
    
    
    
    
