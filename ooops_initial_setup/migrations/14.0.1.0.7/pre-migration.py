from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    view = env.ref('ooops_github_sync.module_form_inherit', raise_if_not_found=False)
    if view:
        view.unlink()
