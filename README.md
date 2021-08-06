[![Runbot Status](https://ops404.it/runbot/badge/flat//12.0.svg)](https://ops404.it/runbot/repo/git-github-com-ooops404-oca-pr-git-)
[![Build Status](https://github.com/ooops404/oca-pr/actions/workflows/ci-push.yml/badge.svg)](https://github.com/ooops404/oca-pr/actions/workflows/ci-push.yml)
[![Translation Status](http://weblate.ops404.it/widgets/oca-pr/-/svg-badge.svg)](http://weblate.ops404.it/engage/oca-pr/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# OCA PR for addons

Temporary repo containing OCA PR's

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | summary
--- | --- | ---
[pos_cache_user_restriction](pos_cache_user_restriction/) | 12.0.1.0.0 | Allow access to pos cache to restricted users
[sale_discount_display_amount](sale_discount_display_amount/) | 12.0.1.0.1 | This addon intends to display the amount of the discount computed on sale_order_line and sale_order level

[//]: # (end addons)

<!-- prettier-ignore-end -->

### Dependency from other GitHub repository

If the project depends on other OCA or other Github repositories, list the dependencies in `oca_dependencies.txt`. One per line like so:

    project_name optional_repository_url optional_branch_name


### Python dependency

If the project needs python dependency, add  to `requirements.txt`, one per line.


## Licenses

This repository is licensed under [LGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to OCA
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
