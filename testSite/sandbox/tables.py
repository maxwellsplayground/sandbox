import django_tables2 as tables
from .models import *

class CoffeeShopTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/shop/{{record.id}}">Edit</a>')

    class Meta:
        model = CoffeeShop
        
        
        