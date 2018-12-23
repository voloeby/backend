from django.shortcuts import render
from django.shortcuts import get_object_or_404
from russianseasons.decorators import *
from russianseasons.models import *
from django.views import View
from django.http import HttpResponse


def shop_page(request):

    context = {}
    template_name = 'shop.html'
    context['items'] = ItemPrototype.objects.all()
    res = render(request, template_name, context)
    return res


class ItemView(View):
    def get(self, request, id):
        context = {}
        template_name = 'item_page.html'
        item = get_object_or_404(ItemPrototype, id=id)
        if item.images.count() > 0:
            item.main_image = item.images.all()[0]
            item.small_images = item.images.all()[1:]
        else:
            pass
        context['item'] = item
        return render(request, template_name, context)

    def post(self, request, id):
        item_prot = get_object_or_404(ItemPrototype, id=id)
        color, created = Color.objects.get_or_create(name=request.POST['color'])
        size, created = Size.objects.get_or_create(name=request.POST['size'])
        item, created = Item.objects.get_or_create(color=color, size=size, prototype=item_prot)
        order = Order()
        order.save()
        order.is_preorder = True
        order.email = request.POST['email']
        order.city = request.POST['city']
        order.items.add(item)
        order.save()
        return HttpResponse('ok')
