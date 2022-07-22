from django.http import HttpResponse
from django.template import loader

from catalog.models import Item


def index(request):
    items_list = Item.objects.all()

    template = loader.get_template('catalog/index.html')
    context = {
        'items_list': items_list,
    }
    return HttpResponse(template.render(context, request))


def item(request, item_id):
    item = Item.objects.get(id=item_id)
    resp = f"<h1>Item:</h1><ul>{item.__dict__}</ul>"
    return HttpResponse(resp)
