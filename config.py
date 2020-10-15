
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MYSITE",
    settings_files=['settings.yaml', '.secrets.yaml'],
    core_loaders = ['YAML'],
    yaml_loader = 'safe_load',
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
