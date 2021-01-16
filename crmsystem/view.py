from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', { 'object_list': object_list,
                                             'form': form})


def thanks_page(request):
    name = request.GET['name']
    email = request.GET['email']
    new_elem = Order(order_name = name, order_email = email)
    new_elem.save()
    return render(request, './thanks.html')

