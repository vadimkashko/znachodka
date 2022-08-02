from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('items/', views.items, name='all_items'),
    path('type/<str:type>', views.items, name='by_type'),
    path('category/<int:category_id>', views.items, name='by_category'),
    path('type_category/<str:type>/<int:category_id>',
         views.items,
         name='by_type_category'),
    path('item/<int:item_id>', views.item, name='item'),
    path('add_item/', views.ContactAdd.as_view(), name='add_item')
]
