from __future__ import unicode_literals

from django.apps import AppConfig


class WebinteractiveConfig(AppConfig):
    name = 'webinteractive'
    def ready(self):
        import signals
