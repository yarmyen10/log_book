# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class LogBook(models.Model):
    _name = 'log.book'
    _description = 'Log Book'
    # _order = 'id'
    # _rec_name = 'number'

    # line_number = fields.Char(string='ที', required=True, copy=False, readonly=True, 
    # default=lambda self: _('New'))

    postal_type = fields.Many2one('log.book.postal.type', string='ประเภท')
    recipient_name = fields.Char(string='นามผู้รับ', required=True)
    destination = fields.Char(string='ปลายทาง')
    barcode = fields.Char(string='Barcode (9 ตัวเลข)', size=9, required=True)
    weight = fields.Float(string='น้ำหนัก')
    satang = fields.Float(string='ค่าบริการ')
    note = fields.Text(string='หมายเหตุ')

    # number = fields.Char(string='Log number', required=True, copy=False, readonly=True, 
    #                      default=lambda self: _('New'))
    
    # receiver_line_ids = fields.One2many('log.book.receiver.lines', 'log_book_id',
    #                                     string='Receiver Lines')
    # image = fields.Binary(string='Log brand')
    
    # @api.model
    # def create(self, vals):
    #     if vals.get('number', _('New')) == _('New'):
    #         vals['number'] = self.env['ir.sequence'].next_by_code('log.book') or _('New')
    #     res = super(LogBook, self).create(vals)
    #     return res
    
class LogBookPostalType(models.Model):
    _name = 'log.book.postal.type'
    _description = ''

    # required=True, translate=True
    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    color = fields.Integer(string='Color')

# # Master Log_Book_Type
# class LogBookReceiverLines(models.Model):
#     _name = 'log.book.receiver.lines'
#     _description = ''

#     # required=True, translate=True
#     log_book_id = fields.Many2one('log.book', string='Log Book')
#     name = fields.Char(string='Name', required=True)
#     destination = fields.Char(string='Destination')
#     barcode = fields.Char(string='Barcode (9 digit)', size=9, required=True)
#     weight = fields.Float(string='Weight')
#     baht = fields.Integer(string='Baht')
#     satang = fields.Float(string='Satang')
#     note = fields.Text(string='Note')