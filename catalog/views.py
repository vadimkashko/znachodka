from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.edit import CreateView
from catalog.models import Category, Contact, Item


def index(request):
    return render(request, 'catalog/index.html')


class ContactAdd(CreateView):
    model = Contact
    fields = '__all__'


def items(request, **kwargs):
    items_set = Item.objects.filter(**kwargs).order_by('create_date')

    # Pagination
    if (per_page := request.GET.get('per_page')):
        request.session['per_page'] = int(per_page)
    per_page = request.session.get('per_page', 12)
    paginator = Paginator(items_set, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Context
    context = {
        'items_set': items_set,
        'page_obj': page_obj,
        'per_page': per_page
    }

    # Context for breadcrumb
    for k, v in kwargs.items():
        if k == 'type':
            context[k] = next(filter(lambda x: v in x, Item.ITEM_TYPES))
        elif k == 'category_id':
            context['category'] = (
                v,
                Category.objects.get(id=v).name,
            )

    return render(request, 'catalog/items.html', context)


def item(request, item_id):
    item = Item.objects.filter(id=item_id)[0]
    context = {
        'item': item,
        'type': tuple(filter(lambda x: item.type in x, Item.ITEM_TYPES))[0][1],
        'category': Category.objects.get(id=item.category_id)
    }
    return render(request, 'catalog/item.html', context)
