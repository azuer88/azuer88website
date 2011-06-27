from django.shortcuts import render_to_response, get_object_or_404
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.template import RequestContext, Template

#from django.views.generic.list_detail import object_list

from settings import MEDIA_ROOT, _PROJECT_DIR

from django.contrib.flatpages.models import FlatPage

def index(request):
    #home = Flatpage.objects.get(url__exact = '/home/')
    home = get_object_or_404(FlatPage, url__exact = '/home/')

    return render_to_response("simple.html", {'object': home, }, context_instance=RequestContext(request))

def disclaimer(request):
    #home = Flatpage.objects.get(url__exact = '/home/')
    object = get_object_or_404(FlatPage, url__exact = '/disclaimer/')

    return render_to_response("simple.html", {'object': object, }, context_instance=RequestContext(request))


def static_path(request):
    return HttpResponse('Static Folder: ' + _PROJECT_DIR + '/media/public/')
