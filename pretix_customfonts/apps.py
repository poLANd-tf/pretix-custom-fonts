from django.apps import AppConfig
from . import __version__


class PluginApp(AppConfig):
    name = 'pretix_customfonts'
    verbose_name = 'Fontpack: Custom fonts'

    class PretixPluginMeta:
        name = 'Fontpack: Custom fonts'
        author = 'Radosław Serba'
        description = 'Custom fonts for internal poLANd.tf use'
        visible = False
        version = __version__
        compatibility = "pretix>=2026.8.0.dev0"

    def ready(self):
        from . import signals  # NOQA