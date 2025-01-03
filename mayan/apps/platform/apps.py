from django.utils.translation import gettext_lazy as _

from mayan.apps.app_manager.apps import MayanAppConfig

from .classes import ClientBackend
from .platform_templates import PlatformTemplate


class PlatformApp(MayanAppConfig):
    app_namespace = 'platform'
    app_url = 'platform'
    has_rest_api = False
    has_tests = True
    name = 'mayan.apps.platform'
    verbose_name = _(message='Platform')

    def ready(self):
        super().ready()

        ClientBackend.load_modules()
        PlatformTemplate.load_modules()
