from odoo import fields,models

class estate_property(models.Model):
    _name = "estate_property"
    _description="Estate Property"

    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    date_avaibility = fields.Date()
    expected_price = fields.Float(required = True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Boolean()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('West', 'west')]
    )