def populate_models(sender, **kwargs):
    from django.apps import apps
    from .apps import StatesConfig as App1Config
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    group_app, created = Group.objects.get_or_create(name=App1Config.name)

    models = apps.all_models[App1Config.name]
    for model in models:
        content_type = ContentType.objects.get(
            app_label=App1Config.name,
            model=model
        )
        permissions = Permission.objects.filter(content_type=content_type)
        group_app.permissions.add(*permissions)

from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import State

@receiver(post_delete, sender=State)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user: # just in case user is not specified
        print(f'Deleting user : {instance.user.username}................')
        instance.user.delete()