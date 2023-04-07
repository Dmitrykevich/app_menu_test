from django import template
from django.urls import resolve, reverse

from app_tree_menu_template_tag.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True, name=menu_name)
    active_item = None
    current_url = resolve(context['request'].path_info).url_name

    for item in menu_items:
        item.is_active = False
        if item.url == context['request'].path_info or item.named_url == current_url:
            item.is_active = True
            active_item = item
        item.children_all = item.children.all()

    context = {'menu_items': menu_items, 'active_item': active_item, 'current_url': current_url}
    return template.loader.render_to_string('app_tree_menu_template_tag/menu.html', context=context)
