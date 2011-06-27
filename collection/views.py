from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.servers.basehttp import FileWrapper

from django.views.generic.list_detail import object_list

from settings import MEDIA_ROOT, _PROJECT_DIR
import settings
from models import Item

def index(request):
    #return list_items(request)
    return redirect('collection_list_paginated', page=1)

def download_item(request, object_id, object_path):
    return download_object(request, object_id, Item)

def download_object(request, object_id, obj):
    import os.path

    p = get_object_or_404(obj, pk=object_id)
    p.downloads += 1
    p.save()
    response = HttpResponse(p.filename, "application/octet-stream")
    response['Content-Length'] = p.filename.size
    return response

def collection_item(request, object_id):
    object = get_object_or_404(Item, id__exact=object_id)
    return render_to_response('item_detail.html', {'object': object,}, context_instance=RequestContext(request))

def collection_list(request, page=0, paginate_by=4, **kwargs):
    page_size = getattr(settings,'COLLECTION_PAGESIZE', paginate_by)
    return list_detail.object_list(
        request,
        queryset=Post.objects.published(),
        paginate_by=page_size,
        page=page,
        **kwargs
    )
def list_items(request, page=None):
    items = Item.objects.filter(private__exact=False)

    if not page:
        page = 1

    return object_list(request, queryset=items, paginate_by=4, page=page, template_name="collection/item_list.html",)
