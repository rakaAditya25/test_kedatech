
from odoo import models, api, fields, _
from odoo.exceptions import ValidationError

class MaterialRegistrasi(models.Model):
    _name = 'material.registrasi'
    

    code = fields.Char(string='Material Code', required=True)
    name = fields.Char(string='Material Name', required=True)
    type = fields.Selection([('pabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')], string="Material Type", required=True)
    buy_price = fields.Float(string='Buy Price')
    supplier_id = fields.Many2one('res.partner', string='Name Supplier')


    #Validasi Buy_price
    @api.constrains('buy_price')
    def _check_buy_price(self):
        for line in self:
            if line.buy_price < 100 :
                raise ValidationError(_('Buy Price  must be upper than 100'))
