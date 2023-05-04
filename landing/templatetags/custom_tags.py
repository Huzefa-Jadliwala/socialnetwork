from django import template
from social.models import Notification

register = template.Library()

# funtion is used to fetch all the unseen notification of the current logged in user
@register.inclusion_tag('social/show_notifications.html', takes_context=True)
def show_notification(context):
    request_user = context['request'].user
    notifications  = Notification.objects.filter(to_user = request_user).exclude(user_has_seen=True).order_by('-date')
    return {'notifications': notifications}