from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    manufacturing_status = fields.Selection([
        ('no', 'No MRP Order'),
        ('confirmed', 'Confirmed'),
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Manufacturing Status', compute='_compute_mfg_status')

    mrp_order_count = fields.Integer(string="MRP Order Count", compute='_compute_mrp_order_count')

    @api.depends('name')
    def _compute_mfg_status(self):
        for order in self:
            mrp_orders = self.env['mrp.production'].search([('origin', '=', order.name)])
            if not mrp_orders:
                order.manufacturing_status = 'no'
            elif all(m.state == 'confirmed' for m in mrp_orders):
                order.manufacturing_status = 'confirmed'
            elif all(m.state == 'planned' for m in mrp_orders):
                order.manufacturing_status = 'planned'
            elif all(m.state == 'done' for m in mrp_orders):
                order.manufacturing_status = 'done'
            elif all(m.state == 'cancel' for m in mrp_orders):
                order.manufacturing_status = 'cancel'
            else:
                order.manufacturing_status = 'in_progress'

    def _compute_mrp_order_count(self):
        for order in self:
            order.mrp_order_count = self.env['mrp.production'].search_count([('origin', '=', order.name)])

    def action_view_mrp_orders(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Manufacturing Orders',
            'res_model': 'mrp.production',
            'view_mode': 'tree,form',
            'domain': [('origin', '=', self.name)],
            'target': 'current',
        }
