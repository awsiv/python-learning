@register.filter(name='getkey')
def getkey(value, arg):
    return value[arg]
