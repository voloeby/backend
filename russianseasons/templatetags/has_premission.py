from django import template
register = template.Library()


@register.simple_tag
def has_premission(request, *args):
    if request.user.is_superuser:
        return True
    else:
        return False
