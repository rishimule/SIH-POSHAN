from .apps import TalukasConfig as App1Config

def is_in_group_talukas(user):
    return user.groups.filter(name="talukas").exists() 