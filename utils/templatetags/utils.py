from django import template
register = template.Library()

from datetime import datetime,timezone

@register.simple_tag
def timesince(timestamp):
    now = datetime.now(timezone.utc)
    dif = now-timestamp
    if dif.days > 2:
        return timestamp.strftime('%b. %d, %Y')
    elif dif.days > 0:
        if dif.days == 1:
            return '1 day ago.'
        return '2 days ago.'
    elif dif.seconds < 60:
        return 'Just Now'
    elif dif.seconds < 3600:
        if dif.seconds//60 == 1:
            return '1 minute ago.'
        return str(dif.seconds//60) + ' minutes ago.'
    elif dif.seconds//3600 == 1:
        return '1 hour ago.'
    return str(dif.seconds//3600) + ' hours ago.'