from odoo import models, fields, api
from datetime import date


# model untuk pasien rumah sakit
class HospitalPatient(models.Model):
    _name           = 'hospital.patient'
    _inherit        = ['mail.thread', 'mail.activity.mixin']
    _description    = 'Hospital Patient'
    _rec_name       = 'name'

    name            = fields.Char(string='Nama', tracking=True)
    date_of_birth   = fields.Date(string='Day Of Birth')
    ref             = fields.Char(string='Referensi')
    age             = fields.Integer(string='Usia', compute='_compute_age', tracking=True)
    gender          = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan')], tracking=True, default='L')
    active          = fields.Boolean(string='Active', default=True)
    appointment_id  = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                self.age = 1
    
    
    
    
