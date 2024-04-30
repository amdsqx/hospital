from odoo import models, fields, api


# model untuk pasien rumah sakit
class HospitalPatient(models.Model):
    _name           = 'hospital.patient'
    _description    = 'Hospital Patient'

    name            = fields.Char(string='Nama')
    ref             = fields.Char(string='Referensi')
    age             = fields.Integer(string='Usia')
    gender          = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),])
    active          = fields.Boolean(string='Active', default=True)
    
    
    
    
