from django.shortcuts import render
from models.ItemPrototype import ItemPrototype
from django.views import View

class ShopView(View):
    template_name = 'admin/shop_page.html'

    def get(self, request):
        context = {}
        template_name = 'admin/shop_page.html'
        context['items'] = ItemPrototype.objects.all()
        return render(request, template_name, context)
