from .apps import DistrictsConfig as App1Config

def is_in_group_districts(user):
    return user.groups.filter(name=App1Config.name).exists() 