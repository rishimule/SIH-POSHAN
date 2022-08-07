import os
import re
from datetime import datetime
from slugify import slugify

def _(something):
    """Simply returns the same thing

    Args:
        something (any): Anything

    Returns:
        any: Input parameter
    """
    return something

def get_current_datetime():
    """Returns alphanumeric datetime.

    Returns:
        str: alphanumeric DateTime
    """     
    return make_to_alphanumeric(datetime.now())

def make_to_alphanumeric(mystr):
    """Make a string in form of alphanumeric. 

    Args:
        mystr (str): String or something that can be converted to string

    Returns:
        str: alphanumeric output str
    """
    return re.sub('[\W_]+', '', str(mystr))

