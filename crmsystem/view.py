from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cmssystem.models import CmsSlider
from price.models import PriceCard

# Create your views here.
def first_page(request):
    slides_list = CmsSlider.objects.all()
    pc_bronze = PriceCard.objects.get(id=4)
    pc_silver = PriceCard.objects.get(id=5)
    pc_gold = PriceCard.objects.get(id=6)
    dict_obj = {'slides_list': slides_list,
                'pc_bronze': pc_bronze,
                'pc_silver': pc_silver,
                'pc_gold': pc_gold
                }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    name = request.GET['name']
    email = request.GET['email']
    new_elem = Order(order_name = name, order_email = email)
    new_elem.save()
    return render(request, './thanks.html')

