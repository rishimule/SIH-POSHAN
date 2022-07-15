from django.apps import AppConfig
from django.db.models.signals import post_migrate


class TalukasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'talukas'

    def ready(self):
        from .signals import populate_models
        post_migrate.connect(populate_models, sender=self)