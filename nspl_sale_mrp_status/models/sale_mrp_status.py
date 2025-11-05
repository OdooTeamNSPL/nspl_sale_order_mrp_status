from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    manufacturing_status_name = fields.Selection([
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('no_mo', 'No MO')
    ], string="Manufacturing Status", compute="_compute_manufacturing_status", store=False, index=True)

    @api.depends('order_line.product_id','picking_ids.state',
                 'picking_ids.move_ids.state')
    def _compute_manufacturing_status(self):
        for order in self:
            mos = self.env['mrp.production'].search([('origin', '=', order.name)])
            if not mos:
                order.manufacturing_status_name = 'no_mo'
            elif all(mo.state == 'done' for mo in mos):
                # Agar delivery bhi done ho toh
                if all(p.state == 'done' for p in order.picking_ids):
                    order.manufacturing_status_name = 'done'
                else:
                    order.manufacturing_status_name = 'in_progress'
            elif any(mo.state in ['progress', 'planned', 'to_close'] for mo in mos):
                order.manufacturing_status_name = 'in_progress'
            else:
                order.manufacturing_status_name = 'confirmed'
