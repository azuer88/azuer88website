from django import template
from django.core.urlresolvers import reverse

register = template.Library()

from home.models import MenuLink

def nav_menulinks():
    #home = reverse('home')
    #menu_list = [
    #    {'url': home, 'title': 'Home', 'caption': 'Home'},
    #]

    #menu_list = []
    #list = MenuLink.objects.filter(active=True).order_by('sequence')
    #for item in list:
    #    #item.deepcopy()
    #    item.url = reverse(item.name)
    #    #menu = item
    #    #menu['url'] = link
    #    menu_list.append(item)
    #return {'menulinks': menu_list}

    list = MenuLink.objects.all()

    return {'menulinks': list}

register.inclusion_tag('menu_links.html')(nav_menulinks)
