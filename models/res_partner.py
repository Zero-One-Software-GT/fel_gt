# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
import logging

class Partner(models.Model):
    _inherit = "res.partner"

    nombre_facturacion_fel = fields.Char('Nombre facturación FEL', copy=False)

    def write(self, vals):
        vat = vals.get('vat')
        vals['vat'] = self.clean_vat(vat)
        result = super(Partner, self).write(vals)
        return result

    def clean_vat(self, vat):
        if vat:
            vat = vat.upper()
            if vat == 'C/F':
                return 'CF'
            if '-' in vat:
                vat = vat.replace('-', '')
                return vat
            return vat
        else:
            return None
    
    @api.model_create_multi
    def create(self, vals_list):
        partners = super(Partner, self).create(vals_list=vals_list)
        for partner, vals in zip(partners, vals_list):
            partner.write({ 
                'vat': self.clean_vat(vals.get('vat'))
            })
        return partners

