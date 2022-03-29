# Copyright 2019 Roberto Fichera <roberto.fichera@levelprime.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = "res.company"

    e_invoice_transmitter_id = fields.Many2one(
        "res.partner",
        "E-bill Transmitter",
        help="This partner will be used as transmitter in out invoice.",
        default=lambda self: self.env.user.partner_id.id,
    )

    max_invoice_in_xml = fields.Integer(
        string="Max Invoice # in XML",
        default=0,
        help="Customer default for maximum number of invoices to group "
        "in a single XML file. 0=Unlimited",
    )

    @api.constrains("max_invoice_in_xml")
    def _validate_max_invoice_in_xml(self):
        if self.max_invoice_in_xml < 0:
            raise ValidationError(
                _(
                    "The customer default for max number of invoices to group "
                    "can't be negative"
                )
            )


class AccountConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    e_invoice_transmitter_id = fields.Many2one(
        related="company_id.e_invoice_transmitter_id", readonly=False
    )
    max_invoice_in_xml = fields.Integer(
        related="company_id.max_invoice_in_xml", readonly=False
    )

    @api.onchange("company_id")
    def onchange_company_id(self):
        res = super(AccountConfigSettings, self).onchange_company_id()
        if self.company_id:
            company = self.company_id
            self.max_invoice_in_xml = company.max_invoice_in_xml or 0
        else:
            self.max_invoice_in_xml = 0
        return res
