from django import template
register = template.Library()

@register.filter(name='addclass')
def addclass(field, css):
    return field.as_widget(attrs={"class":css})

@register.filter(name='disablefield')
def disablefield(field):
    return field(disabled = True)