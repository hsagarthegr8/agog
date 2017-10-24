from django import template
from django.db.models import Q

register = template.Library()

from ..models import Connections

@register.assignment_tag
def is_connected(user1,user2):
    try:
        conn = Connections.objects.get(Q(user1=user1, user2=user2) | Q(user1=user2, user2=user1))
        return conn
    except:
        return None


