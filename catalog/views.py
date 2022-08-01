from django.shortcuts import render
from django.views.generic.edit import CreateView
from catalog.models import Contact, Item


def index(request):
    return render(request, 'catalog/index.html')


class ContactAdd(CreateView):
    model = Contact
    fields = '__all__'


def items(request, category_id=None, type=None):
    if category_id:
        items_set = Item.objects.filter(category_id=category_id)
    elif type:
        items_set = Item.objects.filter(type=type)
    else:
        items_set = Item.objects.all()
    context = {
        'items_set': items_set,
    }
    return render(request, 'catalog/items.html', context)


# def category(request, id):
#     items_set = Item.objects.filter(category__id=id)
#     context = {'items_set': items_set}
#     return render(request, 'catalog/items.html', context)


def item(request, item_id):
    item = Item.objects.filter(id=item_id)[0]
    context = {'item': item}
    return render(request, 'catalog/item.html', context)
