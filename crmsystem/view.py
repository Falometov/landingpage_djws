from django.shortcuts import render
from .models import Request
from .forms import RequestForm
from cmssystem.models import CmsSlider
from price.models import PriceCard
from telegrambot.sendmessage import sendTelegram

# Create your views here.
def first_page(request):
    slides_list = CmsSlider.objects.all()
    plans_list = PriceCard.objects.all()
    pc_bronze = PriceCard.objects.get(id=4)
    pc_silver = PriceCard.objects.get(id=5)
    pc_gold = PriceCard.objects.get(id=6)
    form = RequestForm()
    dict_obj = {'slides_list': slides_list,
                'pc_bronze': pc_bronze,
                'pc_silver': pc_silver,
                'pc_gold': pc_gold,
                'form': form,
                'plans_list': plans_list,
                }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        plan = request.POST['plan']
        new_element = Request(request_name=name, request_email=email, request_plan=plan)
        new_element.save()
        sendTelegram(tg_name = name, tg_plan = plan)
        return render(request, './thanks.html', {'name': name,
                                                 'email': email,
                                                 'plan': plan})
    else:
        return render(request, './thanks.html')

