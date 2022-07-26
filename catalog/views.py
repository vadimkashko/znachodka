from django.shortcuts import render

from catalog.models import Item


def index(request):
    return render(request, 'catalog/index.html')


def items(request):
    items_list = Item.objects.all()
    context = {
        'items_list': items_list,
    }
    return render(request, 'catalog/items.html', context)


def item(request, item_id):
    item = Item.objects.filter(id=item_id)[0]
    context = {'item': item}
    return render(request, 'catalog/item.html', context)
