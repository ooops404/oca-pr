from odoo import SUPERUSER_ID, api


def post_init_hook(cr, pool):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["base.language.install"].create({
        'lang': 'it_IT',
        'overwrite': True,
    }).lang_install()

    env.ref('base.user_root').partner_id.write({'lang': 'it_IT'})
    env.ref('base.user_admin').partner_id.write({'lang': 'it_IT'})
    env.ref('base.default_user').partner_id.write({'lang': 'it_IT'})
    env.ref('base.public_user').partner_id.write({'lang': 'it_IT'})

    field_lang = env['ir.model.fields'].search([
        ('name', '=', 'lang'),
        ('model_id.model', '=', 'res.partner'),
    ])
    if field_lang:
        default_value = env['ir.default'].search([
            ('field_id', '=', field_lang.id),
            ('company_id', '=', False),
            ('user_id', '=', False),
        ])
        if default_value:
            default_value.write({'json_value': '"it_IT"'})
        else:
            env['ir.default'].create({
                'field_id': field_lang.id, 'json_value': '"it_IT"'
            })
