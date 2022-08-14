from .apps import SchoolsConfig as App1Config
from django.contrib.auth.decorators import login_required, user_passes_test


def is_in_group_schools(user):
    return user.groups.filter(name=App1Config.name).exists() 