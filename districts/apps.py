from django.apps import AppConfig
from django.db.models.signals import post_migrate


class DistrictsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'districts'

    def ready(self):
        from .signals import populate_models
        post_migrate.connect(populate_models, sender=self)