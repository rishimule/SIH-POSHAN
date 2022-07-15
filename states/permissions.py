from .apps import StatesConfig as App1Config

def is_in_group_schools(user):
    return user.groups.filter(name=App1Config.name).exists() 